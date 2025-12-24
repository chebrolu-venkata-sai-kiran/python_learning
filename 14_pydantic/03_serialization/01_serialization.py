from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    pincode: str

class User(BaseModel):
    id : int
    name: str 
    email:str 
    is_active : str
    createdAt : datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v : v.strftime('%Y-%m-%d %H:%M:%S')}
    )

user = User(
    id=1,
    name='John Doe',
    email='john.doe@example.com',
    is_active='true',
    createdAt=datetime.now(),
    address=Address(street='123 Main St', city='New York', pincode='12345'),
    tags=['admin', 'user']
)

# print(user.json())

data = user.model_dump()
print(data)
print("-"*50)
data_json = user.model_dump_json()
print(data_json)