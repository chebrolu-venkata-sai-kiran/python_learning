# pure functions and impure functions

# Pure functions: They do not modify the state of the program or any external resources,
#  and always return the same output for the same input. They can be easily tested and debugged.

def add_numbers(a, b):
    return a + b

# Impure functions: They modify the state of the program or external resources,
#  and can have unpredictable behavior. They cannot be easily tested and debugged.
# in the impure functions it will modify the global values which can cause issue in the application

def modify_list(lst, index, value):
    lst[index] = value
    return lst

# Example of a pure function

numbers = [1, 2, 3, 4, 5]
sum_numbers = add_numbers(numbers[0], numbers[1])
print(f"Sum of the first two numbers: {sum_numbers}")

# Example of an impure function

numbers = [1, 2, 3, 4, 5]
modify_list(numbers, 2, 0)
print(f"Modified list: {numbers}")