def greet(name="Gest"):
    return f"Hello, {name}"
print(greet("Alice"))
print(greet())

def sum_all(*args):
    return sum(args)
print(sum_all(1,2, 3))  

def factorial(n): 
    return 1 if n <= 1 else n * factorial(n-1)
print(factorial(5))

square = lambda x: x**2 
print(square(4))  


def process_data(data, *, min_val=0, max_val=100):
    """Filter data within range (keyword-only args)"""
    return [x for x in data if min_val <= x <= max_val]

print(process_data([10, 50, 150], min_val=20, max_val=100)) 