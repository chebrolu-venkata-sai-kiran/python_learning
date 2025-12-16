class drink:
    origin = "india"

# print(drink.origin)

drink.is_cold = True

# print(drink.is_cold)


#creating the object

coke = drink()

print("coke is from",coke.origin)

print("is coke cool",coke.is_cold)

coke.is_cold = False

print("class ",drink.is_cold)
print("object ",coke.is_cold)

coke.flavour = "zero sugar"

print(coke.flavour)