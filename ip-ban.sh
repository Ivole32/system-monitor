#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <IP-ADDRESS>"
    exit 1
fi

IP="$1"

echo "[*] Blocking all traffic to and from IP $IP..."

sudo ufw deny from "$IP"
sudo ufw deny out to "$IP"

sudo iptables -I INPUT -s "$IP" -j DROP
sudo iptables -I OUTPUT -d "$IP" -j DROP

sudo iptables -I FORWARD -s "$IP" -j DROP
sudo iptables -I FORWARD -d "$IP" -j DROP

if command -v conntrack >/dev/null 2>&1; then
    echo "[*] Terminating existing connections to/from $IP..."
    sudo conntrack -D -s "$IP"
    sudo conntrack -D -d "$IP"
else
    echo "[!] 'conntrack' is not installed – cannot terminate existing connections."
    echo "You can install it with: sudo apt install conntrack"
fi

echo "[✓] IP $IP has been fully blocked."