import os
from setting import setting as setting_import

class core():

    """
        core of script
    """


    def __init__(self):
        self.is_root = False
        self.is_supported_os = False
        self.script_ready = False


    def __is_root__(self) -> bool:
        if os.getuid() == 0:
            return True
        else:
            return False


    def __is_supported_os__(self):
        setting = setting_import()
        for dist_check in setting.dist_supported_list:
            if dist_check in setting.dist_name.lower():
                return True
        return False


    def load_core(self):
        self.is_root = self.__is_root__()
        self.is_supported_os = self.__is_supported_os__()
        pass
