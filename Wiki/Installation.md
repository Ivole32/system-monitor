# Install from executable
## 1. Download the executable
Download the file from [here](https://github.com/Ivole32/system-monitor/releases/download/Full/system-monitor)

## 2. Thats it
Follow the usage instructions [here](https://github.com/Ivole32/system-monitor/wiki/Usage)

# Install from source
## 1. Install all linux packages
If you are not the administrator of the system you have to skip to 2. but unfortunally you won't have the abillity to use the build in command line to ban or timeout IP's and more.

### 1.1 Updating your system
To update your system use ```sudo apt update```

### 1.2 Install packages
To install all packages use ```sudo apt install iptables conntrack ufw python3-pip python3-venv```

### 1.3 Enable ufw
To enable the ufw service use ```sudo systemctl enable ufw```
<br>Make sure to start ufw (```sudo systemctl start ufw```) and check if everything is installed correctly with ```sudo systemctl status ufw```

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
To create a venv cd into the repository and run ```python3 -m venv venv```
<br>To install all pyton requirements run ```./venv/bin/python3 -m pip install -r requirements.txt --no-cache```

**If** you want to use the program as **sudo user** (for the build in command line) make sure you use sudo before the every command. 

**Note:** On **Fedora Linux** I had to run ```sudo dnf install python3.13-devel```, because pip wasn't abled to install ```pynput``` without that. If you don't want to use the command line you can also remove ```pynput==1.8.1``` from ```requirements.txt```

**NOTE: There can be issues installing the pip packages because of missing system packages. In this case speak to your system administrator or open an issue.**

If you want to know how to use the program look [here](https://github.com/Ivole32/system-monitor/wiki/Usage)