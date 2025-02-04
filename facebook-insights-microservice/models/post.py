from pydantic import BaseModel, Field
from datetime import datetime

class PostModel(BaseModel):
    id: str = Field(..., alias="_id")
    page_id: str
    content: str
    likes: int
    comments: int
    timestamp: datetime

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "post123",
                "page_id": "123456789",
                "content": "This is an example post content.",
                "likes": 100,
                "comments": 20,
                "timestamp": "2023-01-01T12:00:00"
            }
        }

