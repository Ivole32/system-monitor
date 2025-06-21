#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <IP-ADDRESS>"
    exit 1
fi

IP="$1"

echo "[*] Unblocking all traffic to and from IP $IP..."

sudo ufw delete deny from "$IP" 2>/dev/null
sudo ufw delete deny out to "$IP" 2>/dev/null

sudo iptables -D INPUT -s "$IP" -j DROP 2>/dev/null
sudo iptables -D OUTPUT -d "$IP" -j DROP 2>/dev/null
sudo iptables -D FORWARD -s "$IP" -j DROP 2>/dev/null
sudo iptables -D FORWARD -d "$IP" -j DROP 2>/dev/null

echo "[✓] IP $IP has been fully unblocked."