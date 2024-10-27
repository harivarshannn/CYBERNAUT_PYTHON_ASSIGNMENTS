class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(5, 3)
print(f"Area: {rectangle1.calculate_area()}")
print(f"Perimeter: {rectangle1.calculate_perimeter()}")
