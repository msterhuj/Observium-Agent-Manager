# -*- coding: utf-8 -*-
import setting as setting
import function.core as core
import function.colors as color


def run():
    runned = True
    while runned:
        answer = menu_question()
        if answer == 9:
            runned = False
            core.end_program()
        elif answer == 1:
            print("install agent")
        elif answer == 2:
            print("edit agent if installed")
        elif answer == 3:
            print("remove agent")
        elif answer == 4:
            print("del temp file")
        elif answer == 5:
            print("just install snmp agent")
        else:
            print(color.red + color.bold + "Invalid input !")


def menu_question() -> int:
    print(color.green)
    print("Observium Agent Manager")
    print("1. Install UNIX-Agent (snmpd-config will be overwritten)")
    print("2. Edit agent config")
    print("3. Remove Agent")
    print("4. Purge Temp file")
    print("5. Only config snmp agent")
    print("9. Quit")
    try:
        input_choice = int(input("# "))
        return input_choice
    except ValueError:
        print(color.red + color.bold + "Invalid input !")
        menu_question()
