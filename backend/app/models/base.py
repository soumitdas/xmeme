from datetime import datetime, timezone
from fastapi import HTTPException
from bson import objectid
from pydantic import BaseConfig, BaseModel, validator
import re

class ObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not objectid.ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

class Base(BaseModel):
    @validator("url", check_fields=False, pre=True)
    def format_url(cls, url):
        if not re.match("(?:http|ftp|https)://", url):
            return "http://{}".format(url)
        return url

    class Config(BaseConfig):
        allow_population_by_alias = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z"),
            ObjectId: str
        }