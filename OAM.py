# -*-coding:UTF-8 -*
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

banner = "Observium Agent Manager"
beta_message = "This is a beta version !\n" \
               "If you have any bugs please create an issue on the Observium-Agent-Manager project" \
               "Thank"

dist_name = distro.name()
dist_ver = distro.version()
dist_codename = distro.codename()

dist_supported_list = ["debian"]


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
    print(GREEN + "End of programme Thank you for using me." + NOCOLOR)
    print(beta_message + NOCOLOR)
    print("")
    exit(0)


##########################################################################
# Start point of python script
print(GREEN + banner)
print(RED + beta_message)

# verification requirements for running this script
if user_root():
    print(GREEN + "Root user : OK")
else:
    print(RED + "please run this script as root")
    end_program()

if dist_supported():
    print(GREEN + "Distribution Support : OK")
    print(GREEN + dist_name + ", " + dist_ver + ", " + dist_codename)
else:
    print(RED + "Your's Distribution is not supported by this script"
                "Create a issue on the project so that in a future version you will get your distribution")
    end_program()

end_program()
