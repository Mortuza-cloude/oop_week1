# Write an if-elif-else chain that takes an age variable and prints the fare category: "Child"
# if age < 12, "Student" if 12–22, "Adult" if 23–64, and "Senior" if 65 or above.
#


age=int(input("Enter your age: "))
if age < 12:
    print("Child")
elif age <= 22:
    print("Student")
elif age <= 64:
    print("Adult")
else:
    print("Senior")     


