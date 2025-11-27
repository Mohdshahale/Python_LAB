class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    
    def __lt__(self, other):
        return self.area() < other.area()

    
    def __gt__(self, other):
        return self.area() > other.area()


r1 = Rectangle(10, 5)     
r2 = Rectangle(7, 9)      

print("Area of r1:", r1.area())
print("Area of r2:", r2.area())

if r1 < r2:
    print("r1 has smaller area than r2")
else:
    print("r1 has larger or equal area than r2")
