# nvconf

A Python command to interact with the bbswitch kernel module and the Nvidia Prime command tool.

### Compatibility

This script is ONLY compatible with Ubuntu as it relies on the bbswitch kernel module.
**Make sure proprietary/open Nvidia driver is active, NOT  NOUVEAU**

### Setup:
- Install bbswitch on your system: `sudo apt install bbswitch-dkms`

- Automated install with script:
  - Run the install script for nvconf: `sudo ./install.py`
- Manual install:
  - Copy the nvconf file to `/usr/local/bin/`

- Run the setup for nvconf: `sudo nvconf --setup`

### Usage
- `nvconf --on` -- This will set the nvidia prime profile to 'on-demand' and power on the GPU after reboot
- `nvconf --off` -- This will set the nvidia prime profile to 'intel' and power off the GPU after reboot
- `nvconf --status` -- Show the current nvidia prime status as well as GPU power status

- Use the `--help` flag for help with nvconf options and usage.

