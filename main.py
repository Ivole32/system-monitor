import keyboard
import psutil
import time
import os

from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align

from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

console = Console()
history = InMemoryHistory()

min_cpu, max_cpu = None, None
min_ram, max_ram = None, None
min_disk, max_disk = None, None

history.append_string("help")

def get_system_stats_table():
    global min_cpu, max_cpu, min_ram, max_ram, min_disk, max_disk

    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    if min_cpu is None or cpu_percent < min_cpu:
        min_cpu = cpu_percent
    if max_cpu is None or cpu_percent > max_cpu:
        max_cpu = cpu_percent

    if min_ram is None or ram_percent < min_ram:
        min_ram = ram_percent
    if max_ram is None or ram_percent > max_ram:
        max_ram = ram_percent

    if min_disk is None or disk_percent < min_disk:
        min_disk = disk_percent
    if max_disk is None or disk_percent > max_disk:
        max_disk = disk_percent

    table = Table(title="System Monitor", expand=True)
    table.add_column("Component", style="cyan", justify="right")
    table.add_column("Current", style="green")
    table.add_column("Min", style="green")
    table.add_column("Max", style="red")

    table.add_row("CPU", f"{cpu_percent:.1f} %", f"{min_cpu:.1f} %", f"{max_cpu:.1f} %")
    table.add_row("RAM", f"{ram_percent:.1f} %", f"{min_ram:.1f} %", f"{max_ram:.1f} %")
    table.add_row("Disk", f"{disk_percent:.1f} %", f"{min_disk:.1f} %", f"{max_disk:.1f} %")

    return table

def get_top_processes_table(max_rows):
    table = Table(title="Top Processes (by CPU)", expand=True)
    table.add_column("PID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("CPU %", style="green", justify="right")
    table.add_column("RAM %", style="red", justify="right")

    process_list = list(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']))
    top_processes = sorted(process_list, key=lambda p: p.info['cpu_percent'], reverse=True)[:max_rows]

    for proc in top_processes:
        try:
            pid = str(proc.info['pid'])
            name = (proc.info['name'] or "")[:18]
            cpu = f"{proc.info['cpu_percent']:.1f}"
            ram = f"{proc.info['memory_percent']:.1f}"
            table.add_row(pid, name, cpu, ram)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return table

def get_ssh_connections_table():
    table = Table(title="SSH Connections", expand=True)

    table.add_column("Local Addr", style="cyan", overflow="fold")
    table.add_column("Remote Addr", style="magenta", overflow="fold")
    table.add_column("Status", style="green", justify="center", overflow="fold")
    table.add_column("PID", style="red", justify="right", overflow="fold")

    for conn in psutil.net_connections(kind='inet'):
        try:
            if conn.status == 'ESTABLISHED' and conn.laddr.port == 22:
                local_addr = f"{conn.laddr.ip}:{conn.laddr.port}"
                remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
                status = conn.status
                pid = str(conn.pid) if conn.pid else "-"
                table.add_row(local_addr, remote_addr, status, pid)
        except Exception:
            continue

    return table

def main_loop():
    command_log = []
    while True:
        if keyboard.is_pressed('c'):
            console.print("[bold yellow]Command mode activated![/bold yellow] (Submit with Enter, cancel with Ctrl+C or q)")
            while True:
                try:
                    command = prompt("Command > ", history=history)
                    if command == "exit":
                        exit(0)

                    elif command == "q":
                        break

                    elif command == "help":
                        console.print("""\
                        exit                        – Exit the program
                        help                        – Show this help message
                        q                           – Quit the terminal
                        kill <PID,...>              – Kill the specified process(es) by PID
                        ssh-ban <IP> [PORT]         – Permanently block SSH access from the given IP (default port is 22)
                        ssh-unban <IP> [PORT]       – Remove SSH block for the given IP (default port is 22)
                        ssh-timeout <IP> [PORT]     – Temporarily block SSH access from the given IP (default port is 22)
                        ip-ban <IP>                 – Permanently block all traffic from the given IP
                        ip-unban <IP>               – Remove all traffic blocks for the given IP
                        ip-timeout <IP> <SECONDS>   – Temporarily block all traffic from the given IP for the specified duration
                        """)

                    elif "kill" in command:
                        try:
                            pids = command.split("kill ")[1].split(",")
                            for pid in pids:
                                if os.system(f"kill {pid}") == 0:
                                    console.print(f"[green]Killed PID: {pid}[/green]")
                                else:
                                    console.print(f"[red]Error while killing PID: {pid}[/red]")
                        except Exeption as e:
                            console.print(f"[red]{e}[/red]")

                    elif "ssh-ban " in command:
                        system_command = command.replace("ssh-ban", "./ssh-ban.sh")
                        os.system(system_command)

                    elif "ssh-unban " in command:
                        system_command = command.replace("ssh-ban", "./ssh-unban.sh")
                        os.system(system_command)
                                            
                    elif command == "ssh-timeout":
                        system_command = command.replace("ssh-timeout", "./ssh-timeout.sh")
                        os.system(system_command)

                    elif command == "ip-ban":
                        system_command = command.replace("ip-ban", "./ip-ban.sh")
                        os.system(system_command)

                    elif command == "ip-unban":
                        system_command = command.replace("ip-unban", "./ip-unban.sh")
                        os.system(system_command)

                    elif command == "ip-timeout":
                        system_command = command.replace("ip-timeout", "./ip-timeout.sh")
                        os.system(system_command)

                except KeyboardInterrupt:
                    console.print("[red]Entry canceled.[/red]")
                    break
            
            time.sleep(1)
            continue

        layout = Layout()

        layout.split_row(
            Layout(name="system", ratio=2),
            Layout(name="processes", ratio=4),
            Layout(name="ssh", ratio=2),
        )

        system_table = get_system_stats_table()
        layout["system"].update(Panel(Align.center(system_table), title="System Overview", border_style="cyan"))

        terminal_height = console.size.height
        max_process_rows = max(3, terminal_height - 10)
        process_table = get_top_processes_table(max_process_rows)
        layout["processes"].update(Panel(Align.center(process_table), title="Top Processes", border_style="magenta"))

        ssh_table = get_ssh_connections_table()
        layout["ssh"].update(Panel(Align.center(ssh_table), title="SSH Connections", border_style="green"))

        console.clear()
        console.print(layout)

        time.sleep(1)

if __name__ == "__main__":
    main_loop()