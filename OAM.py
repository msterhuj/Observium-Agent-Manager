from setting import setting as setting_import
from function.core import core as core_import
from function.colors import colors


def main():
    setting = setting_import()
    color = colors()
    core = core_import()

    core.load_core()
    pass


if __name__ == '__main__':
    main()
