from pydantic import BaseModel, Field 
from typing import Optional,List,Union

class Country(BaseModel):
    name: str
    code:str 

class State(BaseModel):
    name: str
    country:Country 

class City(BaseModel):
    name: str
    state:State 

class Address(BaseModel):
    street: str
    city: str
    pincode: str


class Office(BaseModel):
    name: str
    address: Optional[Address] = None
    branches: List[Address]=[]


