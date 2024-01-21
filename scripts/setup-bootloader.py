#!/usr/bin/env python3

import os
import subprocess

def run_command(command):
  subprocess.run(command, shell=True, check=True)

# Change Grub Timeout
if os.path.isfile("/etc/default/grub"):
  run_command("sudo sed -i '/GRUB_TIMEOUT/ c\\GRUB_TIMEOUT=0' /etc/default/grub")
  run_command("sudo grub-mkconfig -o /boot/grub/grub.cfg")

# Change systemd-boot Timeout
if os.path.isfile("/boot/loader/loader.conf"):
  run_command("sudo sed -i '/timeout/ c\\timeout 0' /boot/loader/loader.conf")
