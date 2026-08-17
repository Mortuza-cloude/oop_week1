# Write a function calculate_total(price) that returns the price including 10% 
# Japanese consumption tax, rounded to 2 decimal places. Call it with at 
# least 3 different prices and print the results.

def calculate_total(price):
    tex_rate = 0.10 
    total_price = price *(1+ tex_rate)
    return round(total_price, 2)
print(calculate_total(100))
print(calculate_total(200))
print(calculate_total(300))



