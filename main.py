from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import subprocess
import uuid
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Video Audio Extraction API Running"}

@app.post("/extract-audio/")
async def extract_audio(file: UploadFile = File(...)):

    unique_id = str(uuid.uuid4())
    video_path = f"{unique_id}.mp4"
    audio_path = f"{unique_id}.wav"

    try:
        with open(video_path, "wb") as f:
            f.write(await file.read())

        subprocess.run([
            "ffmpeg",
            "-i", video_path,
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            audio_path
        ], check=True)

        return FileResponse(audio_path, media_type="audio/wav", filename="output.wav")

    finally:
        if os.path.exists(video_path):
            os.remove(video_path)