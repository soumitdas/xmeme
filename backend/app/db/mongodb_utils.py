import logging

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGODB_URI
from db.mongodb import db

async def connect_mongodb():
    """Connect to the database on startup"""
    logging.debug("Connecting to database client")
    db.client = AsyncIOMotorClient(MONGODB_URI)

async def disconnect_mongodb():
    """Disconnect from the database"""
    logging.debug("Disconnecting from database")
    db.client.close()