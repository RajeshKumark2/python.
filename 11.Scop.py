x = 10  # Global

def test():
    global x
    x = 20  # Modify global
    y = 5    # Local
print(x)
