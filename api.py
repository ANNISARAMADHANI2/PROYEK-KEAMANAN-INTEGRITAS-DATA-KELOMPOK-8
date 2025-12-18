from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Optional
import json, os, secrets, base64

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidSignature

app = FastAPI(title="Security Service", version="1.0.0")
bearer_scheme = HTTPBearer()
# ================= CORS =================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

USERS_FILE = "users.json"
SESSIONS_FILE = "sessions.json"

# ================= HELPER =================
def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# ================= AUTH (A) =================
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    sessions = load_json(SESSIONS_FILE)

    if token not in sessions:
        raise HTTPException(401, "Invalid token")

    return sessions[token]

# ================= BASIC =================
@app.get("/health")
def health():
    return {
        "status": "ok",
        "time": datetime.now().isoformat()
    }

# ================= REGISTER (B-) =================
@app.post("/register")
def register(username: str, public_key: str):
    users = load_json(USERS_FILE)

    if username in users:
        raise HTTPException(400, "User exists")

    users[username] = public_key
    save_json(USERS_FILE, users)

    return {"message": "registered"}

# ================= LOGIN (A) =================
@app.post("/login")
def login(username: str):
    users = load_json(USERS_FILE)
    if username not in users:
        raise HTTPException(404, "User not found")

    token = secrets.token_urlsafe(32)
    sessions = load_json(SESSIONS_FILE)
    sessions[token] = username
    save_json(SESSIONS_FILE, sessions)

    return {"access_token": token}

# ================= VERIFY SIGNATURE (B-) =================
@app.post("/verify")
def verify(username: str, message: str, signature_b64: str):
    users = load_json(USERS_FILE)

    if username not in users:
        raise HTTPException(404, "User not found")

    pub_key = serialization.load_pem_public_key(
        users[username].encode()
    )

    try:
        signature = base64.b64decode(signature_b64)
        pub_key.verify(
            signature,
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return {"valid": True}
    except InvalidSignature:
        return {"valid": False}

# ================= ENCRYPT (B+) =================
@app.post("/encrypt")
def encrypt(message: str, user=Depends(get_current_user)):
    key = Fernet.generate_key()
    f = Fernet(key)
    cipher = f.encrypt(message.encode())
    return {"ciphertext": cipher, "key": key}

# ================= DECRYPT (B+) =================
@app.post("/decrypt")
def decrypt(ciphertext: str, key: str, user=Depends(get_current_user)):
    f = Fernet(key.encode())
    plain = f.decrypt(ciphertext.encode())
    return {"message": plain.decode()}

