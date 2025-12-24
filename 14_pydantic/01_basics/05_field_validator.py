from pydantic import BaseModel,field_validator ,model_validator

class User(BaseModel):
    username: str 

    @field_validator('username')
    def validate_username(cls, v):
        if len(v) < 5:
            raise ValueError("Username must be at least 5 characters long")
        return v
    

class SignUpData(BaseModel):
    password : str
    confirm_password: str

    @model_validator(mode='after')
    def validate_passwords(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values