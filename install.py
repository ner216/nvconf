#!/usr/bin/env python3

#script that copies scripts in /src/ directory to system

#Built in imports
import os
import subprocess
import sys

#Get user who is running script
SUDOER = os.environ.get('SUDO_USER')
USER = os.getlogin()
#Exit script if it is not run as sudo:
if not SUDOER or USER == "root":
    print("Script must be run as root or sudo.")
    exit()

#Constant variables
SCRIPTS_PATH = "src/"
INSTALL_PATH = "/usr/local/bin/"

def copy_scipts(scripts_to_install: list) -> None:
    for script in os.listdir(SCRIPTS_PATH):
        if script != ".gitignore" and script in scripts_to_install:
            print(f" Copying {SCRIPTS_PATH}{script} to {INSTALL_PATH}{script}")
            os.popen(f"sudo cp {SCRIPTS_PATH}{script} {INSTALL_PATH}{script}")

def remove_scipts(scripts_to_remove) -> None:
    for script in os.listdir(SCRIPTS_PATH):
        if script != ".gitignore" and script in scripts_to_remove:
            print(f" Removing {INSTALL_PATH}{script}")
            os.popen(f"sudo rm {INSTALL_PATH}{script}")

def list_scripts() -> list:
    script_names = []

    for script in os.listdir(SCRIPTS_PATH):
        if script != ".gitignore":
            script_names.append(script)

    return script_names

def main():
    all_script_names = list_scripts()
    select_script_by_name = []
    scripts_to_install = []
    print(f"This script is used to copy or remove scripts from the {INSTALL_PATH} directory.")
    #Flag variables
    uninstall_arg = False
    help_arg = False
    version_info_arg = False

    #Process arguments
    for arg in sys.argv:
        if arg == "uninstall":
            uninstall_arg = True
        elif str(arg) == "help":
            help_arg = True
        elif str(arg) == "version" or arg == "ver":
            version_info_arg = True
        elif str(arg) in all_script_names:
            select_script_by_name.append(str(arg))

    #Compute command based on given argument
    if help_arg == True:
        print("Commands: ")
        print(" -- Install scripts: install.py install [Optional script names seperated by space]")
        print(" -- uninstall scripts: install.py uninstall [Optional script names seperated by space]")
        print(" -- dry run the program: install.py dryrun")
        print(" -- Get this help message: install.py help")
        print(" -- Get version info: install.py [version/ver]")
        exit()
    elif version_info_arg == True:
        print("Version: 0.1")
        print("Creator: Nolan Provencher")
        print("GitHub: https://github.com/ner216/linux_scripts")
        exit()
    elif uninstall_arg == True:
        print("Scipts to be uninstalled: ")
        if len(select_script_by_name) == 0: #No script name as arguments were used
            for script in all_script_names:
                print(f" {script}")
            scripts_to_install = all_script_names
        else:
            for script in select_script_by_name:
                print(f" {script}")
            scripts_to_install = select_script_by_name
        uninstall_confirmation = input(f"Remove scripts from {INSTALL_PATH}?(y/N) ")
        if uninstall_confirmation == "y":
            remove_scipts(scripts_to_install)
        else:
            exit()
    else: #Run install option by default
        print("Scipts that can be installed: ")
        if len(select_script_by_name) == 0: #No script name as arguments were used
            for script in all_script_names:
                print(f" {script}")
            scripts_to_install = all_script_names
        else:
            for script in select_script_by_name:
                print(f" {script}")
            scripts_to_install = select_script_by_name
        install_confirmation = input(f"Copy scripts to {INSTALL_PATH}?(y/N) ")
        if install_confirmation == "y":
            copy_scipts(scripts_to_install)
            print("Done.")
        else:
            exit()

main()

