# openapi_client.MedicationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**medication_service_create_medication**](MedicationApi.md#medication_service_create_medication) | **POST** /api/v1/medication | Create a medication
[**medication_service_delete_medication**](MedicationApi.md#medication_service_delete_medication) | **DELETE** /api/v1/medication/{id} | Create a medication
[**medication_service_get_medication**](MedicationApi.md#medication_service_get_medication) | **GET** /api/v1/medication/{id} | Get medications
[**medication_service_list_medication**](MedicationApi.md#medication_service_list_medication) | **GET** /api/v1/medication | List medications


# **medication_service_create_medication**
> TemplatebackendCreateMedicationReply medication_service_create_medication(body)

Create a medication

This endpoint creates a medication, and its schedule

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_create_medication_reply import TemplatebackendCreateMedicationReply
from openapi_client.models.templatebackend_create_medication_request import TemplatebackendCreateMedicationRequest
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
    api_instance = openapi_client.MedicationApi(api_client)
    body = openapi_client.TemplatebackendCreateMedicationRequest() # TemplatebackendCreateMedicationRequest | 

    try:
        # Create a medication
        api_response = api_instance.medication_service_create_medication(body)
        print("The response of MedicationApi->medication_service_create_medication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MedicationApi->medication_service_create_medication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendCreateMedicationRequest**](TemplatebackendCreateMedicationRequest.md)|  | 

### Return type

[**TemplatebackendCreateMedicationReply**](TemplatebackendCreateMedicationReply.md)

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

# **medication_service_delete_medication**
> TemplatebackendDeleteMedicationReply medication_service_delete_medication(id)

Create a medication

This endpoint creates a medication, and its schedule

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_delete_medication_reply import TemplatebackendDeleteMedicationReply
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
    api_instance = openapi_client.MedicationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Create a medication
        api_response = api_instance.medication_service_delete_medication(id)
        print("The response of MedicationApi->medication_service_delete_medication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MedicationApi->medication_service_delete_medication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TemplatebackendDeleteMedicationReply**](TemplatebackendDeleteMedicationReply.md)

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

# **medication_service_get_medication**
> TemplatebackendGetMedicationReply medication_service_get_medication(id)

Get medications

This endpoint allow getting a single user's medication

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_medication_reply import TemplatebackendGetMedicationReply
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
    api_instance = openapi_client.MedicationApi(api_client)
    id = 56 # int | 

    try:
        # Get medications
        api_response = api_instance.medication_service_get_medication(id)
        print("The response of MedicationApi->medication_service_get_medication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MedicationApi->medication_service_get_medication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendGetMedicationReply**](TemplatebackendGetMedicationReply.md)

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

# **medication_service_list_medication**
> TemplatebackendListMedicationReply medication_service_list_medication(offset=offset, limit=limit)

List medications

This endpoint allows listing a user's medications

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_list_medication_reply import TemplatebackendListMedicationReply
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
    api_instance = openapi_client.MedicationApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List medications
        api_response = api_instance.medication_service_list_medication(offset=offset, limit=limit)
        print("The response of MedicationApi->medication_service_list_medication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MedicationApi->medication_service_list_medication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**TemplatebackendListMedicationReply**](TemplatebackendListMedicationReply.md)

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

