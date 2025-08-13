n = int(input("Enter a number: "))
original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if original == rev:
    print(original, "is a palindrome.")
else:
    print(original, "is not a palindrome.")
