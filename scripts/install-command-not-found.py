#!/usr/bin/env python3

import subprocess

def run_command(command):
  subprocess.run(command, shell=True, check=True)

# Install for debian-based distros
if subprocess.call("command -v apt-get > /dev/null", shell=True) == 0:
  # Install the app
  run_command("sudo apt-get install -y command-not-found")

  # Update database of command-not-found
  run_command("sudo update-command-not-found")
  run_command("sudo apt-file update")

# Install for archlinux-based distros
if subprocess.call("command -v pacman > /dev/null", shell=True) == 0:
  # Install the app
  run_command("sudo pacman -S --noconfirm pkgfile")

  # Update database of pkgfile
  run_command("sudo pkgfile -u")
