class drink:
    pass

class food:
    pass

print(type(drink))

coke = drink()

print(type(coke))# here it is giving output as the i am class not standalone class a object instance of the drink

print(type(coke) is drink)

print(type(coke) is food)