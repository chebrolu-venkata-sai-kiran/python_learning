"""Inheritance is used where a class wants to derive the nature of parent 
class and then modify or extend the functionality of it. Inheritance will extend 
the functionality with extra features allows overriding of methods, but in the case of 
Composition, we can only use that class we can not modify or extend the functionality of it.
 It will not provide extra features. Thus, when one needs to use the class as it without any 
 modification, the composition is recommended and when one needs to change the behavior of the method 
 in another class, then inheritance is recommended."""


# class Engine:
#     def start(self):
#         return "Engine started!"

# class Car:
#     def __init__(self):
#         # Composition: The Car class creates and owns an Engine instance
#         self.engine = Engine()

#     def operate(self):
#         print(f"Car is running: {self.engine.start()}")

# # Usage
# my_car = Car()
# my_car.operate()
# # Output: Car is running: Engine started!


class BaseChai:
 
    def __init__(self, type_):
        self.type = type_


    def prepare(self) :
        print(f"Preparing {self.type} chai .... ")

 
class MasalaChai (BaseChai) :

    def add_spices (self):
        print("Adding cardamom, ginger, cloves.")

class Chaishop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Masala")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()
 

class FancyChaiShop(Chaishop):
    chai_cls = MasalaChai

shop = Chaishop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()
