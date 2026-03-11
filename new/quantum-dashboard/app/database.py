from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    client: AsyncIOMotorClient = None
    database = None

db = Database()

async def get_database():
    return db.database

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    db.database = db.client[os.getenv("DATABASE_NAME")]

async def close_mongo_connection():
    db.client.close()