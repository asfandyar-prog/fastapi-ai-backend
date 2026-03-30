from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate,PostResponse

from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app= FastAPI(lifespan=lifespan)

text_posts={1:{"title": "First Post", "content": "This is the content of the first post."}}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit :
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)



@app.post("/posts")
def create_post(post:PostCreate)->PostResponse:
    new_post={"title":post.title,"content":post.content}
    text_posts[max(text_posts.keys())+1]=new_post
    return new_post

  
