#!/bin/sh

echo "Viewing output of mypl-hw1 package!"

echo "Output of mypl-hw1"
sudo journalctl -u mypl-hw1 -n 50 --no-pager