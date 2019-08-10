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
        #################################
        # System value please dont edit #
        #################################
        self.banner = "\n" \
                 " _____ _                   _              _____             _      _____                         \n" \
                 "|     | |_ ___ ___ ___ _ _|_|_ _ _____   |  _  |___ ___ ___| |_   |     |___ ___ ___ ___ ___ ___ \n" \
                 "|  |  | . |_ -| -_|  _| | | | | |     |  |     | . | -_|   |  _|  | | | | .'|   | .'| . | -_|  _|\n" \
                 "|_____|___|___|___|_|  \_/|_|___|_|_|_|  |__|__|_  |___|_|_|_|    |_|_|_|__,|_|_|__,|_  |___|_|  \n" \
                 "                                               |___|                                |___|        \n" \
                 "\n"
