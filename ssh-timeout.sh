#!/bin/bash

IP="$1"
TIMEOUT="${2:-600}"

if [ -z "$IP" ]; then
    echo "Usage: $0 <IP-ADRESS> [TIMEOUT_SECONDS]"
    exit 1
fi

sudo ipset liste sshblock >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "[*] Creating ipset 'sshblock' with timeout..."
    sudo ipset create sshblock hash:ip timeout "$TIMEOUT"
fi

sudo ipset add sshblock "$IP" timeout "$TIMEOUT"

sudo iptables -C INPUT -p tcp --dport 22 -m set --match-set sshblock src -j DROP 2>/dev/null || \
sudo iptables -I INPUT -p tcp --dport 22 -m set --match-set sshblock src -j DROP

echo "[✓] SSH access for $IP has been blocked for $TIMEOUT seconds."