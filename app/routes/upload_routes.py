from fastapi import APIRouter, File, UploadFile, HTTPException
import shutil
import os
import uuid
from pathlib import Path

router = APIRouter()

UPLOAD_DIR = Path("app/static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="File type not allowed. Only images are permitted.")
    
    try:
        # Generate a unique filename to avoid collisions
        file_extension = file.filename.split(".")[-1]
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        file_path = UPLOAD_DIR / unique_filename
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Return relative path for better deployment compatibility
        url = f"/static/uploads/{unique_filename}"
        return {"url": url}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {e}")
@router.post("/multiple")
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    urls = []
    try:
        for file in files:
            # Add security check for multiple uploads too!
            if not allowed_file(file.filename):
                raise HTTPException(status_code=400, detail=f"File {file.filename} type not allowed. Only images are permitted.")

            file_extension = file.filename.split(".")[-1]
            unique_filename = f"{uuid.uuid4()}.{file_extension}"
            file_path = UPLOAD_DIR / unique_filename
            
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            # Using relative path for flexibility
            url = f"/static/uploads/{unique_filename}"
            urls.append(url)
            
        return {"urls": urls}
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save files: {e}")
