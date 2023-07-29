class Good:

    def __init__(self, name, price, quantity, productiondate, expirationdate):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.productionDate = productiondate
        self.expirationDate = expirationdate

    def showDetails(self):
        print(f"    {self.name} :")
        print(f"        price : {self.price}")
        print(f"        quantity : {self.quantity}")
        print(f"        productionDate : {self.productionDate}")
        print(f"        expirationDate : {self.expirationDate}")

