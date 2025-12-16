class Drink:
    temperature = "cold"
    size = "medium"


# Creating objects

coke = Drink()
print("coke is", coke.temperature, "and size is", coke.size)
coke.temperature = "hot"
print("coke is now", coke.temperature)

del coke.temperature

print("coke's temperature attribute has been deleted and what will be current value",coke.temperature)

coke.color = "black"
print("coke's color is", coke.color)

del coke.color

print("coke's color attribute has been deleted",coke.color)

#here if we delete the object attribute which is not present, it will throw an AttributeError

# if we have class attributes and object attributes with same name, object attributes will be used

# if we have class attribute and we updated it object attribute will not affect the class attribute

# if we have class attribute and we updated it object attribute will not affect the class attribute 
# 
# and even if we delete the object attribute, class attribute will still exist 

# and fall back will happed to class attribute.


