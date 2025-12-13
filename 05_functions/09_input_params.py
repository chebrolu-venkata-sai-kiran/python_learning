# drink_type = "cold"

# def prepare(name):
#     print(f"Preparing {drink_type} coffee")

# prepare(drink_type)

# print(drink_type)

# nums = [1,2,3]

# def edit_nums(nums):
#     nums[0] = 100

# edit_nums(nums)

# print(nums)

# postional and key word argumetes

# def drink_type(flavour,size,quantity):
#     print(f"Making {flavour} coffee, size: {size}, quantity: {quantity}")

# drink_type("espresso", "medium", 2) # postional arguments

# drink_type(size="large",quantity=5,flavour="matcha") #keyword arguments

# #opt

# Making espresso coffee, size: medium, quantity: 2
# Making matcha coffee, size: large, quantity: 5

# *args ,**kwargs

# def drink(*args,**kwargs):
#     print("args", args)
#     print("kwargs",kwargs)

# drink("cold","large",flavour = "lemon",drink = "chass")

# args ('cold', 'large')
# kwargs {'flavour': 'lemon', 'drink': 'chass'}


# def order(value=[]):
#     value.append("coffee")
#     print(value)

# order()
# order()

# ['coffee']
# ['coffee', 'coffee']

def order(value = None):
    if value is None:
        value = []
    value.append("coffee")
    print(value)

order()
order( )