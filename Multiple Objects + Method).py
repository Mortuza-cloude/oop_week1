# Create a class Employee with constructor __init__(self,
#  name, hours_worked_list) where hours_worked_list is a 
#  list of daily hours, e.g. [8, 7, 9, 8, 6].
#  Add a method get_total_hours(self) that prints the 
#  employee's name and total hours worked using an f-string. Create 4 employee 
#  (similar style to the Student example) 
#  and call the method on each.


class Employee:
    def __init__(self,name, hours_worked_list):
        self.name = name
        self.hours_worked_list = hours_worked_list  
    
    def get_total_hours(self):
        total_hours = sum(self.hours_worked_list)
        print(f"{self.name}: {total_hours} hours") 
employee1 = Employee("Rasel", [8, 7, 9, 8, 6])
employee2 = Employee("Moon", [7, 8, 8, 7, 9])
employee3 = Employee("Tarek", [6, 7, 8, 9, 8])
employee4 = Employee("Mizan", [8, 8, 7, 6, 9])

employee1.get_total_hours()
employee2.get_total_hours()
employee3.get_total_hours()
employee4.get_total_hours()