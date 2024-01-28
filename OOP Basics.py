#
class Item:

    pay_rate = 0.8
    all = []

    def __init__(self, nama: str, races = 0, podiums = 0):
        assert races >= 0, f'No. of races {races} below zero'
        assert podiums >= 0

        self.races = races
        self.podiums = podiums
        self.nama = nama

        Item.all.append(self)

    def calculate_championship(self, a, b):
        return a * b

    def calculate_podium_percentage(self):
        return ((self.podiums / self.races)*100)

    def apply_discount(self):
        self.podiums = self.podiums * self.pay_rate
        return self.podiums

    def __repr__(self):
        return f'Item({self.nama}, {self.races}, {self.podiums})'

item1 = Item('Stafen', 150, 50)
item2 = Item('Hammer', 300, 100)
item3 = Item('Vets', 300, 50)
item4 = Item('Shaal', 150, 20)
item5 = Item('Lonso', 350, 40)

for i in Item.all:
    print(i.nama)
print(Item.all)

# item1 = Item('Hammertime', 300, 103)
#
# item1.name = 'Pajn'
# item1.price = 44
# item1.quantity = 7
# print(item1.calculate_championship(item1.price, item1.quantity))
# print(item1.calculate_podium_percentage())
# print(item1.nam)
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(Item.__dict__)
# print(item1.__dict__)
# print(item1.apply_discount())
# print(item1.podium)

# print(type(item1))
# print(type(item1.quantity))

# item2 = Item('verr')
#
# item2.name = 'Stappen'
# item2.price = 1
# item2.quantity = 3
#
# item2.podium = 69
#
# item2.pay_rate = 0.6
#
# print(item2.apply_discount())