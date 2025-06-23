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
            self.commands.append(command)

    def check_command(self, user_command) -> bool | int:
        i = 0
        for command in self.commands:
            if user_command == command[0]:
                return True, i
            else:
                i += 1
        return False, 0

    def create_command(self, command_name, command_exec, command_arguments, command_description) -> None:
        config_commands = ast.literal_eval(self.config.get_config_value("commands", topic='custom-commands'))

        config_commands.append([command_name, command_exec, command_arguments, command_description, True])

        option = {"commands": config_commands}

        self.config.write_to_config(option, topic="custom-commands")

        self.add_commands()

    def delete_command(self, command_name) -> None:
        config_commands = ast.literal_eval(self.config.get_config_value("commands", topic='custom-commands'))

        for command in config_commands:
            if command[0] == command_name:
                config_commands.remove(command)

                option = {"commands": config_commands}

                self.config.write_to_config(option, topic="custom-commands")
                self.console.print("Command deleted")

                self.add_commands()

                return

        self.console.print("No matching command found")

    def set_command_enabling_mode(self, command_name, mode) -> None:
        config_commands = ast.literal_eval(self.config.get_config_value("commands", topic='custom-commands'))

        for command in config_commands:
            if command[0] == command_name:
                command[-1] = mode  
                break

        option = {"commands": config_commands}

        self.config.write_to_config(option, topic="custom-commands")

        self.add_commands()

        if mode:
            console.print("Enabled command")
        else:
            console.print("Disbaled command")

    def execute_command(self, command) -> str | None:
        if command == "exit":
            exit(0)

        elif command == "q":
            return "break flag"

        elif command == "help":
            help_text = r"""
exit                        – Exit the program
help                        – Show this help message
q                           – Quit the terminal
create                      – Creates a new custom command
delete <COMMAND>            – Deletes a custom command
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
                name = custom_command[0] + " " + custom_command[2]
                description = custom_command[3]

                padded_name = name.ljust(27)
                command_string = f"{padded_name} – {description}"
                if custom_command[-1] == False:
                    command_string += " (Disabled)\n"
                else:
                    command_string += "\n"
                help_text += command_string

            self.console.print(help_text, style="")

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

        elif "ssh-timeout" in command:
            system_command = command.replace("ssh-timeout", "./ssh-timeout.sh")
            os.system(system_command)

        elif "ip-ban" in command:
            system_command = command.replace("ip-ban", "./ip-ban.sh")
            os.system(system_command)

        elif "ip-unban" in command:
            system_command = command.replace("ip-unban", "./ip-unban.sh")
            os.system(system_command)

        elif "ip-timeout" in command:
            system_command = command.replace("ip-timeout", "./ip-timeout.sh")
            os.system(system_command)

        elif command == "create":
            return "create"

        elif "delete" in command:
            command_name = command.replace("delete ", "")
            self.delete_command(command_name)

        elif "enable" in command:
            command_name = command.replace("enable ", "")
            self.set_command_enabling_mode(command_name, True)

        elif "disable" in command:
            command_name = command.replace("disable ", "")
            self.set_command_enabling_mode(command_name, False)

        else:
            custom_command_check, custom_command_index = self.check_command(command)
            arguments = command.replace(f"{self.commands[custom_command_index][0]} ", "")
            self.console.print(f"{arguments}")
            arguments = arguments.split(" ")
            if custom_command_check:
                if self.commands[custom_command_index][-1]:
                    system_command = self.commands[custom_command_index][1]
                    if elf.commands[custom_command_index][2] != "":
                        i = 1
                        while True:
                            try:
                                system_command.replace(f"${i}", arguments[i-1])
                                i += 1

                            except:
                                break

                    os.system(self.commands[custom_command_index][1])

            else:
                if self.allow_system_commands:
                    os.system(command)