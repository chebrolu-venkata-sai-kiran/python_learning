from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__,"is running")
        res = func(*args, **kwargs)
        print(func.__name__,'is completed')
        return res

    return wrapper
    
@log
def ad(a,b):
    print(a+b)

ad(1,2)