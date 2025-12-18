from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
import base64

MESSAGE = b"halo dari alice"

with open("punkhazard-keys/priv.pem", "rb") as f:
    priv = serialization.load_pem_private_key(f.read(), password=None)

sig = priv.sign(MESSAGE, ec.ECDSA(hashes.SHA256()))
print("message:", MESSAGE.decode())
print("signature_b64:", base64.b64encode(sig).decode())

