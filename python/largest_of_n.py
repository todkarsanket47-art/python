n = int(input("How many numbers? "))
count = 0
largest = None

while count < n:
    num = float(input(f"Enter number {count + 1}: "))
    if largest is None or num > largest:
        largest = num
    count += 1

print("The largest number is", largest)
