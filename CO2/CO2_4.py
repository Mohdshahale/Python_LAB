import math
def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

even_digit_squares = []

for n in range(1000, 10000):
    digits = str(n)
    
    if all(int(d) % 2 == 0 for d in digits):
        if is_perfect_square(n):
            even_digit_squares.append(n)

print("Four-digit perfect squares with all even digits:")
print(even_digit_squares)
