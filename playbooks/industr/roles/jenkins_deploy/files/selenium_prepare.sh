#!/bin/bash

# Firefox
apt-get install -y firefox-esr

# Geckdriver
cd /usr/local/bin/
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
chmod +x geckodriver

# Selenium
pip install selenium
