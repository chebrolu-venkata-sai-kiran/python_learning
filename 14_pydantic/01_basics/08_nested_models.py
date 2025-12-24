from pydantic import BaseModel, Field 

class Office(BaseModel):
    name: str
    address: str
    location: str

class Employee(BaseModel):
    name: str
    age: int
    location :Office


Office =Office(name='Agentic AI', address='123 Main St', location="office_location")

employee = Employee(name='John Doe', age=30, location=Office)

print(employee)

