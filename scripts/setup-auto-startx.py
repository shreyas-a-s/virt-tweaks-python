#!/usr/bin/env bash

import subprocess

def run_command(command):
  subprocess.run(command, shell=True, check=True)

# Setup for zsh
if subprocess.call("command -v zsh > /dev/null", shell=True) == 0:
  zsh_config = "\
  \nif [ -z \"$DISPLAY\" ] && [ $(tty) = /dev/tty1 ]; then\
  \n  startx\
  \nfi"

  run_command(f"printf '{zsh_config}' | sudo tee -a /etc/zsh/zprofile > /dev/null")

# Setup for bash
if subprocess.call("command -v bash > /dev/null", shell=True) == 0:
  bash_config = "\
  \nif [ -z \"$DISPLAY\" ] && [ $(tty) == /dev/tty1 ]; then\
  \n  startx\
  \nfi"

  run_command(f"printf '{bash_config}' | tee -a ~/.bashrc > /dev/null")
