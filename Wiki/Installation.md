## 1. Install all linux packages
If you are not the administrator of the system you have to skip to 2. but unfortunally you won't have the abillity to use the build in command line to ban or timeout IP's and more.

### 1.1 Updating your system
To update your system use ```sudo apt update```

### 1.2 Install packages
To install all packages use ```sudo apt install iptables, conntrack, ufw```

### 1.3 Enable ufw
To enable the ufw service use ```sudo systemctl enable ufw```
<br>Make sure to start ufw (`Q``sudo systemctl start ufw```) and check if everything is installed correctly with ```sudo systemctl status ufw```

## 2. Cloning the repository
### 2.1 cd into the right place
You should open a terminal and use ```cd``` to move to the directory you want the repository to be safed in.

## 2.2 Clone the repository
Use ```git clone https://github.com/ivole32/system-monitor```to clone the repository into your files.

If you don't have git installed:
#### 1. Solution
You can find the installation instructions for git [here](https://github.com/git-guides/install-git).

#### 2. Solution
You can also download the repository manually from [here](https://github.com/ivole32/system-monitor).


## 3. Install python requirements
To install all pyton requirements cd into the repository and run ```pip install -r requirements.txt```

Currently there is no documentation to install the python requirements in a venv. But hey you are on linux. Find it out by yourself.

**If** you want to use the program as **sudo user** (for the build in command line) make sure you use sudo before the ```pip``` command.

If you want to know how tu use the program look [here](https://github.com/Ivole32/system-monitor/wiki/Usage)