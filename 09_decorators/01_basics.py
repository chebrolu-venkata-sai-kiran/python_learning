# decorators are basically adding the functions more details the wrapper is the one we need to use 

# while using the decorators and we need to use the wraps to store the meta data of the original function

#basically just decorating some functions


# decorator function

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before executing the function")
        func( )
        print("After executing the function")

    return wrapper


@my_decorator
def greet():
    print( "a + b")


greet()
print(greet.__name__)