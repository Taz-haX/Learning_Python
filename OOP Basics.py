#
class Item:

    pay_rate = 0.8

    def __init__(self, nama: str, races = 0, podiums = 0):
        assert races >= 0, f'No. of races {races} below zero'
        assert podiums >= 0

        self.race = races
        self.podium = podiums
        self.nam = nama


    def calculate_championship(self, a, b):
        return a * b

    def calculate_podium_percentage(self):
        return ((self.podium / self.race)*100)

    def apply_discount(self):
        self.podium = self.podium * Item.pay_rate
        return self.podium



item1 = Item('Hammertime', 300, 103)

item1.name = 'Pajn'
item1.price = 44
item1.quantity = 7
print(item1.calculate_championship(item1.price, item1.quantity))
print(item1.calculate_podium_percentage())
print(item1.nam)
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(Item.__dict__)
# print(item1.__dict__)
print(item1.apply_discount())
print(item1.podium)

# print(type(item1))
# print(type(item1.quantity))

item2 = Item('verr')

item2.name = 'Stappen'
item2.price = 1
item2.quantity = 3