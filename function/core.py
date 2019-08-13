import os
import function.colors as color
import setting


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

def load_core():
    pass
