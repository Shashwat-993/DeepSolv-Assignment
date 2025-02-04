from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from config import config, logger

app = FastAPI(title="Facebook Insights Microservice")

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(config.MONGO_URI)
    app.mongodb = app.mongodb_client[config.MONGO_DB_NAME]
    logger.info("Connected to MongoDB")

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
    logger.info("Disconnected from MongoDB")

@app.get("/")
async def root():
    return {"message": "Welcome to Facebook Insights Microservice"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

