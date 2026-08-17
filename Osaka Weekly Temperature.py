# Given a list temps = [28, 31, 27, 33, 30, 29, 32] 
# (one week of Osaka temperatures in °C), find and print the highest,
#   lowest, and average temperature.
# Hint: max(), min(), sum(), len()

temp_list = [28, 31, 27, 33, 30, 29, 32]

highest = max(temp_list)
lowest = min(temp_list)

average = sum(temp_list)/ len(temp_list)

print(f"Highest:, {highest}°C" )
print(f"Lowest:, {lowest}°C" )
print(f"Average:, {average}°C")