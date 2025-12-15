# dictionary comprehentions

# create a dictionary with keys as numbers and values as their squares

# squares = {num: num**2 for num in range(1, 11)}

# print(squares)


drinks = {
    "Coke": 150,
    "Pepsi": 120,
    "Sprite": 100
}

# create a new dictionary with keys as drinks and values as their prices in euros

euros = {drink: price * 0.85 for drink, price in drinks.items()}

print(euros)
