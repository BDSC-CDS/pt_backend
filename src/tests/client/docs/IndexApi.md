# openapi_client.IndexApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_service_create_hello**](IndexApi.md#index_service_create_hello) | **POST** /api/v1/hello/{identifier} | Get a hello
[**index_service_get_hello**](IndexApi.md#index_service_get_hello) | **GET** /api/v1/hello | Get a hello
[**index_service_get_helloo**](IndexApi.md#index_service_get_helloo) | **GET** /api/v1/helloo | Get a hello


# **index_service_create_hello**
> TemplatebackendCreateHelloReply index_service_create_hello(identifier, body)

Get a hello

This endpoint returns a hello

### Example

* Api Key Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.index_service_create_hello_request import IndexServiceCreateHelloRequest
from openapi_client.models.templatebackend_create_hello_reply import TemplatebackendCreateHelloReply
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
    api_instance = openapi_client.IndexApi(api_client)
    identifier = 56 # int | 
    body = openapi_client.IndexServiceCreateHelloRequest() # IndexServiceCreateHelloRequest | 

    try:
        # Get a hello
        api_response = api_instance.index_service_create_hello(identifier, body)
        print("The response of IndexApi->index_service_create_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->index_service_create_hello: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **int**|  | 
 **body** | [**IndexServiceCreateHelloRequest**](IndexServiceCreateHelloRequest.md)|  | 

### Return type

[**TemplatebackendCreateHelloReply**](TemplatebackendCreateHelloReply.md)

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

# **index_service_get_hello**
> TemplatebackendGetHelloReply index_service_get_hello()

Get a hello

This endpoint returns a hello

### Example

* Api Key Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_hello_reply import TemplatebackendGetHelloReply
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
    api_instance = openapi_client.IndexApi(api_client)

    try:
        # Get a hello
        api_response = api_instance.index_service_get_hello()
        print("The response of IndexApi->index_service_get_hello:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->index_service_get_hello: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TemplatebackendGetHelloReply**](TemplatebackendGetHelloReply.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_service_get_helloo**
> TemplatebackendGetHelloReply index_service_get_helloo()

Get a hello

This endpoint returns a hello

### Example

* Api Key Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_hello_reply import TemplatebackendGetHelloReply
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
    api_instance = openapi_client.IndexApi(api_client)

    try:
        # Get a hello
        api_response = api_instance.index_service_get_helloo()
        print("The response of IndexApi->index_service_get_helloo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->index_service_get_helloo: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TemplatebackendGetHelloReply**](TemplatebackendGetHelloReply.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

