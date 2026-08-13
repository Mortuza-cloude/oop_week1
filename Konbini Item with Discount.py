# Create a class Item with constructor __init__(self, name, price). 
# Add a method apply_discount(self, percent) that prints the discounted price, 
# e.g. "Onigiri after 20% discount: 96 yen". Create 2 items and test the 
# method with different discount percentages.

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def apply_discount(self, percent):
        discounted_price = self.price * (1 - percent/100)
        print(f"{self.name} after {percent}% discount: {discounted_price:} yen")     
    
item1 = Item("Onigiri", 50)
item2 = Item("Coffee", 60)

item1.apply_discount(20)
item2.apply_discount(10)