#!/usr/bin/env python3

import os
import subprocess

def run_command(command):
  subprocess.run(command, shell=True, check=True)

# Check if /etc/inittab exists
if os.path.isfile("/etc/inittab"):
  # For non-systemd distros
  run_command("sudo cp /etc/inittab /etc/inittab.bak")
  run_command("sed -i '/1:2345/s/^/#/' /etc/inittab")
  run_command("sed -i \"/1:2345/a\\1:2345:respawn:/bin/login -f $USER tty1 </dev/tty1 >/dev/tty1 2>&1\" /etc/inittab")
else:
  # For systemd distros
  if not os.path.exists("/etc/systemd/system/getty@tty1.service.d"):
    run_command("sudo mkdir /etc/systemd/system/getty@tty1.service.d")

  systemd_config = "[Service]\n" \
    "ExecStart=\n" \
    "ExecStart=-/sbin/agetty -o '-p -f -- \\\\\\\\u' --noclear --autologin $USER %%I $TERM\n"

  with open("/etc/systemd/system/getty@tty1.service.d/autologin.conf", "w") as file:
    file.write(systemd_config)
