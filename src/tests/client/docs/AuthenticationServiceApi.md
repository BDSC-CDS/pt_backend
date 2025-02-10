# openapi_client.AuthenticationServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_service_authenticate**](AuthenticationServiceApi.md#authentication_service_authenticate) | **POST** /api/rest/v1/authentication/login | Authenticate


# **authentication_service_authenticate**
> TemplatebackendAuthenticationReply authentication_service_authenticate(body)

Authenticate

This endpoint authenticates a user

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_authentication_reply import TemplatebackendAuthenticationReply
from openapi_client.models.templatebackend_credentials import TemplatebackendCredentials
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthenticationServiceApi(api_client)
    body = openapi_client.TemplatebackendCredentials() # TemplatebackendCredentials | 

    try:
        # Authenticate
        api_response = api_instance.authentication_service_authenticate(body)
        print("The response of AuthenticationServiceApi->authentication_service_authenticate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationServiceApi->authentication_service_authenticate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendCredentials**](TemplatebackendCredentials.md)|  | 

### Return type

[**TemplatebackendAuthenticationReply**](TemplatebackendAuthenticationReply.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

