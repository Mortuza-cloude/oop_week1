# Create a class Rectangle with a constructor that takes width and height. 
# Add a method get_area(self) that prints the area (width * height). 
# Create two Rectangle objects with 
# different sizes and call the method on both.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        print(f"Area: {area}")

rect1 = Rectangle(2, 3)
rect1.get_area()
rect2 = Rectangle(4, 5)
rect2.get_area()
