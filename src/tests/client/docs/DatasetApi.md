# openapi_client.DatasetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataset_service_change_types_dataset**](DatasetApi.md#dataset_service_change_types_dataset) | **POST** /api/v1/dataset/types | Change the types of a dataset
[**dataset_service_delete_dataset**](DatasetApi.md#dataset_service_delete_dataset) | **DELETE** /api/v1/dataset/{id} | Deletes a dataset
[**dataset_service_get_dataset_content**](DatasetApi.md#dataset_service_get_dataset_content) | **GET** /api/v1/dataset/content/{id} | Get Dataset Content
[**dataset_service_get_dataset_identifier**](DatasetApi.md#dataset_service_get_dataset_identifier) | **GET** /api/v1/dataset/identifier/{id} | Get Dataset Content filtered by identifying and quasi identifying columns
[**dataset_service_get_dataset_metadata**](DatasetApi.md#dataset_service_get_dataset_metadata) | **GET** /api/v1/dataset/metadata/{id} | Get Dataset Metadata
[**dataset_service_list_datasets**](DatasetApi.md#dataset_service_list_datasets) | **GET** /api/v1/dataset | List datasets
[**dataset_service_revert_dataset**](DatasetApi.md#dataset_service_revert_dataset) | **POST** /api/v1/dataset/revert | Revert a dataset
[**dataset_service_store_dataset**](DatasetApi.md#dataset_service_store_dataset) | **POST** /api/v1/dataset | Store a dataset
[**dataset_service_transform_dataset**](DatasetApi.md#dataset_service_transform_dataset) | **POST** /api/v1/dataset/transform | Transform a dataset


# **dataset_service_change_types_dataset**
> TemplatebackendChangeTypesDatasetReply dataset_service_change_types_dataset(body)

Change the types of a dataset

This endpoint changes the types of a dataset

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_change_types_dataset_reply import TemplatebackendChangeTypesDatasetReply
from openapi_client.models.templatebackend_change_types_dataset_request import TemplatebackendChangeTypesDatasetRequest
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
    api_instance = openapi_client.DatasetApi(api_client)
    body = openapi_client.TemplatebackendChangeTypesDatasetRequest() # TemplatebackendChangeTypesDatasetRequest | 

    try:
        # Change the types of a dataset
        api_response = api_instance.dataset_service_change_types_dataset(body)
        print("The response of DatasetApi->dataset_service_change_types_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_service_change_types_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendChangeTypesDatasetRequest**](TemplatebackendChangeTypesDatasetRequest.md)|  | 

### Return type

[**TemplatebackendChangeTypesDatasetReply**](TemplatebackendChangeTypesDatasetReply.md)

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

# **dataset_service_delete_dataset**
> TemplatebackendDeleteDatasetReply dataset_service_delete_dataset(id)

Deletes a dataset

This endpoint deletes a dataset

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_delete_dataset_reply import TemplatebackendDeleteDatasetReply
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
    api_instance = openapi_client.DatasetApi(api_client)
    id = 56 # int | 

    try:
        # Deletes a dataset
        api_response = api_instance.dataset_service_delete_dataset(id)
        print("The response of DatasetApi->dataset_service_delete_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_service_delete_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendDeleteDatasetReply**](TemplatebackendDeleteDatasetReply.md)

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

# **dataset_service_get_dataset_content**
> TemplatebackendGetDatasetContentReply dataset_service_get_dataset_content(id, offset=offset, limit=limit)

Get Dataset Content

This endpoint allow getting a specific user's Dataset Content

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_dataset_content_reply import TemplatebackendGetDatasetContentReply
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
    api_instance = openapi_client.DatasetApi(api_client)
    id = 56 # int | 
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # Get Dataset Content
        api_response = api_instance.dataset_service_get_dataset_content(id, offset=offset, limit=limit)
        print("The response of DatasetApi->dataset_service_get_dataset_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_service_get_dataset_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**TemplatebackendGetDatasetContentReply**](TemplatebackendGetDatasetContentReply.md)

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

# **dataset_service_get_dataset_identifier**
> TemplatebackendGetDatasetContentReply dataset_service_get_dataset_identifier(id, offset=offset, limit=limit)

Get Dataset Content filtered by identifying and quasi identifying columns

This endpoint allow getting a specific user's Dataset Content filtered by identifying and quasi identifying columns

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_dataset_content_reply import TemplatebackendGetDatasetContentReply
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
    api_instance = openapi_client.DatasetApi(api_client)
    id = 56 # int | 
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # Get Dataset Content filtered by identifying and quasi identifying columns
        api_response = api_instance.dataset_service_get_dataset_identifier(id, offset=offset, limit=limit)
        print("The response of DatasetApi->dataset_service_get_dataset_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_service_get_dataset_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**TemplatebackendGetDatasetContentReply**](TemplatebackendGetDatasetContentReply.md)

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

# **dataset_service_get_dataset_metadata**
> TemplatebackendGetDatasetMetadataReply dataset_service_get_dataset_metadata(id)

Get Dataset Metadata

This endpoint allow getting a specific user's Dataset Metadata

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_dataset_metadata_reply import TemplatebackendGetDatasetMetadataReply
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
    api_instance = openapi_client.DatasetApi(api_client)
    id = 56 # int | 

    try:
        # Get Dataset Metadata
        api_response = api_instance.dataset_service_get_dataset_metadata(id)
        print("The response of DatasetApi->dataset_service_get_dataset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_service_get_dataset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendGetDatasetMetadataReply**](TemplatebackendGetDatasetMetadataReply.md)

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

# **dataset_service_list_datasets**
> TemplatebackendListDatasetsReply dataset_service_list_datasets(offset=offset, limit=limit)

List datasets

This endpoint allows listing a user's datasets

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_list_datasets_reply import TemplatebackendListDatasetsReply
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
    api_instance = openapi_client.DatasetApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List datasets
        api_response = api_instance.dataset_service_list_datasets(offset=offset, limit=limit)
        print("The response of DatasetApi->dataset_service_list_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_service_list_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**TemplatebackendListDatasetsReply**](TemplatebackendListDatasetsReply.md)

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

# **dataset_service_revert_dataset**
> TemplatebackendRevertDatasetReply dataset_service_revert_dataset(body)

Revert a dataset

This endpoint reverts a dataset

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_revert_dataset_reply import TemplatebackendRevertDatasetReply
from openapi_client.models.templatebackend_revert_dataset_request import TemplatebackendRevertDatasetRequest
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
    api_instance = openapi_client.DatasetApi(api_client)
    body = openapi_client.TemplatebackendRevertDatasetRequest() # TemplatebackendRevertDatasetRequest | 

    try:
        # Revert a dataset
        api_response = api_instance.dataset_service_revert_dataset(body)
        print("The response of DatasetApi->dataset_service_revert_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_service_revert_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendRevertDatasetRequest**](TemplatebackendRevertDatasetRequest.md)|  | 

### Return type

[**TemplatebackendRevertDatasetReply**](TemplatebackendRevertDatasetReply.md)

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

# **dataset_service_store_dataset**
> TemplatebackendStoreDatasetReply dataset_service_store_dataset(body)

Store a dataset

This endpoint stores a dataset

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_store_dataset_reply import TemplatebackendStoreDatasetReply
from openapi_client.models.templatebackend_store_dataset_request import TemplatebackendStoreDatasetRequest
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
    api_instance = openapi_client.DatasetApi(api_client)
    body = openapi_client.TemplatebackendStoreDatasetRequest() # TemplatebackendStoreDatasetRequest | 

    try:
        # Store a dataset
        api_response = api_instance.dataset_service_store_dataset(body)
        print("The response of DatasetApi->dataset_service_store_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_service_store_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendStoreDatasetRequest**](TemplatebackendStoreDatasetRequest.md)|  | 

### Return type

[**TemplatebackendStoreDatasetReply**](TemplatebackendStoreDatasetReply.md)

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

# **dataset_service_transform_dataset**
> TemplatebackendTransformDatasetReply dataset_service_transform_dataset(body)

Transform a dataset

This endpoint transforms a dataset

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_transform_dataset_reply import TemplatebackendTransformDatasetReply
from openapi_client.models.templatebackend_transform_dataset_request import TemplatebackendTransformDatasetRequest
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
    api_instance = openapi_client.DatasetApi(api_client)
    body = openapi_client.TemplatebackendTransformDatasetRequest() # TemplatebackendTransformDatasetRequest | 

    try:
        # Transform a dataset
        api_response = api_instance.dataset_service_transform_dataset(body)
        print("The response of DatasetApi->dataset_service_transform_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->dataset_service_transform_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendTransformDatasetRequest**](TemplatebackendTransformDatasetRequest.md)|  | 

### Return type

[**TemplatebackendTransformDatasetReply**](TemplatebackendTransformDatasetReply.md)

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

