num = int(input("Enter a 4-digit number: "))
first_two = num // 100
last_two = num % 100
result = first_two ** 2 + last_two ** 2
print("Sum of squares:", result)