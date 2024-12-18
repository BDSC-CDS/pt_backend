import json
import base64
import requests
from urllib.parse import urlencode
from src.internal.util.crypto import encrypt, decrypt

class JupyterhubClient:
    def __init__(self, config):
        self.host = config.host.rstrip('/')
        self.token = config.token
        self.key = config.key
        self.headers = {
            "Authorization": f"token {self.token}",
            "Content-Type": "application/json"
        }

    def create_user(self, username: str) -> requests.Response:
        endpoint = f"{self.host}/hub/api/users/{username}"
        response = requests.post(endpoint, headers=self.headers, json={})
        return response

    def launch_named_server(self, username: str, server_name: str) -> requests.Response:
        endpoint = f"{self.host}/hub/api/users/{username}/servers/{server_name}"
        response = requests.post(endpoint, headers=self.headers, json={})
        return response

    def get_authenticate_user_url(self, backend_jwt_token: str, notebook_bytes:bytes, next_url_path: str) -> str:
        endpoint = f"{self.host}/hub/backendJWTlogin"
        next_url = f"{self.host}{next_url_path}"

        notebook_bytes_b64_encoded_str = base64.b64encode(notebook_bytes).decode('utf-8')
                                                                    
        payload = {
            "backend_jwt_token": backend_jwt_token,
            "bytes": notebook_bytes_b64_encoded_str
        }

        encrypted_payload = encrypt(self.key, json.dumps(payload))

        params = {
            "encrypted_payload": encrypted_payload,
            "next": next_url
        }

        parameters = urlencode(params)
        return f"{endpoint}?{parameters}"

