# Installation

## 1. Install all linux packages
If you are not the administrator of the system you have to skip to 2. but unfortunally you won't have the abillity to use the build in command line to ban or timeout IP's and more.
### 1.1 Updating your system
To update your system use ```sudo apt update```

### 1.2 Install packages
To install all packages use ```sudo apt install iptables, conntrack, ufw```

### 1.3 Enable ufw
To enable the ufw service use ```sudo systemctl enable ufw```
<br>Make sure to start ufw (```sudo systemctl start ufw```) and check if everything is installde correctly with ```sudo systemctl status ufw```

## 2. Install all python requirements
To install all pyton requirements cd into the repository and run ```pip install -r requirements.txt```