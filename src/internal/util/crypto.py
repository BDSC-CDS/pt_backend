import base64
import os
import gzip
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def generate_key() -> str:
    """Generate a 256-bit AES key and return its Base64-encoded string."""
    return base64.b64encode(AESGCM.generate_key(bit_length=256)).decode('utf-8')

def encrypt(key_b64: str, plaintext: str) -> str:
    """
    Compress and encrypt the plaintext using AES-GCM with a Base64-encoded key.
    Returns a single Base64-encoded string containing nonce + ciphertext.
    """
    key = base64.b64decode(key_b64)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    compressed = gzip.compress(plaintext.encode('utf-8'))
    ciphertext = aesgcm.encrypt(nonce, compressed, None)
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def decrypt(key_b64: str, combined_b64: str) -> str:
    """
    Decrypt and decompress the Base64-encoded combined string (nonce + ciphertext) using AES-GCM.
    Returns the plaintext.
    """
    key = base64.b64decode(key_b64)
    combined = base64.b64decode(combined_b64)
    nonce, ciphertext = combined[:12], combined[12:]
    aesgcm = AESGCM(key)
    compressed = aesgcm.decrypt(nonce, ciphertext, None)
    return gzip.decompress(compressed).decode('utf-8')
