# documentation for functions and built-in functions

# we need to add the """""" while writing the functions so it can be easy to use the function and understand

# __ is called as dhunder so __doc__ is called as dhunder doc

# def drink():
#     '''This function returns a string stating the user can drink.'''
#     return 'You can drink'

# print(drink.__doc__)
# print(drink.__name__)

# help(print)


def cafe(coke = 0,pizza =0):
    """
    Docstring for cafe
    
    :param coke: Number of the coke order each (100rs)
    :param pizza: Number of the pizza order each(200rs)
    :return: Total bill amount and a message
    """
    total = (coke * 100) + (pizza * 200)
    return f'Total bill amount: {total}rs', f'You ordered {coke} coke(s) and {pizza} pizza(s). Thanks for visiting us!'


print(cafe(2, 3))
