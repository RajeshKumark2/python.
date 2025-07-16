# Basic if-elif-else
temperature = 30

if temperature > 40:
    print("Hot")
elif 20 <= temperature <= 40:
    print("Moderate")
else:
    print("Cold")

# Ternary operator

# Interview Question: FizzBuzz
for i in range(1, 16):
    output = ""
    if i % 3 == 0: output += "Fizz"
    if i % 5 == 0: output += "Buzz"
    print(output or i)  # Output: 1, 2, Fizz, 4, Buzz...