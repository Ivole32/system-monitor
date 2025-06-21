#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP-ADDRESS> <PORT>"
    exit 1
fi

IP="$1"
PORT="$2"

echo "[*] Unblocking IP $IP and port $PORT..."

sudo ufw delete deny from "$IP" to any port "$PORT"
sudo ufw delete deny out to "$IP" port "$PORT"

sudo iptables -D INPUT -s "$IP" -j DROP 2>/dev/null
sudo iptables -D OUTPUT -d "$IP" -j DROP 2>/dev/null

echo "[✓] IP $IP has been unblocked."