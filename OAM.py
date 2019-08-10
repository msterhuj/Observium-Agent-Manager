from setting import setting as parameter
from function.colors import colors

def main():
    setting = parameter()
    color = colors()
    print(color.green + setting.banner)
    pass

if __name__ == '__main__':
    main()
