#!/bin/bash
mkdir -p ~/.system-monitor
cd ~/.system-monitor

if [ ! -d "system-monitor" ]; then
	git clone https://github.com/ivole32/system-monitor
fi

cd system-monitor
git pull

python3 ./main.py