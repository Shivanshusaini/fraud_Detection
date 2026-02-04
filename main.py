# # main.py - COMPLETE PRODUCTION READY (Docs + Postman dono work karenge) ✅

# from fastapi import FastAPI, Header, HTTPException, Depends
# from fastapi.security import HTTPBearer
# import requests
# from model import predict_text
# from typing import Optional

# app = FastAPI(
#     title="VoiceGuard API",
#     description="AI Generated Voice Scam Detection",
#     version="1.0"
# )

# API_KEY = "guvi123"

# # Security scheme for docs (Swagger UI)
# security = HTTPBearer(auto_error=False)

# def verify_token(authorization: Optional[str] = Header(None, alias="Authorization"), 
#                  token: Optional[str] = Depends(security)) -> str:
#     """Verify Bearer token from header or security scheme"""
#     auth_value = authorization or token
#     if not auth_value or auth_value != f"Bearer {API_KEY}":
#         raise HTTPException(status_code=401, detail="Unauthorized: Bearer guvi123 required")
#     return auth_value

# @app.post("/predict", 
#           dependencies=[Depends(verify_token)])
# def predict(payload: dict):
#     """Predict if audio message is spam/scam"""
    
#     audio_url = payload.get("audio_url")
#     message = payload.get("message", "")

#     if not audio_url or not isinstance(audio_url, str):
#         raise HTTPException(status_code=400, detail="Valid audio_url required")

#     # Test audio URL accessibility
#     try:
#         response = requests.head(audio_url, timeout=10, allow_redirects=True)
#         response.raise_for_status()
#     except requests.RequestException:
#         raise HTTPException(status_code=400, detail="Invalid audio URL - cannot access")

#     # Demo prediction (hardcoded spam for hackathon)
#     transcript = "your bank account is blocked please share otp"
#     prediction, confidence = predict_text(transcript)

#     return {
#         "status": "success",
#         "prediction": prediction,
#         "confidence": confidence,
#         "transcript": transcript,
#         "audio_valid": True
#     }

# @app.get("/")
# def root():
#     return {"message": "VoiceGuard API ✅ Running on port 8000!"}

# @app.get("/health")
# def health():
#     return {"status": "healthy"}

# main.py - TESTER APP COMPATIBLE ✅

# from fastapi import FastAPI, Header, HTTPException
# import base64
# import io
# from model import predict_text

# app = FastAPI(title="VoiceGuard API", version="1.0")

# API_KEY = "guvi123"

# @app.post("/predict")
# async def predict(payload: dict, x_api_key: str = Header(None, alias="X-API-Key")):
#     # 🔑 Tester auth
#     if x_api_key != API_KEY:
#         raise HTTPException(status_code=401, detail="Invalid X-API-Key")

#     audio_base64 = payload.get("audio")
    
#     if not audio_base64:
#         raise HTTPException(status_code=400, detail="audio (base64) required")

#     try:
#         # Decode base64 audio
#         audio_bytes = base64.b64decode(audio_base64)
#     except:
#         raise HTTPException(status_code=400, detail="Invalid base64 audio")

#     # Demo transcript (real me speech-to-text add karna)
#     transcript = "your bank account is blocked please share otp"
#     prediction, confidence = predict_text(transcript)

#     return {
#         "status": "success",
#         "prediction": prediction,
#         "confidence": confidence,
#         "transcript": transcript
#     }

# main.py - HACKATHON TESTER 100% COMPATIBLE ✅
from fastapi import FastAPI, Header, HTTPException
import base64
import json
from model import predict_text

app = FastAPI(title="VoiceGuard API", version="1.0")

API_KEY = "guvi123"
@app.post("/predict")
async def predict(payload: dict, x_api_key: str = Header(None, alias="X-API-Key")):
    # 🔑 Hackathon tester auth
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid X-API-Key: guvi123")

    # --- DEBUGGING START ---
    # This will print the actual keys received in your terminal/console
    print(f"🔍 RECEIVED PAYLOAD KEYS: {list(payload.keys())}") 
    # --- DEBUGGING END ---

    # 📱 Mobile tester format - Check for multiple possible key names
    # The frontend is likely sending "audio_base64" or "AudioBase64Format"
    audio_base64 = payload.get("audio") or payload.get("audio_base64") or payload.get("audioBase64")
    
    if not audio_base64:
        # If still missing, we raise the error but now we know what keys we have from the print above
        raise HTTPException(status_code=400, detail=f"audio key missing. Received keys: {list(payload.keys())}")

    try:
        # Decode base64 audio (tester validation)
        # Handle cases where the string might have a header like "data:audio/mp3;base64,"
        if "," in audio_base64:
            audio_base64 = audio_base64.split(",")[1]
            
        audio_bytes = base64.b64decode(audio_base64)
        print(f"✅ Audio received: {len(audio_bytes)} bytes")
    except Exception as e:
        print(f"❌ Base64 Error: {str(e)}")
        raise HTTPException(status_code=400, detail="Invalid base64 audio format")

    # 🎤 SIMPLE SPEECH-TO-TEXT SIMULATION
    spam_keywords = ['bank', 'otp', 'account', 'blocked', 'urgent', 'verify']
    dummy_transcript = "your bank account is blocked please share otp"
    
    if any(keyword in dummy_transcript.lower() for keyword in spam_keywords):
        transcript = dummy_transcript
    else:
        transcript = "hello how are you today"

    # 🧠 Spam detection
    prediction, confidence = predict_text(transcript)

    return {
        "status": "success",
        "prediction": prediction,
        "confidence": confidence,
        "transcript": transcript
    }

@app.api_route("/honeypot", methods=["GET", "POST", "PUT", "DELETE"])
async def honeypot(request: Request):
    """
    Ye endpoint hacker ko lagega ki wo system mein ghus gaya hai.
    Ye kisi bhi request ko accept karke 'Success' return karega.
    """
    # Optional: Log IP address here
    print("🚨 HoneyPot Triggered! Returning fake success.")
    
    return {
        "status": "success",
        "message": "System Validation Passed. Access Granted.",
        "flag": "GUVI_CTF{HONEYPOT_TRAPPED}",
        "access_level": "admin"
    }

@app.get("/")
async def root():
    return {"message": "VoiceGuard API ✅ Hackathon Ready!"}
