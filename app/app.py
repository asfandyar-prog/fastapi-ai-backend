import tempfile
import os
import uuid
import shutil
from datetime import datetime
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from imagekitio import ImageKit  # ✅
from imagekitio.types import FileUploadParams
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(...),
    session: AsyncSession = Depends(get_async_session)
):
    temp_file_path = None
    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=os.path.splitext(file.filename)[1]
        ) as temp_file:
            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

        # ✅ NEW - correct for current imagekitio version
        upload_result = ImageKit.files.upload(
        file=open(temp_file_path, "rb"),
        file_name=file.filename,
        use_unique_file_name=True,
        tags=["backend-upload"],
    )

        post = Post(
            caption=caption,
            url=upload_result.url,
            file_type="video" if file.content_type.startswith("video") else "image",
            file_name=upload_result.name,
            created_at=datetime.utcnow()
        )
        session.add(post)
        await session.commit()
        await session.refresh(post)
        return post

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)  # ✅ delete temp file
        file.file.close()


@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    posts_data = []
    for post in posts:
        posts_data.append({
            "id": str(post.id),
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat()
        })
    return posts_data



# @app.delete("/posts/{post_id}")
# async def delete_post(post_id: str, session: AsyncSession = Depends(get_async_session)):
#     try:
#         post_uuid = uuid.UUID(post_id)
#         result = await session.execute(select(Post).where(Post.id == post_uuid))
#         post= result.scalar().first()

#         if not post:
#             raise HTTPException(status_code=404, detail="Post not found")   
        
#         await session.delete(post)
#         await session.commit()

#         return {"success":True,"message":"Post deleted successfully"    }
    
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid post ID format")