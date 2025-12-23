from typing import Optional
from pydantic import BaseModel ,Field
import re

class Item(BaseModel):
    id: int
    name: str =Field(
        ...,
        min_lenght = 10,
        max_length = 50,
        example = "coke",
        description = 'The name of the item'
        
    )
    department : Optional[str] = 'General'
    salary : int= Field(
        ...,
        ge = 10000,
        lt = 100000,
        example = 50000,
        description = 'The salary of the employee'
    )

class User(BaseModel):
    email : str = Field(
        ...,
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        example = 'john.doe@example.com',
        description = 'The email of the user'   
    )