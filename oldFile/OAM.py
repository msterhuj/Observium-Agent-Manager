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
