import unittest
import openapi_client
from pprint import pprint
from src.tests.acceptance.helpers.client import client, admin_client

class TestUser(unittest.TestCase):
    def test_create_get_user(self):
        with client() as api_client, admin_client() as api_admin_client:
            # Create an instance of the API class
            api_instance = openapi_client.UsersServiceApi(api_client)
            body = openapi_client.TemplatebackendUser(
                password="hello", 
                username="moto1", 
                email="hello.moto@gmail.com",
                firstName="hello",
                lastName="moto"
            )
            api_response = api_instance.users_service_create_user(body)
            print("The response of UsersServiceApi->users_service_create_user:\n")
            pprint(api_response)

            self.assertIsNotNone(api_response)
            self.assertIsInstance(api_response.result.id, int)
            id = api_response.result.id
            self.assertTrue(id > 0)

            # test getting user with an admin account to check for correct creation
            admin_api_instance = openapi_client.UsersServiceApi(api_admin_client)
            api_response = admin_api_instance.users_service_get_user(id=id)
            print("The response of UsersServiceApi->users_service_get_user:\n")
            pprint(api_response)
            self.assertIsNotNone(api_response)
            self.assertIsNotNone(api_response.result)
            self.assertIsNotNone(api_response.result.user)
            self.assertIsInstance(api_response.result.user.id, int)

            self.assertEqual(id, api_response.result.user.id)
            self.assertEqual(None, api_response.result.user.password)
            self.assertEqual("moto1", api_response.result.user.username)
            self.assertEqual("hello.moto@gmail.com", api_response.result.user.email)
            self.assertEqual("hello", api_response.result.user.first_name)
            self.assertEqual("moto", api_response.result.user.last_name)

if __name__ == '__main__':
    unittest.main()