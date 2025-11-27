my_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}

ascending = dict(sorted(my_dict.items()))

descending = dict(sorted(my_dict.items(), reverse=True))

print("Original dictionary:", my_dict)
print("Dictionary in ascending order:", ascending)
print("Dictionary in descending order:", descending)
