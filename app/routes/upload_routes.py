from fastapi import APIRouter, File, UploadFile, HTTPException
import shutil
import os
import uuid
from pathlib import Path

router = APIRouter()

UPLOAD_DIR = Path("app/static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Generate a unique filename to avoid collisions
        file_extension = file.filename.split(".")[-1]
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        file_path = UPLOAD_DIR / unique_filename
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Return the URL
        # Note: Ideally domain should be dynamic, but for now strict 127.0.0.1:8000
        url = f"http://127.0.0.1:8000/static/uploads/{unique_filename}"
        return {"url": url}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {e}")
