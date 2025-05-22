# openapi_client.TransformConfigServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transform_config_service_create_transform_config**](TransformConfigServiceApi.md#transform_config_service_create_transform_config) | **POST** /api/v1/transform-config | Create a transform configuration
[**transform_config_service_delete_transform_config**](TransformConfigServiceApi.md#transform_config_service_delete_transform_config) | **DELETE** /api/v1/transform-config/{id} | Delete transform configuration
[**transform_config_service_export_transform_config**](TransformConfigServiceApi.md#transform_config_service_export_transform_config) | **GET** /api/v1/transform-config/export/{id} | Export transform configuration as a string
[**transform_config_service_export_transform_config_json**](TransformConfigServiceApi.md#transform_config_service_export_transform_config_json) | **GET** /api/v1/transform-config/export/json/{id} | Export transform configuration as a JSON file 
[**transform_config_service_list_transform_configs**](TransformConfigServiceApi.md#transform_config_service_list_transform_configs) | **GET** /api/v1/transform-config | List transform configurations


# **transform_config_service_create_transform_config**
> TemplatebackendCreateTransformConfigReply transform_config_service_create_transform_config(body)

Create a transform configuration

This endpoint creates a dataset transform configuration

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_create_transform_config_reply import TemplatebackendCreateTransformConfigReply
from openapi_client.models.templatebackend_create_transform_config_request import TemplatebackendCreateTransformConfigRequest
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
    api_instance = openapi_client.TransformConfigServiceApi(api_client)
    body = openapi_client.TemplatebackendCreateTransformConfigRequest() # TemplatebackendCreateTransformConfigRequest | 

    try:
        # Create a transform configuration
        api_response = api_instance.transform_config_service_create_transform_config(body)
        print("The response of TransformConfigServiceApi->transform_config_service_create_transform_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformConfigServiceApi->transform_config_service_create_transform_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendCreateTransformConfigRequest**](TemplatebackendCreateTransformConfigRequest.md)|  | 

### Return type

[**TemplatebackendCreateTransformConfigReply**](TemplatebackendCreateTransformConfigReply.md)

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

# **transform_config_service_delete_transform_config**
> TemplatebackendDeleteTransformConfigReply transform_config_service_delete_transform_config(id)

Delete transform configuration

This endpoint deletes a dataset transform configuration

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_delete_transform_config_reply import TemplatebackendDeleteTransformConfigReply
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
    api_instance = openapi_client.TransformConfigServiceApi(api_client)
    id = 56 # int | 

    try:
        # Delete transform configuration
        api_response = api_instance.transform_config_service_delete_transform_config(id)
        print("The response of TransformConfigServiceApi->transform_config_service_delete_transform_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformConfigServiceApi->transform_config_service_delete_transform_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendDeleteTransformConfigReply**](TemplatebackendDeleteTransformConfigReply.md)

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

# **transform_config_service_export_transform_config**
> TemplatebackendExportTransformConfigReply transform_config_service_export_transform_config(id)

Export transform configuration as a string

This endpoint returns a JSON string of a transform configuration (SPHN Connector format)

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_export_transform_config_reply import TemplatebackendExportTransformConfigReply
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
    api_instance = openapi_client.TransformConfigServiceApi(api_client)
    id = 56 # int | 

    try:
        # Export transform configuration as a string
        api_response = api_instance.transform_config_service_export_transform_config(id)
        print("The response of TransformConfigServiceApi->transform_config_service_export_transform_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformConfigServiceApi->transform_config_service_export_transform_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendExportTransformConfigReply**](TemplatebackendExportTransformConfigReply.md)

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

# **transform_config_service_export_transform_config_json**
> ApiHttpBody transform_config_service_export_transform_config_json(id)

Export transform configuration as a JSON file 

This endpoint returns a JSON file of a transform configuration (SPHN Connector format)

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.api_http_body import ApiHttpBody
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
    api_instance = openapi_client.TransformConfigServiceApi(api_client)
    id = 56 # int | 

    try:
        # Export transform configuration as a JSON file 
        api_response = api_instance.transform_config_service_export_transform_config_json(id)
        print("The response of TransformConfigServiceApi->transform_config_service_export_transform_config_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformConfigServiceApi->transform_config_service_export_transform_config_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ApiHttpBody**](ApiHttpBody.md)

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

# **transform_config_service_list_transform_configs**
> TemplatebackendListTransformConfigsReply transform_config_service_list_transform_configs(offset=offset, limit=limit)

List transform configurations

This endpoint allows listing a user's dataset transform configurations

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_list_transform_configs_reply import TemplatebackendListTransformConfigsReply
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
    api_instance = openapi_client.TransformConfigServiceApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List transform configurations
        api_response = api_instance.transform_config_service_list_transform_configs(offset=offset, limit=limit)
        print("The response of TransformConfigServiceApi->transform_config_service_list_transform_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformConfigServiceApi->transform_config_service_list_transform_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**TemplatebackendListTransformConfigsReply**](TemplatebackendListTransformConfigsReply.md)

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

