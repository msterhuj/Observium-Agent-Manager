import os


RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NOCOLOR = '\033[0m'


# Check if script run by root
def isRoot() -> bool:
    if os.getuid() == 0:
        return True
    else:
        return False


# Check is os is sported by this script
def isSupportedOS(currentDist: str, distSupported: list) -> bool:
    for dist_check in distSupported:
        if dist_check in currentDist.lower():
            return True
    return False


def isScriptReady(dist_supported_list: list, dist_name: str, dist_ver: str, dist_codename: str) -> bool:
    error = False
    if isRoot():
        print(GREEN + "[*] Root user : OK")
    else:
        print(RED + "[!] Please run this script as root")
        error = True

    if isSupportedOS(dist_name, dist_supported_list):
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
