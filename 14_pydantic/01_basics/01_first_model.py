print("this is the start of the pydantic script")

# Create a new directory called 'pydantic_models'

from pydantic import BaseModel

class Drink(BaseModel):
    name: str
    type: str
    origin: str

input_data = {'name': 'coke', 'type': 'cold', 'origin': 'india'}

# Create a new instance of the Drink class from the input data

drink = Drink(**input_data)

# Print the information about the drink
# print(**input_data)
print(drink)

print("this is the end of the pydantic script")