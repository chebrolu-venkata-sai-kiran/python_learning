# here we are defining a class named drink with three attributes name, type, and origin.

# __init__ is a special method in Python classes that is called when an object is created from the class.

# here we are initializing the attributes of the class with the given values.

# get_info is another method in the class. It returns a string with the name, type, and origin of the drink.



class drink:

    def __init__(self, name, type_, origin):
        self.name = name
        self.type = type_
        self.origin = origin

    def get_info(self):
        return f"{self.name} is a {self.type} drink from {self.origin}"


# creating an object of the class drink with name "Coke", type "cold", and origin "India".

coke = drink("Coke", "cold", "India")

# calling the get_info method on the object coke to get the information about the drink.

print(coke.get_info())