from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
from typing import List, Optional
from schemas import PageInfo, Post, Follower

async def get_page(db: AsyncIOMotorDatabase, username: str) -> Optional[PageInfo]:
    page = await db.pages.find_one({"url": f"https://www.facebook.com/{username}"})
    if page:
        return PageInfo(**page)
    return None

async def get_pages(
    db: AsyncIOMotorDatabase,
    min_followers: Optional[int] = None,
    max_followers: Optional[int] = None,
    name: Optional[str] = None,
    category: Optional[str] = None
) -> List[PageInfo]:
    query = {}
    if min_followers is not None:
        query["followers"] = {"$gte": min_followers}
    if max_followers is not None:
        query["followers"] = query.get("followers", {}) | {"$lte": max_followers}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if category:
        query["category"] = category

    cursor = db.pages.find(query)
    pages = await cursor.to_list(length=None)
    return [PageInfo(**page) for page in pages]

async def get_followers(db: AsyncIOMotorDatabase, username: str, skip: int, limit: int) -> List[Follower]:
    page = await db.pages.find_one({"url": f"https://www.facebook.com/{username}"})
    if not page:
        return []
    
    followers = await db.followers.find({"page_id": page["_id"]}).skip(skip).limit(limit).to_list(length=None)
    return [Follower(**follower) for follower in followers]

async def get_posts(db: AsyncIOMotorDatabase, username: str, skip: int, limit: int) -> List[Post]:
    page = await db.pages.find_one({"url": f"https://www.facebook.com/{username}"})
    if not page:
        return []
    
    posts = await db.posts.find({"page_id": page["_id"]}).sort("timestamp", -1).skip(skip).limit(limit).to_list(length=None)
    return [Post(**post) for post in posts]

async def save_page_to_db(db: AsyncIOMotorDatabase, page_data: PageInfo):
    await db.pages.update_one(
        {"url": page_data.url},
        {"$set": page_data.dict()},
        upsert=True
    )

