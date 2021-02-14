from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import memes
from db.mongodb_utils import connect_mongodb, disconnect_mongodb

app = FastAPI(title="XMeme" ,docs_url="/swagger-ui", redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_mongodb)
app.add_event_handler("shutdown", disconnect_mongodb)

app.include_router(memes.router)