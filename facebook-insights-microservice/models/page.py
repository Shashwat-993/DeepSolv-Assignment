from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PageModel(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    url: str
    profile_pic: str
    email: Optional[str]
    website: Optional[str]
    category: str
    followers: int
    likes: int
    creation_date: datetime

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "123456789",
                "name": "Example Page",
                "url": "https://www.facebook.com/examplepage",
                "profile_pic": "https://example.com/profile.jpg",
                "email": "contact@example.com",
                "website": "https://www.example.com",
                "category": "Technology",
                "followers": 10000,
                "likes": 9500,
                "creation_date": "2020-01-01T00:00:00"
            }
        }

