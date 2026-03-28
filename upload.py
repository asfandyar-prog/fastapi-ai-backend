from fastapi import APIRouter, UploadFile, File
from app.models.schemas import UploadResponse
import shutil, os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return UploadResponse(
        filename=file.filename,
        status="success",
        message=f"{file.filename} uploaded and ready for processing."
    )
