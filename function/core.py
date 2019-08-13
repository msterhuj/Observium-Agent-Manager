import os
import setting as setting
import function.colors as color
import function.cli as cli


def is_root() -> bool:
    if os.getuid() == 0:
        return True
    else:
        return False


def is_supported_os() -> bool:
    for dist_check in setting.dist_supported_list:
        if dist_check in setting.dist_name.lower():
            return True
    return False


def load():
    print(color.green + "Checking is this System can use the script")
    can_start = True
    if is_root():
         print(color.green + "[*] Root user : OK")
    else:
        print(color.red + "[!] Please run this script as root")
        can_start = False

    if is_supported_os():
        print(color.green + "[*] Distribution Support : OK")
        print(color.green + "[*] " + setting.dist_name + ", " + setting.dist_ver + ", " + setting.dist_codename)
    else:
        print(color.green + "[!] Your's Distribution is not supported by this script\n"
                            "[!] Create a issue on the project so that in a future version you will get your distribution")
        can_start = False

    if can_start == False:
        print(color.red + "Unable to start the OAM please correct error above")
        end_program()

    print(color.green + "Start OAM !")
    cli.run()
    pass


def end_program():  # return null / stop the programme and remove color on cli
    print("")
    print(color.green + "End of programme Thank you for using me.")
    print(color.yellow + setting.beta_message)
    print(color.reset)
    exit(0)
