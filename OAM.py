# -*- coding: utf-8 -*-
###
# This script is under development for manage snmp client config
# By MsterHuj
# https://github.com/msterhuj/Observium-Agent-Manager
###

# THIS SCRIPT IS NOT FINISH PLEASE DONT USE IT !

import os
import distro

# var stock

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NOCOLOR = '\033[0m'

banner = "[*] Observium Agent Manager Python script"
beta_message = "[!] This is a beta version !\n" \
               "[!] If you have any bugs please create an issue on the Observium-Agent-Manager project\n" \
               "[!] Thank"

dist_name = distro.name()
dist_ver = distro.version()
dist_codename = distro.codename()

dist_supported_list = ["debian", "ubuntu", "kali"]

cliStatus = True


# def function
def user_root(): # return bool / check user is root
    if os.getuid() == 0:
        return True
    else:
        return False


def dist_supported(): # return bool / check system allow to use script
    for dist_check in dist_supported_list:
        if dist_check in dist_name.lower():
            return True
    return False


def end_program(): # return null / stop the programme and remove color on cli
    print("")
    print(GREEN + "End of programme Thank you for using me.")
    print(RED + beta_message)
    print(NOCOLOR)
    exit(0)


def check_script_all_ok(): # return bool / check if script can be run
    error = False
    if user_root():
        print(GREEN + "[*] Root user : OK")
    else:
        print(RED + "[!] Please run this script as root")
        error = True

    if dist_supported():
        print(GREEN + "[*] Distribution Support : OK")
        print(GREEN + "[*] " + dist_name + ", " + dist_ver + ", " + dist_codename)
    else:
        print(RED + "[!] Your's Distribution is not supported by this script\n"
                    "[!] Create a issue on the project so that in a future version you will get your distribution")
        error = True

    if error:
        return False
    else:
        return True


def cli():
    while cliStatus:
        print(GREEN + "[*] All right starting agent !")
        print("")
        print("Observium Agent Manager")
        print("1. Intall UNIX-Agent (snmpd-config will be overwritten)")
        print("2. Manage agent script")
        print("3. Remove Agent")
        print("9. Quit")
        input_choice = input("# ") # TODO make a system for check if is number

        if input_choice == "1":
            # run func install agent
            print(NOCOLOR + "run func install agent")
        elif input_choice == "2":
            # run func agent Manager
            print(NOCOLOR + "run func agent Manager")
        elif input_choice == "3":
            # run func remove agentAddress
            print(NOCOLOR + "run func remove agentAddress")
        elif input_choice == "9":
            print("")
            end_program()
        else:
            print(RED + "Invalid Number !")


##########################################################################
# Start point of python script
print(GREEN + banner)
print(RED + beta_message)
print("")

# verification requirements for running this script
if check_script_all_ok():
    cli()
else:
    print("Error detected fix it to use me please :p")

print("")
print("This script is not finished yet I am still working on it")
print("")

end_program()
