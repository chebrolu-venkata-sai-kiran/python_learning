cup_size = input("please enter preffered cup size: ").lower()

if cup_size == "small":
    print(f"the preffered size is {cup_size} and price is 10$")
elif cup_size == "medium":
    print(f"the preffered size is {cup_size} and price is 15$")
elif cup_size == "large":
    print(f"the preffered size is {cup_size} and price is 20$")
else:
    print(f"invalid option please select correct size")