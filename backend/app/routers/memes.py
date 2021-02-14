from typing import Optional
from fastapi import APIRouter, HTTPException

from datetime import datetime

from models.memes import MemeSchema, UpdateMemeSchema, NewMemeSchema, MemesResponse
from models.base import ObjectId

from bson import objectid
from db.mongodb import db

router = APIRouter(prefix="/memes", tags=["memes"])

def response_helper(db_resp: dict) -> dict:
    return { **db_resp, "id": db_resp["_id"] }

@router.get("/", response_model=MemesResponse)
async def get_memes(limit: int = 100):
    memes: MemesResponse = []
    meme_docs = db.client["xmeme"]["meme"].find({}).sort("createdAt", -1).limit(limit)
    async for meme in meme_docs:
        memes.append(response_helper(meme))
    return memes

@router.get("/{meme_id}", response_model=MemeSchema)
async def get_meme_by_id(meme_id: ObjectId):
    meme_doc = await db.client["xmeme"]["meme"].find_one({ "_id": objectid.ObjectId(meme_id) })
    if not meme_doc: raise HTTPException(status_code=404, detail="Meme not found")
    return response_helper(meme_doc)

@router.post("/", response_model=MemeSchema)
async def post_meme(meme_data: NewMemeSchema):
    meme_doc = meme_data.dict()
    meme_doc["createdAt"] = datetime.utcnow()
    meme_doc["updatedAt"] = datetime.utcnow()
    await db.client["xmeme"]["meme"].insert_one(meme_doc)
    return response_helper(meme_doc)

@router.patch("/{meme_id}", response_model=MemeSchema)
async def update_meme(meme_id: ObjectId, meme_data: UpdateMemeSchema):
    update_data = meme_data.dict(exclude_none= True)
    update_data["updatedAt"] = datetime.utcnow()
    meme_doc = await db.client["xmeme"]["meme"].find_one_and_update({ "_id": objectid.ObjectId(meme_id) }, {
        "$set": update_data
    }, return_document = True)
    if not meme_doc: raise HTTPException(status_code=404, detail="Meme with id {} was not found".format(meme_id))
    return response_helper(meme_doc)