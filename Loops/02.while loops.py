# 1. Basic counter
count = 0
while count < 3:
    print(count)
    count += 1
# Output: 0 1 2

# 2. User input validation
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# 3. Infinite loop with break
while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == "exit":
        break