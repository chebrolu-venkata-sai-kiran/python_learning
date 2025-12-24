from pydantic import BaseModel, Field,field_validator,model_validator
from datetime import datetime 
class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def names_must_be_capital(cls, v):
        if not v.istitle():
            raise ValueError("Names must be capitalized")
        return v
    

class User(BaseModel):
    email : str

    @field_validator('email')
    def mormalize_email(cls, v):
        return v.lower().strip()
    

class Prodcut(BaseModel):
    price : str

    @field_validator('price',mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v
    

class DateRange(BaseModel):
    start_date : datetime
    end_date : datetime

    @model_validator(mode='after')
    def validate_dates(cls, values):
        if values.start_date > values.end_date:
            raise ValueError("Start date must be before end date")
        return values



