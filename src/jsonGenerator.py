import random

class JsonGenerator:
    def __init__(self):
        self.json = ""
        self.rand = random.Random()

    typeList = ["junkFood", "drink", "diary", "sanitary", "protein"]
    proteinGoodsList = ["beef", "chicken", "turkey", "sausage", "fish", "egg"]
    diaryGoodsList = ["milk", "cheese", "yogurt", "cream", "dough", "Curd"]
    drinkGoodsList = ["coke", "hype", "delester", "hotChocolate", "coffee", "tea"]
    sanitaryGoodsList = ["handWash", "shampoo", "tissue", "faceWash", "bodyWash", "washingPowder"]
    junkFoodGoodsList = ["chips", "pofak", "tokhme", "popCorn", "lavashak", "chocolate"]

    def generate_buy_recipe(self):
        self.generate_random_types()
        return self.json

    def generate_random_types(self):
        self.json += "{"
        types_index = self.generate_non_duplicate_random_numbers(5)
        for i in types_index:
            self.generate_random_goods(self.typeList[i])
        self.json += "}"

    def generate_random_goods(self, type):
        self.json += "\"" + type + "\":["
        if type == "junkFood":
            goods_list = self.junkFoodGoodsList
        elif type == "drink":
            goods_list = self.drinkGoodsList
        elif type == "diary":
            goods_list = self.diaryGoodsList
        elif type == "sanitary":
            goods_list = self.sanitaryGoodsList
        elif type == "protein":
            goods_list = self.proteinGoodsList
        else:
            return

        goods_index = self.generate_non_duplicate_random_numbers(6)
        for i in goods_index:
            self.generate_random_goods_details(goods_list[i], type)
        self.json += "],"

    def generate_random_goods_details(self, item, type):
        price = self.generate_random_price(type)
        p_date = self.generate_random_p_date()
        e_date = self.generate_random_e_date(p_date, type)
        self.json += "\"" + item + "\":{\"price\":\"" + str(price) + "\",\"quantity\":\"" + str(self.rand.randint(15, 164)) + "\",\"productionDate\":\"" + p_date + "\",\"expirationDate\":\"" + e_date + "\"},"

    def generate_random_price(self, type):
        if type == "junkFood":
            return str(self.rand.randint(20000, 75000))
        elif type == "drink":
            return str(self.rand.randint(25000, 65000))
        elif type == "diary":
            return str(self.rand.randint(50000, 200000))
        elif type == "sanitary":
            return str(self.rand.randint(60000, 260000))
        elif type == "protein":
            return str(self.rand.randint(100000, 400000))
        else:
            return "error"

    def generate_random_p_date(self):
        return "2023-" + str(self.rand.randint(1, 12)) + "-" + str(self.rand.randint(1, 28))

    def generate_random_e_date(self, p_date, type):
        split = p_date.split("-")
        year = int(split[0])
        month = int(split[1])
        day = int(split[2])

        if type == "junkFood":
            month += 6
            if month > 12:
                month -= 12
                year += 1
        elif type == "drink":
            month += 8
            if month > 12:
                month -= 12
                year += 1
        elif type == "diary":
            day += 15
            if day > 30:
                day -= 30
                month += 1
                if month > 12:
                    month -= 12
                    year += 1
        elif type == "sanitary":
            year += 2
        elif type == "protein":
            day += 2
            if day > 30:
                day -= 30
                month += 1
                if month > 12:
                    month -= 12
                    year += 1
        else:
            return "error"

        return str(year) + "-" + str(month) + "-" + str(day)

    def generate_non_duplicate_random_numbers(self, max_value):
        generated = []
        while len(generated) < self.rand.randint(1, max_value):
            next_num = self.rand.randint(0, max_value - 1)
            if next_num not in generated:
                generated.append(next_num)
        return generated
