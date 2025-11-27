
number=[10,25,-20,30,15,-15,-45,96,52]
positive_numbers=[]
negative_numbers=[]

for num in number:
    if num > 0:
        positive_numbers.append(num)
    else:
       negative_numbers.append(num)

print("positive numbers:",positive_numbers)
print("negative numbers:",negative_numbers)

