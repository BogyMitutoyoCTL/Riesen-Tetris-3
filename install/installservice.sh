#!/bin/bash
cp LED.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable LED
service LED start
