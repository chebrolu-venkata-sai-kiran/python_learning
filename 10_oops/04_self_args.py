# here we are using the self keyword to access the instance variables and the class variables.



class Drink:
    size = "Large"

    def describe(self):
        return f"This is a {self.size} cup of coke."
    
coke = Drink()
print(coke.describe())

print(Drink.describe(coke))
coke2 = Drink()
coke2.size = "Medium"
print(coke2.describe())
print(Drink.describe(coke2))
print(Drink.size)
