list1 = input("enter the colors in list 1:").split()
list2 = input("enter the colors in list 2:").split()

result = [color for color in list1 if color not in list2]


print("Colors in list1 not in list2:", result)
