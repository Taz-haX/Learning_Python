#
class Item:
    def calculate_championship(self, a, b):
        return a * b


item1 = Item()

item1.name = 'Pajn'
item1.price = 44
item1.quantity = 7
print(item1.calculate_championship(item1.price, item1.quantity))

# print(type(item1))
# print(type(item1.quantity))

item2 = Item()

item2.name = 'Stappen'
item2.price = 1
item2.quantity = 3