import json
from aioredis import Redis

async def get_cached_data(redis: Redis, key: str):
    data = await redis.get(key)
    if data:
        return json.loads(data)
    return None

async def set_cached_data(redis: Redis, key: str, data: dict, expire: int = 300):
    await redis.set(key, json.dumps(data), expire=expire)

