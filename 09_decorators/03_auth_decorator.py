# in this function we are checking the user access and in decorator it is good to return for each steps in wrapper

from functools import wraps

def require_admin(func):

    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("access denied : admins only")
           # return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def display_admin_details(user_role):
    print(f"Welcome, {user_role}")

display_admin_details("user")

display_admin_details("admin")