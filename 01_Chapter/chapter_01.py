a = 5

print(f"The value of a is: {id(a)}")

a =12

print(f"The new value of a is: {id(a)}")

# integers are immutable, so changing the value of a changes its memory location. 
# The id() function returns the memory location of the object.
