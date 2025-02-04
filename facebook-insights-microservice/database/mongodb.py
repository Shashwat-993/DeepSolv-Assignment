from motor.motor_asyncio import AsyncIOMotorDatabase
from models.page import PageModel
from models.post import PostModel
from models.follower import FollowerModel

class MongoDB:
    def __init__(self, database: AsyncIOMotorDatabase):
        self.database = database
        self.page_collection = database.pages
        self.post_collection = database.posts
        self.follower_collection = database.followers

    async def get_page(self, page_id: str) -> PageModel:
        page = await self.page_collection.find_one({"_id": page_id})
        if page:
            return PageModel(**page)
        return None

    async def create_page(self, page: PageModel):
        await self.page_collection.insert_one(page.dict(by_alias=True))

    async def get_posts(self, page_id: str, skip: int = 0, limit: int = 10) -> list[PostModel]:
        cursor = self.post_collection.find({"page_id": page_id}).skip(skip).limit(limit)
        posts = await cursor.to_list(length=limit)
        return [PostModel(**post) for post in posts]

    async def create_post(self, post: PostModel):
        await self.post_collection.insert_one(post.dict(by_alias=True))

    async def get_followers(self, page_id: str, skip: int = 0, limit: int = 10) -> list[FollowerModel]:
        cursor = self.follower_collection.find({"page_id": page_id}).skip(skip).limit(limit)
        followers = await cursor.to_list(length=limit)
        return [FollowerModel(**follower) for follower in followers]

    async def create_follower(self, follower: FollowerModel):
        await self.follower_collection.insert_one(follower.dict(by_alias=True))

