triangle=lambda b,h: 0.5*b*h
rectangle=lambda l,w: l*w
square=lambda s: s*s

b=float(input("Enter base of triangle: "))
h=float(input("Enter height of triangle: "))
print("Area of triangle= ",triangle(b,h))
print()
l=float(input("Enter length of rectangle: "))
w=float(input("Enter width of rectangle: "))
print("Area of rectangle= ",rectangle(l,w))
print()
s=float(input("Enter side of square: "))
print("Area of square= ",square(s))
