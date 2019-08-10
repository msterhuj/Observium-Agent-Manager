import os
from function.Colors import Colors as color

class Checker():

    def isScriptReady(dist_supported_list: list, dist_name: str, dist_ver: str, dist_codename: str) -> bool:
        error = False
         if isRoot():
             print(color.green() + "[*] Root user : OK")
         else:
             print(color.red() + "[!] Please run this script as root")
             error = True

         if isSupportedOS(dist_name, dist_supported_list):
             print(color.green() + "[*] Distribution Support : OK")
             print(color.green() + "[*] " + dist_name + ", " + dist_ver + ", " + dist_codename)
         else:
             print(color.green() + "[!] Your's Distribution is not supported by this script\n"
                         "[!] Create a issue on the project so that in a future version you will get your distribution")
             error = True

         if error:
             return False
         else:
             return True
        print("HIEN")
        return False
