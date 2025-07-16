# 1. Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: 
# apple
# banana
# cherry

# 2. Using range()
for i in range(3):  # 0 to 2
    print(i)
# Output: 0 1 2

# 3. Iterating with index
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry

# 4. Dictionary iteration
person = {"name": "Alice", "age": 30, "job": "Engineer"}
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 30
# job: Engineer