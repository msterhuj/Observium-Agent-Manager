import os
import distro

class setting():
    """
        This file containe all parameter of script
    """

    def __init__(self):
        ################################
        # you can change this settings #
        self.bypass_root_check = False
        ######################
        # Script Message Var #
        self.banner = "\n" \
                 " _____ _                   _              _____             _      _____                         \n" \
                 "|     | |_ ___ ___ ___ _ _|_|_ _ _____   |  _  |___ ___ ___| |_   |     |___ ___ ___ ___ ___ ___ \n" \
                 "|  |  | . |_ -| -_|  _| | | | | |     |  |     | . | -_|   |  _|  | | | | .'|   | .'| . | -_|  _|\n" \
                 "|_____|___|___|___|_|  \_/|_|___|_|_|_|  |__|__|_  |___|_|_|_|    |_|_|_|__,|_|_|__,|_  |___|_|  \n" \
                 "                                               |___|                                |___|        \n" \
                 "\n"
        self.beta_message = "[!] This is a beta version !\n" \
                            "[!] If you have any bugs please create an issue on the Observium-Agent-Manager project\n" \
                            "[!] https://github.com/msterhuj/Observium-Agent-Manager\n" \
                            "[!] Thank"
        #################################
        # System value please dont edit #
        self.dist_name = distro.name()
        self.dist_ver = distro.version()
        self.codename = distro.codename()
        self.dist_supported_list = ["debian", "ubuntu", "kali"]
