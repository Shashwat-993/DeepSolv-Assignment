from pydantic import BaseModel, Field

class FollowerModel(BaseModel):
    id: str = Field(..., alias="_id")
    page_id: str
    name: str
    profile_pic: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "follower123",
                "page_id": "123456789",
                "name": "John Doe",
                "profile_pic": "https://example.com/johndoe.jpg"
            }
        }

