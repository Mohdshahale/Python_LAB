class rectangle:
    def area(length,bredth):
        area=length*bredth
        return area
    def peri(l,b):
        perimeter=2*(l+b)
        return perimeter
print("enter the length and breadth of the first rectangle")
length1= int(input("enter the length:"))
bredth1= int(input("enter the bradth:"))

print("enter the length and breadth of the second rectangle")
length2= int(input("enter the length:"))
bredth2= int(input("enter the bradth:"))

value1=rectangle.area(length1,bredth1)
value2=rectangle.area(length2,bredth2)

peri1=rectangle.peri(length1,bredth1)
peri2=rectangle.peri(length2,bredth2)

if value1>value2:
    print("the first rectange has highest area:",value1)
    print("perimeter:",peri1)
else:
    print("the second rectange has highest area:",value2)
    print("perimeter:",peri2)




        
