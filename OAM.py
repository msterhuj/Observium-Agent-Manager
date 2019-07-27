# -*- coding: utf-8 -*-
###
# This script is under development for manage snmp client config
# By MsterHuj
# https://github.com/msterhuj/Observium-Agent-Manager
###

# THIS SCRIPT IS NOT FINISH PLEASE DONT USE IT !

import os
import distro
from switch import Switch

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

dist_supported_list = ["debian", "ubuntu"]


# def function
def user_root():
    if os.getuid() == 0:
        return True
    else:
        return False


def dist_supported():
    for dist_check in dist_supported_list:
        if dist_check in dist_name.lower():
            return True
    return False


def end_program():
    print("")
    print(GREEN + "End of programme Thank you for using me.")
    print(RED + beta_message)
    print(NOCOLOR)
    exit(0)


##########################################################################
# Start point of python script
print(GREEN + banner)
print(RED + beta_message)
print("")

# verification requirements for running this script
if user_root():
    print(GREEN + "[*] Root user : OK")
else:
    print(RED + "[!] Please run this script as root")
    end_program()

if dist_supported():
    print(GREEN + "[*] Distribution Support : OK")
    print(GREEN + "[*] " + dist_name + ", " + dist_ver + ", " + dist_codename)
else:
    print(RED + "[!] Your's Distribution is not supported by this script\n"
                "[!] Create a issue on the project so that in a future version you will get your distribution")
    end_program()

print(GREEN + "[*] All right starting agent !")
print("")
print("Observium Agent Manager")
print("1. Intall UNIX-Agent (snmpd-config will be overwritten)")
print("2. Manage agent script")
print("3. Remove Agent")
print("9. Quit")
input_choice = input("# ")



print("")
print("This script is not finished yet I am still working on it")
print("")

end_program()
