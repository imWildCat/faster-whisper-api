import os
import threading
import time
import uuid
from fastapi import FastAPI, File, Form
from faster_whisper import WhisperModel
import subprocess
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import logging

logging.basicConfig()
logging.getLogger("faster_whisper").setLevel(logging.DEBUG)

app = FastAPI()

security = HTTPBearer()


# Initialize the model variable
model = None
model_size = "large-v3"
last_request_time = time.time()

def load_model():
    global model
    if model is None:
        model = WhisperModel(model_size, device="cuda", compute_type="float16")

def offload_model():
    global model
    if model is not None:
        del model
        model = None

def check_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer" or credentials.credentials != os.getenv("API_KEY"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization code",
        )

def offload_check():
    global last_request_time
    while True:
        if time.time() - last_request_time > 5:
            offload_model()
        time.sleep(1)

# Start the offload check in a separate thread
threading.Thread(target=offload_check, daemon=True).start()

@app.post("/v1/audio/transcriptions")
async def create_transcription(
    file: bytes = File(...),
    language: str = Form(None),
    prompt: str = Form(None),
    response_format: str = Form('json'),
    temperature: float = Form(0),
    timestamp_granularities: list = Form(None),
    token: HTTPAuthorizationCredentials = Depends(check_token)
):
    global last_request_time
    last_request_time = time.time()

    load_model()
    
    random_uuid = uuid.uuid4()
    tmp_path = './tmp'

    # create dir if not exists
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)
        logging.info(f"Created tmp directory at {tmp_path}")

 
    file_name = f"{tmp_path}/audio_{random_uuid}.m4a"
    file_name_full = os.path.abspath(file_name)
    # use ffmpeg to convert the m4a to wav
    output_file_name = f"{tmp_path}/audio_{random_uuid}.wav"
    output_file_name_full = os.path.abspath(output_file_name)

    try:
        # Save the audio file locally
        with open(file_name_full, "wb") as audio:
            audio.write(file)
        
        subprocess.run(["ffmpeg", "-i", file_name_full, output_file_name_full])
        logging.info(f"File saved to {file_name}")

        # Transcribe the audio file
        segments, info = model.transcribe(output_file_name_full, beam_size=5, initial_prompt=prompt, temperature=temperature)

        combined_text = '\n'.join([segment.text for segment in segments])
        # Build the response
        response = {
            "text": combined_text,
        }

        return response
    except Exception as e:
        raise e
    finally:
        # Clean up the files
        os.remove(file_name_full)
        os.remove(output_file_name_full)
        logging.info(f"Removed {file_name_full} and {output_file_name_full}")
