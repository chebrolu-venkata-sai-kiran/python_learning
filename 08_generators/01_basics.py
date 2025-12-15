# generators
#in generators function will pick the data where it exactly left the last time here we are accessing it 
# throught memory instead when ever we call next it will take data from the place where we left
# 
def serve_drink():
    yield "cup 1 served"
    yield "cup 2 served"
    yield "cup 3 served"


# creating a generator object
drink_generator = serve_drink()

# accessing the values one by one

print(next(drink_generator))
print(next(drink_generator))
print(next(drink_generator))

# second menthod

# for drink in serve_drink():
#     print(drink,end="  ")