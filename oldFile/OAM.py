# -*- coding: utf-8 -*-
###
# This script is under development for manage snmp client config
# By MsterHuj
# https://github.com/msterhuj/Observium-Agent-Manager
###

# THIS SCRIPT IS NOT FINISH PLEASE DONT USE IT !

import os
import shutil as flm
import distro
import wget
import tarfile
from function.Checker import Checker as check
from function.Colors import Colors as color

# var stock

banner = "\n" \
         " _____ _                   _              _____             _      _____                         \n" \
         "|     | |_ ___ ___ ___ _ _|_|_ _ _____   |  _  |___ ___ ___| |_   |     |___ ___ ___ ___ ___ ___ \n" \
         "|  |  | . |_ -| -_|  _| | | | | |     |  |     | . | -_|   |  _|  | | | | .'|   | .'| . | -_|  _|\n" \
         "|_____|___|___|___|_|  \_/|_|___|_|_|_|  |__|__|_  |___|_|_|_|    |_|_|_|__,|_|_|__,|_  |___|_|  \n" \
         "                                               |___|                                |___|        \n" \
         "\n"
beta_message = "[!] This is a beta version !\n" \
               "[!] If you have any bugs please create an issue on the Observium-Agent-Manager project\n" \
               "[!] https://github.com/msterhuj/Observium-Agent-Manager\n" \
               "[!] Thank"

dist_name = distro.name()
dist_ver = distro.version()
dist_codename = distro.codename()

dist_supported_list = ["debian", "ubuntu", "kali"]


def end_program():  # return null / stop the programme and remove color on cli
    print("")
    print(color.green() + "End of programme Thank you for using me.")
    print(color.red() + beta_message)
    print(color.reset())
    exit(0)


def cli():
    cliStatus = True
    while cliStatus:
        print(color.green() + "")
        print("Observium Agent Manager")
        print("1. Install UNIX-Agent (snmpd-config will be overwritten)")
        print("2. Manage agent script")
        print("3. Remove Agent")
        print("4. Purge Temp file")
        print("9. Quit")
        input_choice = input("# ")  # TODO make a system for check if is number

        if input_choice == "1":
            # run func install agent
            # install_agent_observium_ce()
            print("Disabled Func")

        elif input_choice == "2":
            # run func agent Manager
            print(color.reset() + "run func agent Manager")

        elif input_choice == "3":
            # run func remove agent Manager
            print(color.reset() + "run func remove agentAddress")

        elif input_choice == "4":
            print("Removing temp file")
            try:
                os.remove("/opt/observium-community-latest.tar.gz")
                print("Removed")
            except OSError as exep:
                print(color.red() + "Error : file not fond or other error" + color.green())

        elif input_choice == "9":
            print("Quitting...")
            cliStatus = False

        else:
            print(color.red() + "Invalid Number !")


##########################################################################
# Start point of python script
def main():
    print("")
    print("")
    print(color.green() + banner)
    print("")
    print("")

    # verification requirements for running this script
    if check.isScriptReady(dist_supported_list, dist_name, dist_ver, dist_codename):
        print(color.green() + "[*] All right starting agent !")
        cli()
    else:
        print("")
        print(color.red() + "[!] Error detected fix it to use me please :p")
        print("")

    print("")
    print(color.green() + "[!] This script is not finished yet I am still working on it [!]")
    print("")

    end_program()


if __name__ == '__main__':
    main()
