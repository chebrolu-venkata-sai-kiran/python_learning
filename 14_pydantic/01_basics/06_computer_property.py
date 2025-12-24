from pydantic import BaseModel,computed_field,Field


class Product(BaseModel):
    price : float
    quantity : int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
  

# Example usage:

product = Product(price=10.5, quantity=3)
print(product.total_price)  # Output: 31.5

class Hotel(BaseModel):
    room_price : float
    nights : int = Field(...,ge=1)

    @computed_field
    @property
    def total_price(self) -> float:
        return self.room_price * self.nights
    

# Example usage:

hotel = Hotel(room_price=150, nights=2)
print(hotel.total_price)  # Output: 300
print(hotel.model_dump())