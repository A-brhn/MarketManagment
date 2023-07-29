from logic import *

def start(types):
    print("to see a Specific type Enter     : 1")
    print("to sort by price Enter           : 2")
    print("to sort by eDate enter           : 3")
    print("to sort by Quantity Enter        : 4")
    print("to see the rotten items Enter    : 5")
    print("to see the total price           : 6")
    print("to see the details of bill Enter : 7")
    print("to Exit                          : 8")

    selected = int(input("\r\nPlease Enter your choice: "))

    if selected == 1:
        printTypeMenu(types)
    elif selected == 2:
        sortByPrice(types)
        start(types)
    elif selected == 3:
        sortByEDAte(types)
        start(types)
    elif selected == 4:
        sortByQuantity(types)
        start(types)
    elif selected == 5:
        pass
    elif selected == 6:
        pass
    elif selected == 7:
        pass
    elif selected == 8:
        pass
    else:
        print("please Enter a correct option\n")
        start(types)

def printTypeMenu(types):
    print("to see junkFoods Enter  : 1")
    print("to see drinks Enter     : 2")
    print("to see diaries Enter    : 3")
    print("to see sanitaries Enter : 4")
    print("to see proteins Enter   : 5")
    print("back to Menu            : 6")

    selected = int(input("\r\nPlease Enter your choice: "))

    if 1 <= selected <= 5:
        printSpecificType(types, selected)
        printTypeMenu(types)
    elif selected == 6:
        start(types)
    else:
        print("please Enter a correct option")
        printTypeMenu(types)








