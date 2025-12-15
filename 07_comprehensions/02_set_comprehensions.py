# set comprehentions

drinks = ["tea","coffee","cola","lemon tea","juice","masala chai","coffee","cola","lemon tea","orange juice"]

unique_drinks ={drink for drink in drinks}

print(unique_drinks)

# set comprehensions case 2 

drinks_1 = {
    "hot drinks":["tea","coffee","badam milk"],
    "favorite drink":["tea","cola","coffee"],
    "least favorite drink":["badam milk","orange juice"]
}

unique_drinks_1 = {drink for drink_list in drinks_1.values() for drink in drink_list}
# here we took initailly drink_list in the drinks_1 and drink in the second drink list but we gave drink in the inital
# we need to give the what is the final out put we are expecting from the list 

print(unique_drinks_1)

