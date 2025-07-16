numbers = [ 1, 2, 3, 4]
squared_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(squared_evens)