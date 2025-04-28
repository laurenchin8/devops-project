#!/bin/sh

echo "Testing opl hw1 assignment..."

echo "Installing pytest..."
sudo apt-get update -qq
sudo apt install -y -q python3-pip
sudo pip3 install -q pytest

echo "Running the 28 unit tests..."
pytest ./hw1_tests.py
