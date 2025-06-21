#!/bin/bash

IP="$1"
TIMEOUT="${2:-600}"

if [ -z "$IP" ]; then
    echo "Usage: $0 <IP-ADDRESS> [TIMEOUT_SECONDS]"
    exit 1
fi


sudo ipset create blacklist hash:ip timeout "$TIMEOUT" 2>/dev/null


sudo ipset add blacklist "$IP" timeout "$TIMEOUT"

sudo iptables -C INPUT -m set --match-set blacklist src -j DROP 2>/dev/null || \
sudo iptables -I INPUT -m set --match-set blacklist src -j DROP

sudo iptables -C OUTPUT -m set --match-set blacklist dst -j DROP 2>/dev/null || \
sudo iptables -I OUTPUT -m set --match-set blacklist dst -j DROP

echo "[✓] IP $IP has been temporarily blocked for $TIMEOUT seconds."