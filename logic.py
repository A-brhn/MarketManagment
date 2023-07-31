from datetime import date

def printSpecificType(types, selected):
    if selected == 1:
        name = "junkFood"
    elif selected == 2:
        name = "drink"
    elif selected == 3:
        name = "diary"
    elif selected == 4:
        name = "sanitary"
    else:
        name = "protein"

    condition = 0
    for t in types:
        if t.name == name:
            for good in t.goodsList:
                good.showDetails()
            print("\n")
            condition = 1
    if condition == 0:
        print("There is no such type in your bill !!!\n")


def sortByPrice(types):

    allGoodsList = []
    for type in types:
        for good in type.goodsList:
            allGoodsList.append(good)
    allGoodsList.sort(key=lambda g:g.price, reverse=False)
    for good in allGoodsList:
        good.showDetails()
    print("\n")

def sortByEDAte(types):
    allGoodsList = []
    for type in types:
        for good in type.goodsList:
            allGoodsList.append(good)
    allGoodsList.sort(key=lambda g: g.expirationDate, reverse=False)
    for good in allGoodsList:
        good.showDetails()
    print("\n")

def sortByQuantity(types):
    allGoodsList = []
    for type in types:
        for good in type.goodsList:
            allGoodsList.append(good)
    allGoodsList.sort(key=lambda g: g.quantity, reverse=False)
    for good in allGoodsList:
        good.showDetails()
    print("\n")

def showRottenGoods(types):
    rottenGoodsList = []
    for type in types:
        for good in type.goodsList:
            if good.expirationDate < date.today():
                rottenGoodsList.append(good)
    print(f"today : {date.today().year}-{date.today().month}-{date.today().day}")
    for good in rottenGoodsList:
        good.showDetails()
    print("\n")

def calculateTotalPrice(types):
    totalPrice = 0
    for type in types:
        for good in type.goodsList:
            totalPrice += good.price
    print(f"the total price is : {totalPrice}")
    print("\n")
