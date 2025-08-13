import math

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter number of terms: "))

cos_x = 0
sign = 1

for i in range(n):
    term = sign * (x ** (2 * i)) / math.factorial(2 * i)
    cos_x += term
    sign *= -1

print(f"Cosine of {x} calculated using series is: {cos_x}")
