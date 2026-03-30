import select

from fastapi import FastAPI, HTTPException,File,UploadFile,Form,Depends
from app.schemas import PostCreate,PostResponse

from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
from app.images import imagekit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions 


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app= FastAPI(lifespan=lifespan)

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(...),
    session: AsyncSession = Depends(get_async_session)
    ):
    post = Post(
        caption=caption,
        url="dummy_url",
        file_type="photo",
        file_name="dummy name"
        
    )
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
    ):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all() ]

    posts_data=[]

    for post in posts:
        posts_data.append(
            {
                "id":str(post.id),
                "caption":post.caption,
                "url":post.url,
                "file_type":post.file_type,
                "file_name":post.file_name,
                "created_at":post.created_at.isoformat()
            }
        )
    return posts_data