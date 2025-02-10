import time
import unittest
import json
import openapi_client
import base64
from pprint import pprint
from src.tests.acceptance.helpers.client import client

class TestAuthenticate(unittest.TestCase):
    def test_authenticate(self):
        with client() as api_client:
            # Create an instance of the API class
            user_api = openapi_client.UsersServiceApi(api_client)
            body = openapi_client.TemplatebackendUser(
                password="hello1234", 
                username="username2", 
                email="email@gmail.com",
                firstName="Jean",
                lastName="Marc"
            )
            api_response = user_api.users_service_create_user(body)
            self.assertIsNotNone(api_response)
            self.assertIsInstance(api_response.result.id, int)
            
            auth_api = openapi_client.AuthenticationServiceApi(api_client)
            body = openapi_client.TemplatebackendCredentials(username='username2', password="hello1234")
            r = auth_api.authentication_service_authenticate(body)
            self.assertIsNotNone(r)
            self.assertIsNotNone(r.result.token)
            self.assertIsInstance(r.result.token, str)

            token = r.result.token
            token_split = token.split(".")
            self.assertEqual(len(token_split), 3)

            payload_b64 = token_split[1]
            payload_b64 += "="*divmod(len(payload_b64),4)[1]
            payload_json = base64.b64decode(payload_b64)
            payload = json.loads(payload_json)
            #{'sub': '45', 'email': 'email@gmail.com', 'tenantid': 0, 'roles': [], 'username': 'username2', 'iat': 1706112543, 'exp': 1706371743}
            self.assertGreater(int(payload["sub"]), 0)
            self.assertEqual(payload["email"], "email@gmail.com")
            current_time = int(time.time())
            self.assertEqual(payload["tenantid"], 0)
            self.assertEqual(payload["roles"], [])
            self.assertEqual(payload["username"], "username2")
            self.assertGreaterEqual(payload["iat"], current_time - 10)  # not issued in the distant past
            self.assertLessEqual(payload["iat"], current_time + 10)     # not issued in the distant future
            expected_exp = payload["iat"] + (72 * 60 * 60)  # 72 hours from iat
            self.assertGreaterEqual(payload["exp"], expected_exp - 10)  # not expiring too early
            self.assertLessEqual(payload["exp"], expected_exp + 10)     # not expiring too late


if __name__ == '__main__':
    unittest.main()