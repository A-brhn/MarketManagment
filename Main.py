import re
from datetime import date

from jsonGenerator import JsonGenerator
from Good import Good
from Type import Type
from Menu import *

class Main:

    json = JsonGenerator()
    bill = json.generate_buy_recipe()
    types = []

    @staticmethod
    def maketypes(bill, types):

        typesContentRegex = '"\w+":\[[\w":\{\}\-\,]+'

        typesContent = re.findall(typesContentRegex, bill)

        typeNameRegex = '"(\w+)":\['
        goodsContentRegex = '"\w+":\{[\w":\-\,]+\}'
        goodNameRegex = '"(\w+)":\{'
        goodPriceRegex = '"price":"(\d+)"'
        goodQuantityRegex = '"quantity":"(\d+)"'
        goodPDateRegex = '"productionDate":"(\d+)\-(\d+)\-(\d+)"'
        goodEDateRegex = '"expirationDate":"(\d+)\-(\d+)\-(\d+)"'

        for typeContent in typesContent:
            typeName = re.search(typeNameRegex,typeContent).group(1)
            goodsList = []
            goodsContent = re.findall(goodsContentRegex,typeContent)
            for goodContent in goodsContent:
                goodName = re.search(goodNameRegex,goodContent).group(1)
                goodPrice = int(re.search(goodPriceRegex,goodContent).group(1))
                goodQuantity = int(re.search(goodQuantityRegex,goodContent).group(1))
                fullDate = re.search(goodPDateRegex,goodContent)
                goodPDate = date(int(fullDate.group(1)),int(fullDate.group(2)),int(fullDate.group(3)))
                fullDate = re.search(goodEDateRegex,goodContent)
                goodEDate = date(int(fullDate.group(1)),int(fullDate.group(2)),int(fullDate.group(3)))
                goodsList.append(Good(goodName,goodPrice,goodQuantity,goodPDate,goodEDate))
            types.append(Type(typeName,goodsList))

    print(bill)
    maketypes(bill, types)
    start(types)
