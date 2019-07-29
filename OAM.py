# -*- coding: utf-8 -*-
###
# This script is under development for manage snmp client config
# By MsterHuj
# https://github.com/msterhuj/Observium-Agent-Manager
###

# THIS SCRIPT IS NOT FINISH PLEASE DONT USE IT !

import os
import distro
import wget
import tarfile

# var stock

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NOCOLOR = '\033[0m'

banner = "[*] Observium Agent Manager Python script"
beta_message = "[!] This is a beta version !\n" \
               "[!] If you have any bugs please create an issue on the Observium-Agent-Manager project\n" \
               "[!] https://github.com/msterhuj/Observium-Agent-Manager\n" \
               "[!] Thank"

dist_name = distro.name()
dist_ver = distro.version()
dist_codename = distro.codename()

dist_supported_list = ["debian", "ubuntu", "kali"]


# def function
def user_root():  # return bool / check user is root
    if os.getuid() == 0:
        return True
    else:
        return False


def dist_supported():  # return bool / check system allow to use script
    for dist_check in dist_supported_list:
        if dist_check in dist_name.lower():
            return True
    return False


def end_program():  # return null / stop the programme and remove color on cli
    print("")
    print(GREEN + "End of programme Thank you for using me.")
    print(RED + beta_message)
    print(NOCOLOR)
    exit(0)


def check_script_all_ok():  # return bool / check if script can be run
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


def pkg_apt():
    if "debian" or "ubuntu" in dist_supported_list:  # TODO update the checker by list an mane detect
        return True


def install_agent_observium_ce():
    print("Downloading Observium CE...")
    wget.download("http://www.observium.org/observium-community-latest.tar.gz", "/opt/observium-community-latest.tar.gz")
    print("\nExtract tar file...")
    file = tarfile.open("/opt/observium-community-latest.tar.gz")
    file.extractall("/opt/observium/")
    print("Install agent dependence")
    if pkg_apt():
        print(GREEN + "Update apt source" + YELLOW)
        os.system("apt-get update")
        print(GREEN + "Install dependence" + YELLOW)
        os.system("apt-get -qq install -y xinetd snmpd libwww-perl")


def cli():
    cliStatus = True
    while cliStatus:
        print(GREEN + "")
        print("Observium Agent Manager")
        print("1. Install UNIX-Agent (snmpd-config will be overwritten)")
        print("2. Manage agent script")
        print("3. Remove Agent")
        print("4. Purge Temp file")
        print("9. Quit")
        input_choice = input("# ")  # TODO make a system for check if is number

        if input_choice == "1":
            # run func install agent
            install_agent_observium_ce()

        elif input_choice == "2":
            # run func agent Manager
            print(NOCOLOR + "run func agent Manager")

        elif input_choice == "3":
            # run func remove agent Manager
            print(NOCOLOR + "run func remove agentAddress")

        elif input_choice == "4":
            print("Removing temp file")
            try:
                os.remove("/opt/observium-community-latest.tar.gz")
                print("Removed")
            except OSError as exep:
                print(RED + "Error : file not fond or other error" + GREEN)

        elif input_choice == "9":
            print("Quitting...")
            cliStatus = False

        else:
            print(RED + "Invalid Number !")


##########################################################################
# Start point of python script
print("")
print("")
print(GREEN + banner)
print("")
print("")

# verification requirements for running this script
if check_script_all_ok():
    print(GREEN + "[*] All right starting agent !")
    cli()
else:
    print("")
    print(RED + "Error detected fix it to use me please :p")
    print("")

print("")
print(GREEN + "This script is not finished yet I am still working on it")
print("")

end_program()
