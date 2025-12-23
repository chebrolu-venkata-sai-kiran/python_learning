from pydantic import BaseModel

class Drink(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True


# Create a Drink instance

drink_1 = Drink(id=1, name="Coke", price=1.50)
print(drink_1)


# Modify a Drink attribute  

drink_1.price = 1.60
print(drink_1)

drink_2 = Drink(id=2 , price=1.70, name="Pepsi",in_stock= False)

print(drink_2)

# if we miss any filed attribute, it will raise an error

drink_3 = Drink(id=24  )

