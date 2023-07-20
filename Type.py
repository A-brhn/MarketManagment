class Type:

    def __init__(self, name, goodslist):
        self.name = name
        self.goodsList = goodslist

    def showdetails(self):
        print(self.name + ":")
        for i in range(0, len(self.goodsList)):
            print(f"    {self.goodsList[i].name} :")
            print(f"        price : {self.goodsList[i].price}")
            print(f"        quantity : {self.goodsList[i].quantity}")
            print(f"        productionDate :{self.goodsList[i].productionDate}")
            print(f"        expirationDate : {self.goodsList[i].expirationDate}")
