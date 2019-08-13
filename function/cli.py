import setting as setting
import function.core as core
import function.colors as color


def run():
    answer = question()
    if answer == 9:
        core.end_program()
    elif answer == 1:
        print()
    elif answer == 2:
        print()
    elif answer == 3:
        print()
    elif answer == 4:
        print()
    elif answer == 5:
        print()


def question() -> int:
    print(color.green)
    print("Observium Agent Manager")
    print("1. Install UNIX-Agent (snmpd-config will be overwritten)")
    print("2. Manage agent script")
    print("3. Remove Agent")
    print("4. Purge Temp file")
    print("9. Quit")
    try:
        input_choice = int(input("# "))
        return input_choice
    except ValueError as e:
        print(color.red + color.bold + "Invalid input !")
        question()
