# Create a list items = ["onigiri", "tea", "bento"]. Add 
# "pudding" to the end, remove "tea", then loop through and
# print each item with its index, e.g. "1. onigiri".


items= ["onigiri", "tea", "bento"]
items.append("pudding")
items.remove("tea")

for i in range(len(items)):
    print(f"{i + 1}. {items[i]}")
