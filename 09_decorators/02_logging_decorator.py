# in this one we are logging which function it is exectuing with wraps

from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed successfully")
        return result
    return wrapper

@log_execution
def add(a, b):
    print (a + b)

(add(2,3))