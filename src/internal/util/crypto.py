import base64
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def generate_key() -> str:
    """Generate a 256-bit AES key and return its Base64-encoded string."""
    key = AESGCM.generate_key(bit_length=256)
    return base64.b64encode(key).decode('utf-8')

def encrypt(key_b64: str, plaintext: str) -> str:
    """
    Encrypt the plaintext using AES-GCM with a Base64-encoded key.
    Returns a single Base64-encoded string containing nonce + ciphertext.
    """
    key = base64.b64decode(key_b64)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # 96-bit nonce
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode('utf-8'), None)
    combined = nonce + ciphertext  # Concatenate nonce and ciphertext
    return base64.b64encode(combined).decode('utf-8')

def decrypt(key_b64: str, combined_b64: str) -> str:
    """
    Decrypt the Base64-encoded combined string (nonce + ciphertext) using AES-GCM.
    Returns the plaintext.
    """
    key = base64.b64decode(key_b64)
    combined = base64.b64decode(combined_b64)
    nonce = combined[:12]  # Extract the 96-bit nonce
    ciphertext = combined[12:]  # Extract the remaining ciphertext
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext.decode('utf-8')