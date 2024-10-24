import openapi_client
from pprint import pprint

class ArxClient:
    def __init__(self, arx_client_config):
        configuration = openapi_client.Configuration(
            host = arx_client_config.host
        )
        self.api_client = openapi_client.ApiClient(configuration)

    def get_all_records(self):
        records_api_instance = openapi_client.RecordsApiApi(self.api_client)
        api_response = records_api_instance.get_all_records_using_get()

        print("The response of get_all_records:")
        pprint(api_response)
        
        return api_response