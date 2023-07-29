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

