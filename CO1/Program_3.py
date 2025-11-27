number=list(map(int,input("enter the value:").split()))
value=[]
for num in number:
    num=num*num
    value.append(num)

print("the given list:",number)
print("the list of square:",value)
