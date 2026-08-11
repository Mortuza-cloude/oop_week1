# Create a dictionary vending = {"cola": 150, "water": 120, "coffee": 130}. 
# Ask for (or hardcode) an item name and print its price. 
# If the item doesn't exist, print "Item not available".
#

vending = dict(cola=150, water=120, coffee=130)

item_name = input("Enter the item name: ")

if item_name in vending:
    print(f"The price of {item_name} is {vending[item_name]} yen.")
else:
    print("Item not available.")
