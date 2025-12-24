from pydantic import BaseModel, Field 
from typing import Optional,List,Union

class Address(BaseModel):
    street: str
    city: str
    pincode: str

class Office(BaseModel):
    name: str
    address: Optional[Address] = None
    location: str

class Employee(BaseModel):
    name: str
    company :Optional[Office] = None

class TextContent(BaseModel):
    type: str = "text"
    content : str

class ImageContent(BaseModel): 
    type: str = "image"

    image_url: str
    caption: Optional[str] = None

class Article(BaseModel):
    title: str
    sections: List[Union[TextContent,ImageContent]]


# Create an instance of the Article model

article = Article(
    title="My First Article",
    sections=[
        TextContent(content="This is the first section"),
        ImageContent(image_url="https://example.com/image1.jpg", caption="Image 1"),])


print(article.json())