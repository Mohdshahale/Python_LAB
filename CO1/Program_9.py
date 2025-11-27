list_a=list(map(int,input("enter the first list:").split()))
list_b=list(map(int,input("enter the first list:").split()))

if len(list_a)== len(list_b):
    print("both lists are in the same length")
else:
    print("both lists are not the same length")

if sum(list_a)== sum(list_b):
    print("the sum of both lists are same")
else:
    print("the sum is not same")
    
common_value= set(list_a) & set(list_b)
if common_value:
    print("yes, there are same values")
else:
    print("no, there are not same values")

print("",common_value)    
print("",list_a)
print("",list_b)


