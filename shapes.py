import math

class Shape:
    def __init__(self):
        pass
    
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
        
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

# Prompting user for input
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

side1, side2, side3 = map(float, input("Enter the three sides of the triangle separated by space: ").split())
triangle = Triangle(side1, side2, side3)

side = float(input("Enter the side length of the square: "))
square = Square(side)

# Output
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())

print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())
