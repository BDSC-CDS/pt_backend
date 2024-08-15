# openapi_client.AuditLogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_log_service_get_logs**](AuditLogApi.md#audit_log_service_get_logs) | **GET** /api/v1/audit/logs | Get logs
[**audit_log_service_get_logs_for_user**](AuditLogApi.md#audit_log_service_get_logs_for_user) | **GET** /api/v1/audit/users/{userid}/logs | Get logs for a user


# **audit_log_service_get_logs**
> TemplatebackendGetLogsResponse audit_log_service_get_logs(offset=offset, limit=limit, filters=filters, sort_by=sort_by)

Get logs

Gets a list of logs.

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_logs_response import TemplatebackendGetLogsResponse
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
    api_instance = openapi_client.AuditLogApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    filters = 'filters_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)

    try:
        # Get logs
        api_response = api_instance.audit_log_service_get_logs(offset=offset, limit=limit, filters=filters, sort_by=sort_by)
        print("The response of AuditLogApi->audit_log_service_get_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->audit_log_service_get_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **filters** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 

### Return type

[**TemplatebackendGetLogsResponse**](TemplatebackendGetLogsResponse.md)

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

# **audit_log_service_get_logs_for_user**
> TemplatebackendGetLogsResponse audit_log_service_get_logs_for_user(userid, offset=offset, limit=limit, filters=filters, sort_by=sort_by)

Get logs for a user

Gets logs for a specific user.

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_logs_response import TemplatebackendGetLogsResponse
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
    api_instance = openapi_client.AuditLogApi(api_client)
    userid = 56 # int | 
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    filters = 'filters_example' # str |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)

    try:
        # Get logs for a user
        api_response = api_instance.audit_log_service_get_logs_for_user(userid, offset=offset, limit=limit, filters=filters, sort_by=sort_by)
        print("The response of AuditLogApi->audit_log_service_get_logs_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->audit_log_service_get_logs_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **filters** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 

### Return type

[**TemplatebackendGetLogsResponse**](TemplatebackendGetLogsResponse.md)

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

