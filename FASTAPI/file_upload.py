
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import shutil

app = FastAPI()

# Step 1: Ensure uploads folder exists
upload_dir = Path("uploads")
upload_dir.mkdir(exist_ok=True)

# Step 2: Static file setup
app.mount("/files", StaticFiles(directory=str(upload_dir)), name="files")


# Step 3: Upload file API
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="File not selected"
        )

    filename = Path(file.filename).name
    file_path = upload_dir / filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "fileName": filename,
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }


# Step 4: Get file URL API
@app.get("/files/{filename}")
def get_file(filename: str):
    filename = Path(filename).name
    file_path = upload_dir / filename

    if not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return {
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }


# Step 5: Home API
@app.get("/")
def home():
    return {
        "message": "File upload API running"
    }
