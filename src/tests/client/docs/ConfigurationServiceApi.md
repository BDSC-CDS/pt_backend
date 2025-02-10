# openapi_client.ConfigurationServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration_service_create_config**](ConfigurationServiceApi.md#configuration_service_create_config) | **POST** /api/rest/v1/configs | Create a configuration
[**configuration_service_delete_config**](ConfigurationServiceApi.md#configuration_service_delete_config) | **DELETE** /api/v1/config/{id} | Deletes a config
[**configuration_service_export_config**](ConfigurationServiceApi.md#configuration_service_export_config) | **GET** /api/rest/v1/config/export/{id} | Export a configuration as json (SPHN Connector format)
[**configuration_service_get_configs**](ConfigurationServiceApi.md#configuration_service_get_configs) | **GET** /api/rest/v1/configs | Get configuration files


# **configuration_service_create_config**
> TemplatebackendCreateConfigReply configuration_service_create_config(body)

Create a configuration

This endpoint creates a usconfigurationer

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_config import TemplatebackendConfig
from openapi_client.models.templatebackend_create_config_reply import TemplatebackendCreateConfigReply
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
    api_instance = openapi_client.ConfigurationServiceApi(api_client)
    body = openapi_client.TemplatebackendConfig() # TemplatebackendConfig | 

    try:
        # Create a configuration
        api_response = api_instance.configuration_service_create_config(body)
        print("The response of ConfigurationServiceApi->configuration_service_create_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationServiceApi->configuration_service_create_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendConfig**](TemplatebackendConfig.md)|  | 

### Return type

[**TemplatebackendCreateConfigReply**](TemplatebackendCreateConfigReply.md)

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

# **configuration_service_delete_config**
> TemplatebackendDeleteConfigReply configuration_service_delete_config(id)

Deletes a config

This endpoint deletes a config

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_delete_config_reply import TemplatebackendDeleteConfigReply
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
    api_instance = openapi_client.ConfigurationServiceApi(api_client)
    id = 56 # int | 

    try:
        # Deletes a config
        api_response = api_instance.configuration_service_delete_config(id)
        print("The response of ConfigurationServiceApi->configuration_service_delete_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationServiceApi->configuration_service_delete_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendDeleteConfigReply**](TemplatebackendDeleteConfigReply.md)

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

# **configuration_service_export_config**
> TemplatebackendExportConfigReply configuration_service_export_config(id)

Export a configuration as json (SPHN Connector format)

This endpoint returns the JSON of a configuration

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_export_config_reply import TemplatebackendExportConfigReply
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
    api_instance = openapi_client.ConfigurationServiceApi(api_client)
    id = 56 # int | 

    try:
        # Export a configuration as json (SPHN Connector format)
        api_response = api_instance.configuration_service_export_config(id)
        print("The response of ConfigurationServiceApi->configuration_service_export_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationServiceApi->configuration_service_export_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendExportConfigReply**](TemplatebackendExportConfigReply.md)

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

# **configuration_service_get_configs**
> TemplatebackendGetConfigsReply configuration_service_get_configs()

Get configuration files

This endpoint returns the configuration files for a given user

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_configs_reply import TemplatebackendGetConfigsReply
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
    api_instance = openapi_client.ConfigurationServiceApi(api_client)

    try:
        # Get configuration files
        api_response = api_instance.configuration_service_get_configs()
        print("The response of ConfigurationServiceApi->configuration_service_get_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationServiceApi->configuration_service_get_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TemplatebackendGetConfigsReply**](TemplatebackendGetConfigsReply.md)

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

