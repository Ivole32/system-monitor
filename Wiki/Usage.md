# With executable
## Open the download location
Use ```cd <path>``` to go to the download location of the file

## Run program
Use ```./system-monitor``` to run the program

**Note:** If you want to use the command line tool run the command with ````sudo```

# Build from source
## Non root user (only display)
### 1. cd to repository
Open a terminal and use ```cd <Repository Path>```

### 2. Run the python script
Go to the terminal type ```./venv/bin/python3 ./main.py``` and hit enter.

## Root user (for the build in command tool)
### 1. cd to repository
Open a terminal and use ```cd <Repository Path>```

### 2. Run the python script
Go to the terminal type ```sudo python3 ./main.py``` and hit enter.

Now you can see the system monitor. If you want to use the build in command tool proced to step **3**.

### 3. Use the command line tool
To use the build in command line tool simply press ```c``` and wait untill ```Command >``` pops up.

You can now use help to see the commands or go [here](#build-in-commands)

## Build in commands
### `exit`
Exits the whole program.

### `q`
Exits the command line tool and displays the normal monitoring screen.

### `help`
Shows a quick help messages with all commands that are descibed here.

### `kill <PID,...>`
Takes a list of PID's seperated by an comma and kills all of them.

### `ssh-ban <IP> [PORT]`
Bans a specific IP for SSH access to the system. It takes an IP of the remot host to ban and the local SSH port (This argument is optional -> standart: 22).

### `ssh-unban <IP> [PORT]`
Unbans a specific IP for SSH access on the system. It takes the IP of the banned remote system and the local SSH port (This argument is optional -> standart: 22).

### `ssh-timeout <IP> [PORT]`
Timeouts a specific IP for SSH access to the system. It takes the IP of the remote host you want to timeout and the local SSH port (This argument is optional -> standart: 22).

### `ip-ban <IP>`
Permanently block all traffic from the given IP. It takes the IP of the remote system.

### `ip-unban <IP>`
Unbans a banned IP to reallow traffic from the given IP. It takes the IP of the remote system.

**Note:** This will unban the IP for all traffic but **not** if you banned the IP for SSH. You have to do this by yourself with [`ssh-unban`](#ssh-unban-ip-port)

### `ip-timeout <IP> <SECONDS>`
Timeouts traffic from a specific IP for the given time in seconds. It takes the IP to timeout and the timeout time in seconds.

### `create`
If you want to create custom commands in the build in command line you can use `create`.<br>Just answer the questions about the name, the execution command and the description.<br>
The custom command creation follow a very strict system so read this well. <br>
<br>The first question that the terminal will ask you is the name of the command. This will be the name you will type in to run it.<br>Please do **not** use commas or spaces.<br><br>
Next it will ask you for the execution command.<br>If you want to use aguments within your command replace those with `$<argument number>`. To use unlimmited arguments type `$*`, but this can only be done for the **last** argument you want to put in the command.<br><br>
After this it will ask you to specify the arguments. Press enter if there are no arguments you want to use. if you have arguments type <argument_name> for each argument seperated by an space in the right order (`$1` is first then `$2`,... ). If you used an unlimmited argument type `<argument_name,...>` (after all the $<number>).


### `delete <COMMAND>`
If you want to delete a custom command you can use this.

### `disable <COMMAND>`
Use this to disable a custom command. 

### `enable <COMMAND>`
Use this to (re)enable a custom command.

## Command tabel
| Command                       | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| `exit`                         | Exit the program                                                           |
| `help`                        | Show this help message                                                     |
| `q`                           | Quit the terminal                                                          |
| `create`                      | Create a new command                                                       |
| `delete <COMMAND>`            | Delete a custom command                                                    |
| `enable/disable <COMMAND>`    | Enable or disable a custom command                                         |
| `kill <PID,...>`              | Kill the specified process(es) by PID                                      |
| `ssh-ban <IP> [PORT]`         | Permanently block SSH access from the given IP (default port is 22)        |
| `ssh-unban <IP> [PORT]`       | Remove SSH block for the given IP (default port is 22)                     |
| `ssh-timeout <IP> [PORT]`     | Temporarily block SSH access from the given IP (default port is 22)        |
| `ip-ban <IP>`                 | Permanently block all traffic from the given IP                            |
| `ip-unban <IP>`               | Remove all traffic blocks for the given IP                                 |
| `ip-timeout <IP> <SECONDS>`   | Temporarily block all traffic from the given IP for the specified duration |