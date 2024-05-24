import math

class shape:
    
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class circle(shape):

    def __init__ (self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius * self.radius)
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class triangle(shape):

    def __init__ (self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3



    def calculate_area(self):

        s = (side1 + side2 + side3)/2
        a = ((s-side1)*(s-side2)*(s-side3))*s
        return a
    
    def calculate_perimeter(self):
        return side1 + side2 + side3

class square(shape):
    def __init__ (self,side):
        self.side = side
    
    def calculate_area(self):
        return self.side * self.side
    
    def calculate_perimeter(self):
        return 4 * self.side

keepAsking = True

while keepAsking:

    try:
        choice = int(input("circle--1\ntriangle--2\nsquare--3\nenter your choice:"))
        if(choice ==1 ):

            print("Circle:")

            radius = float(input("\tEnter radius: "))

            my_circle = circle(radius)

            print("\tArea: ",my_circle.calculate_area())
            print(f"\t Perimeter:{my_circle.calculate_perimeter()}")

            keepAsking = False

        elif(choice == 2 ):

            print("Triangle:")

            side1 = float(input("\tEnter side1: "))
            side2 = float(input("\tEnter side2: "))
            side3 = float(input("\tEnter side3: "))

            my_triangle = triangle(side1,side2,side3)

            print(f"\tArea:{my_triangle.calculate_area()}")
            print(f"\tPerimeter:{my_triangle.calculate_perimeter()}")

            keepAsking = False

        elif( choice == 3 ):

            print("Square:")
            
            side = float(input("\tEnter side: "))
            
            my_square = square(side)

            print(f"Area:{my_square.calculate_area()}")
            print(f"Perimeter:{my_square.calculate_perimeter()}")

            keepAsking = False
        else:
            print("You have choosen a wrong option......")

    except Exception as error:
        print("Please provide suitable values:\n",error)