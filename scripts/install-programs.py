#!/usr/bin/env bash

import os
import subprocess

def run_command(command):
  subprocess.run(command, shell=True, check=True)

# Change directory
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

# Install for debian-based distros
if subprocess.call("command -v apt-get > /dev/null", shell=True) == 0:
  run_command("xargs -a './programs.txt' sudo apt-get install -y")
