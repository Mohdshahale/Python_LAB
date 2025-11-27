number=list(map(int,input("enter the numbers:").split()))
over=[]
for num in number:
    if num> 100:
        over.append("over")
    else:
        over.append(num);
print("",over)
        
