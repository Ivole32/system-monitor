#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP-ADDRESS> <PORT>"
    exit 1
fi

IP="$1"
PORT="$2"

echo "[*] Blocking IP $IP and port $PORT..."

sudo ufw deny from "$IP" to any port "$PORT"
sudo ufw deny out to "$IP" port "$PORT"

sudo iptables -I INPUT -s "$IP" -j DROP
sudo iptables -I OUTPUT -d "$IP" -j DROP

if command -v conntrack >/dev/null 2>&1; then
    echo "[*] Terminating existing connections to/from $IP..."
    sudo conntrack -D -s "$IP"
    sudo conntrack -D -d "$IP"
else
    echo "[!] 'conntrack' is not installed – cannot terminate existing connections."
    echo "You can install it with: sudo apt install conntrack"
fi

echo "[✓] IP $IP has been blocked."