import re
from datetime import date

from Good import Good
from Type import Type
from Menu import *

class Main:

    bill = """{"protein":["turkey":{"price":"210146","quantity":"136","productionDate":"2022-2-19","expirationDate":"2022-2-21"},"beef":{"price":"207474","quantity":"22","productionDate":"2022-2-4","expirationDate":"2022-2-6"},"sausage":{"price":"365589","quantity":"75","productionDate":"2022-12-11","expirationDate":"2022-12-13"},"fish":{"price":"225766","quantity":"34","productionDate":"2022-8-7","expirationDate":"2022-8-9"},"chicken":{"price":"291321","quantity":"46","productionDate":"2022-2-13","expirationDate":"2022-2-15"},],"junkFood":["tokhme":{"price":"22828","quantity":"157","productionDate":"2022-3-15","expirationDate":"2022-9-15"},"chocolate":{"price":"43491","quantity":"78","productionDate":"2022-2-8","expirationDate":"2022-8-8"},"pofak":{"price":"69819","quantity":"121","productionDate":"2022-3-20","expirationDate":"2022-9-20"},],"diary":["milk":{"price":"175886","quantity":"115","productionDate":"2022-12-5","expirationDate":"2022-12-20"},"yogurt":{"price":"75896","quantity":"92","productionDate":"2022-8-2","expirationDate":"2022-8-17"},"cheese":{"price":"156740","quantity":"122","productionDate":"2022-10-3","expirationDate":"2022-10-18"},],}"""
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
                goodPrice = re.search(goodPriceRegex,goodContent).group(1)
                goodQuantity = re.search(goodQuantityRegex,goodContent).group(1)
                fullDate = re.search(goodPDateRegex,goodContent)
                goodPDate = date(int(fullDate.group(1)),int(fullDate.group(2)),int(fullDate.group(3)))
                fullDate = re.search(goodEDateRegex,goodContent)
                goodEDate = date(int(fullDate.group(1)),int(fullDate.group(2)),int(fullDate.group(3)))
                goodsList.append(Good(goodName,goodPrice,goodQuantity,goodPDate,goodEDate))
            types.append(Type(typeName,goodsList))

    maketypes(bill, types)
    start(types)
