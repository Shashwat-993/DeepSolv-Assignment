from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PageInfo(BaseModel):
    id: str
    name: str
    url: str
    profile_pic: str
    email: Optional[str]
    website: Optional[str]
    category: str
    followers: int
    likes: int
    creation_date: str

class Post(BaseModel):
    id: str
    page_id: str
    content: str
    likes: int
    comments: int
    timestamp: datetime

class Follower(BaseModel):
    id: str
    page_id: str
    name: str
    profile_pic: str

