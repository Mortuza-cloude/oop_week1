# Create a class Employee with a constructor __init__(self, name, hourly_wage) 
# that stores both as attributes. Create two objects, Yuki and Kenta, with different 
# names and wages,
#  and print each one's name and hourly_wage.


class Employee:

    def __init__(self, name, hourly_wage):
        self.name = name
        self.hourly_wage = hourly_wage

yuki = Employee("Yuki", 1200)
kenta = Employee("Kenta", 1300)

print(f"Name: {yuki.name}, Hourly Wage: {yuki.hourly_wage}  yen")
print(f"Name: {kenta.name}, Hourly Wage: {kenta.hourly_wage} yen")