#!/usr/bin/env bash

import subprocess

def run_command(command):
  subprocess.run(command, shell=True, check=True)

# Install dependencies
if subprocess.call("command -v apt-get > /dev/null", shell=True) == 0:
  run_command("sudo apt-get install -y wget")

# Download and install neovim
run_command("wget https://github.com/neovim/neovim/releases/latest/download/nvim.appimage")
run_command("chmod +x nvim.appimage")
run_command("sudo mv nvim.appimage /usr/local/bin/nvim")
