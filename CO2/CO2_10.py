def factors(n):
    factor_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)
    return factor_list

num = int(input("Enter a number: "))

print(f"Factors of {num} are:", factors(num))
