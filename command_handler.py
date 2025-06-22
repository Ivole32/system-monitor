import os
import ast

class command_handler():
    def __init__(self, console, config, allow_system_commands) -> None:
        self.console = console
        self.config = config
        self.allow_system_commands = allow_system_commands
        self.add_commands()

    def add_commands(self) -> None:
        self.commands = []
        self.config_commands = ast.literal_eval(self.config.get_config_value("commands", topic='custom-commands'))

        for command in self.config_commands:
            if command[3]:
                self.commands.append(command)

    def check_command(self, user_command) -> bool | int:
        i = 0
        for command in self.commands:
            if user_command == command[0]:
                return True, i
            else:
                i += 1
        return False, 0

    def execute_command(self, command) -> str | None:
        if command == "exit":
            exit(0)

        elif command == "q":
            return "break flag"

        elif command == "help":
            help_text = """\
exit                        – Exit the program
help                        – Show this help message
q                           – Quit the terminal
create                      – Creates a new command
delete                      – Deletes a custom command
enable/disable <COMMAND>    – Eanbles/Disables a custom command
kill <PID,...>              – Kill the specified process(es) by PID
ssh-ban <IP> [PORT]         – Permanently block SSH access from the given IP (default port is 22)
ssh-unban <IP> [PORT]       – Remove SSH block for the given IP (default port is 22)
ssh-timeout <IP> [PORT]     – Temporarily block SSH access from the given IP (default port is 22)
ip-ban <IP>                 – Permanently block all traffic from the given IP
ip-unban <IP>               – Remove all traffic blocks for the given IP
ip-timeout <IP> <SECONDS>   – Temporarily block all traffic from the given IP for the specified duration
"""
            for custom_command in self.commands:
                name = custom_command[0]
                description = custom_command[2]

                padded_name = name.ljust(27)
                command_string = f"{padded_name} – {description}"
                help_text += command_string

            self.console.print(help_text)

        elif "kill" in command:
            try:
                pids = command.split("kill ")[1].split(",")
                for pid in pids:
                    if os.system(f"kill {pid}") == 0:
                        self.console.print(f"[green]Killed PID: {pid}[/green]")
                    else:
                        self.console.print(f"[red]Error while killing PID: {pid}[/red]")
            except Exeption as e:
                self.console.print(f"[red]{e}[/red]")

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

        else:
            custom_command_check, custom_command_index = self.check_command(command)
            if custom_command_check:
                os.system(self.commands[custom_command_index][1])

            else:
                if self.allow_system_commands:
                    os.system(command)