def process_data(data): 
    return sum(x**2 for x in data if x % 2 == 0)
print(process_data([1, 2, 3, 4, 5, 6]))