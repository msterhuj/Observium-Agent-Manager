import os
import distro
import function.colors as color

################################
# you can change this settings #
bypass_root_check = False

######################
# Script Message Var #
banner = "\n" \
         " _____ _                   _              _____             _      _____                         \n" \
         "|     | |_ ___ ___ ___ _ _|_|_ _ _____   |  _  |___ ___ ___| |_   |     |___ ___ ___ ___ ___ ___ \n" \
         "|  |  | . |_ -| -_|  _| | | | | |     |  |     | . | -_|   |  _|  | | | | .'|   | .'| . | -_|  _|\n" \
         "|_____|___|___|___|_|  \_/|_|___|_|_|_|  |__|__|_  |___|_|_|_|    |_|_|_|__,|_|_|__,|_  |___|_|  \n" \
         "                                               |___|                                |___|        \n" \
         "\n"
beta_message = "[!] This is a beta version !\n" \
               "[!] If you have any bugs please create an issue on the Observium-Agent-Manager project\n" \
               "[!] "+color.underlined+"https://github.com/msterhuj/Observium-Agent-Manager"+color.reset_underlined+"\n" \
               "[!] Thank"

#################################
# System value please dont edit #
dist_name = distro.name()
dist_ver = distro.version()
dist_codename = distro.codename()
dist_supported_list = ["debian", "ubuntu", "kali"]
