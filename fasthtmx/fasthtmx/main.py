from loguru import logger
from fastapi import FastAPI, Depends
# from fasthtmx.db import init_db, get_session,
from fasthtmx.db import  init_db_async, get_session_async
from fasthtmx.schema.song import *
from sqlmodel import select, Session
app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#     await init_db_async()
#     logger.info("db initialized")

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/songs")
async def get_songs(session:Session = Depends(get_session_async)):
    result = await session.execute(select(Song))
    # songs = result.scalars().all()
    songs = result.fetchall()
    for song in songs:
        logger.info(f"song : {type(song)}")
    return songs
    
    

@app.post("/songs")
async def add_song(song: SongCreate, session:Session = Depends(get_session_async)):
    song = Song(**song.dict())
    await session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
