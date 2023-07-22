class Type:

    def __init__(self, name, goodslist):
        self.name = name
        self.goodsList = goodslist

    def showdetails(self):
        print(f"{self.name} :")
        for good in self.goodsList:
            print(f"    {good.name} :")
            print(f"        price : {good.price}")
            print(f"        quantity : {good.quantity}")
            print(f"        productionDate :{good.productionDate}")
            print(f"        expirationDate : {good.expirationDate}")
        print("-----------------------")
