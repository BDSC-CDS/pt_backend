import requests
from urllib.parse import urlencode

class JupyterhubClient:
    def __init__(self, config):
        self.url = config.url.rstrip('/')
        self.token = config.token
        self.headers = {
            "Authorization": f"token {self.token}",
            "Content-Type": "application/json"
        }

    def create_user(self, username: str) -> requests.Response:
        endpoint = f"{self.url}/hub/api/users/{username}"
        response = requests.post(endpoint, headers=self.headers, json={})
        return response

    def launch_named_server(self, username: str, server_name: str) -> requests.Response:
        endpoint = f"{self.url}/hub/api/users/{username}/servers/{server_name}"
        response = requests.post(endpoint, headers=self.headers, json={})
        return response

    def get_authenticate_user_url(self, backend_jwt_token: str, notebook_bytes:bytes, next_url_path: str) -> str:
        endpoint = f"{self.url}/hub/backendJWTLogin"
        next_url = f"{self.url}{next_url_path}"

        

        params = {
            "token": backend_jwe_token,
            "next": next_url
        }

        parameters = urlencode(params)
        return f"{endpoint}?{parameters}"

