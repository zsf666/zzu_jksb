#!/bin/bash
value=$(<crontab.txt)
echo "$value" >> /var/spool/cron/crontabs/root
crontab -e
