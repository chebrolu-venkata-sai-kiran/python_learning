#list comprehenstions

drink = ["tea","coffee","cola","lemon tea","juice"]

# using list comprehension to create a new list with names containing 'ea'

filtered_drink = [drink_name for drink_name in drink if 'ea' in drink_name]

print(filtered_drink)

# using list comprehension we can check the len of the drink also if it is more than 4

filtered_drink_len = [drink_name for drink_name in drink if len(drink_name) > 4]

print(filtered_drink_len)