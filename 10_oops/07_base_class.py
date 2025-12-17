# accessing of the base class (parent class) can be done by the three different types of the methods 
#1.code duplication
#2.Explicit call
#3.Super()

class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#1.code duplication
class ColdDrink(Drink):
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
        print("This is a cold drink")
#2.Explicit call
#when you are calling explicitly we need to keep the self argument in the method
class ColdDrink2(Drink):
    def __init__(self, name, price,size):
        Drink.__init__(self,name, price)
        self.size = size


#3.Super()
class ColdDrink3(Drink):
    def __init__(self, name, price,size):
        super().__init__(name, price)
        self.size = size

# these are the three ways to call the base class 


cold_drink1 = ColdDrink("Coke", 10, "Small")
cold_drink2 = ColdDrink2("Pepsi", 15, "Medium")
cold_drink3 = ColdDrink3("Sprite", 20, "Large")

