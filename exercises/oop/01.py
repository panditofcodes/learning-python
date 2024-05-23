import math
class circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * math.pow(self.radius,2)
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
radius = float(input("Enter radius:"))

circle1 = circle(radius)

print(circle1.calculate_area())

print(circle1.calculate_perimeter())