#!/usr/bin/env python3

import os
import shutil
import subprocess

# Define needed functions
def run_command(command):
  subprocess.run(command, shell=True, check=True)

# Change directory
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

# Custom scripts
run_command('scripts/install-command-not-found.py')            # Install command-not-found handler
run_command('scripts/install-nvim.py')                         # Install neovim
run_command('scripts/install-programs.py')                     # Install programs
run_command('scripts/setup-auto-startx.py')                    # Setup auto startx
run_command('sudo python3 scripts/setup-autologin-to-tty.py')  # Setup autologin to tty
run_command('scripts/setup-bootloader.py')                     # Set bootloader timeout to 0 sec

# Setup zsh as user shell
zsh_env_setup = "printf '### SET XDG DIR FOR ZSH ###\\nZDOTDIR=~/.config/zsh\\n' | sudo tee -a /etc/zsh/zshenv > /dev/null"
zsh_path = shutil.which("zsh")
if zsh_path:
  try:
    run_command(zsh_env_setup)
    run_command(f'chsh -s "{zsh_path}"')
  except subprocess.CalledProcessError:
    print("Error setting Zsh as the user shell.")
else:
  print("Zsh is not installed or not in the PATH.")

# Set xfce4-terminal as default
run_command('sudo update-alternatives --set x-terminal-emulator /usr/bin/xfce4-terminal.wrapper')
