dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1 | dict2
print("Merged dictionary:", merged_dict)

merged_dict2 = dict1.copy()
merged_dict2.update(dict2)
print("Merged dictionary (method 2):", merged_dict2)
