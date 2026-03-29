from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    image_url: str | None = None



class PostResponse(BaseModel):
    title: str
    content: str
    image_url: str | None = None