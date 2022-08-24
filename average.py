# HEADING INTERFACE VARIABLE
border = "========================================"
space = " "
title = "WELCOME TO AVERAGE CALCULATION SYSTEM!"
version = "0.0.1"
description = "Just enter the number of data to find an average."
author = "Created by: Yerenzter"
language = "Written in Python 3"

# MAIN MENU VARIABLE
hintMenu = "Please enter a number to select options..."
hintInput = "Enter your number: "
menu1 = "(1) Enter"
menu2 = "(2) Exit"

# AVERAGE MAIN MENU VARIABLE
hintAM = "Select the type: "
aMenu1 = "(1) Integer Type"
aMenu2 = "(2) Float Type"
aMenu3 = "(3) All"

# MAIN PROGRAM STRING VARIABLE
numberOfData = "Please enter your number of data: "
enterData = "Enter your data: "
dataList = []
result = "Your average is "
integer = "Integer value: "
floats = "Float value: "
roundUp = "Round up: "
realNumber = "Real Number: "

# HOME PROMPT INTERFACE VARIABLE
ask = "Do you want proceed to main menu?"
yes = "(1) Yes"
no = "(2) No"
finish = "(3) Exit"

# ERROR HANDLING MESSAGE VARIABLE
STATUS_CODE_0001 = "STATUS_CODE(1)::EXCEED_VALUE_ERROR"
STATUS_CODE_0002 = "STATUS_CODE(2)::UNEXPECTED_TYPE_ERROR"
STATUS_CODE_0003 = "STATUS_CODE(3)::SUCCESS"

# ERROR RESOLVER MESSAGE VARIABLE
STATUS_CODE_0001_RESOLVE = "The value exceeds from the maximum given list. To resolve the problem please enter the value that does not more than a maximum integer value."

STATUS_CODE_0002_RESOLVE = "Unexpected type occur, to resolve the problem please enter the value according to the type (e.g String, Integer, Float, Character etc.) given by the program."

STATUS_CODE_0003_RESOLVE = "Program finished. No errors & warnings occured."

PROGRAM_RESOLVE = "Solution? "

# PROGRAM STRING LIST VARIABLE
programList = [border, space, title, version, description, author, language, space, border, space, space, hintMenu, space, menu1, menu2, space]

aMenuList = [hintAM, aMenu1, aMenu2, aMenu3]

homeMenuList = [ask, yes, no, finish]

for programLists in programList:
    print(programLists)

prompt = int(input(hintInput))

def STATUS_CODE_0001():
    print(space)
    print(STATUS_CODE_0001)
    print(space)
    print(PROGRAM_RESOLVE + STATUS_CODE_0001_RESOLVE)

def STATUS_CODE_0002():
    print(space)
    print(STATUS_CODE_0002)
    print(space)
    print(PROGRAM_RESOLVE + STATUS_CODE_0002_RESOLVE)

def STATUS_CODE_0003():
    print(space)
    print(STATUS_CODE_0003)
    print(space);
    print(PROGRAM_RESOLVE + STATUS_CODE_0003_RESOLVE)

def avgMenu():
    print(space)

    for aMenuLists in aMenuList:
        print(aMenuLists)

    print(space)

    prompt = int(input(hintInput))

    if prompt == 1:
        avgInteger()
    elif prompt == 2:
        avgFloat()
    elif prompt == 3:
        avgAll()
    else:
        STATUS_CODE_0001()

def avgHome():
    print(space)

    for homeMenuLists in homeMenuList:
        print(homeMenuLists)

    prompt = int(input(hintInput))

    if prompt == 1:
        avgMenu()
    elif prompt == 2:
        STATUS_CODE_0003()
    elif prompt == 3:
        exit()
    else:
        avgHome()

def avgInteger():
    value = int(input(numberOfData))

    for values in range(value):
        data = int(input(enterData))

        if True:
            dataList.append(data)

    sums = sum(dataList)

    average = int(sums / value)

    print(result + str(average))

    STATUS_CODE_0003()

    avgHome()

def avgFloat():
    value = int(input(numberOfData))

    for values in range(value):
        data = float(input(enterData))

        if True:
            dataList.append(data)

    sums = sum(dataList)

    average = float(sums / value)

    print(result + str(average))

    STATUS_CODE_0003()

    avgHome()

def avgAll():
    value = int(input(numberOfData))

    for values in range(value):
        data = float(input(enterData))

        if True:
            dataList.append(data)

    sums = sum(dataList)

    averageInt = int(sums / value)
    averageFloat = float(sums / value)
    averageRU = round(int(sums /value))

    print(space)
    print(result)
    print(space)
    print(integer + str(averageInt))
    print(floats + str(averageFloat))
    print(roundUp + str(averageRU))
    print(realNumber + str(averageInt))

    STATUS_CODE_0003()

    avgHome()

# EVENT HANDLING FOR A MAIN MENU
if prompt == 1:
    avgMenu()
elif prompt == 2:
    exit()
else:
    STATUS_CODE_0001()
