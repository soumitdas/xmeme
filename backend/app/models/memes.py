from typing import Optional, List

from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl, Schema, constr
from models.base import Base, ObjectId

class MemeSchema(Base):
    # _id: ObjectId = Field(None)
    id: Optional[ObjectId] = Field(None)
    name: constr(min_length=1, max_length=30)
    url: HttpUrl
    caption: constr(min_length=1, max_length=300)
    created_at: Optional[datetime] = Schema(..., alias="createdAt")
    updated_at: Optional[datetime] = Schema(..., alias="updatedAt")

class UpdateMemeSchema(Base):
    url: Optional[HttpUrl]
    caption: Optional[constr(min_length=1, max_length=300)]

class NewMemeSchema(Base):
    name: constr(min_length=1, max_length=30)
    url: HttpUrl
    caption: constr(min_length=1, max_length=300)

class MemesResponse(Base):
    __root__: List[MemeSchema]
