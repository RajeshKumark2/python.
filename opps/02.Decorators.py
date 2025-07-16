def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Excuting {func.__name__}")
        return func(*args, **kwargs)
    return wrapper 
@log_execution
def calculate(a, b):
    return a + b 

