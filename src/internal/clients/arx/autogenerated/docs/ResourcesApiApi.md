# openapi_client.ResourcesApiApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_expert_attributes_using_get**](ResourcesApiApi.md#get_expert_attributes_using_get) | **GET** /resources/expert-attributes | getExpertAttributes
[**get_expert_default_values_using_get**](ResourcesApiApi.md#get_expert_default_values_using_get) | **GET** /resources/expert-default-values | getExpertDefaultValues
[**get_hierarchies_using_get**](ResourcesApiApi.md#get_hierarchies_using_get) | **GET** /resources/hierarchies | getHierarchies
[**get_hierarchy_using_get**](ResourcesApiApi.md#get_hierarchy_using_get) | **GET** /resources/hierarchies/{attributeName} | getHierarchy
[**get_ipp_name_using_get**](ResourcesApiApi.md#get_ipp_name_using_get) | **GET** /resources/ipp-name | getIppName
[**get_numero_sejour_name_using_get**](ResourcesApiApi.md#get_numero_sejour_name_using_get) | **GET** /resources/numero-sejour-name | getNumeroSejourName
[**get_privacy_models_using_get**](ResourcesApiApi.md#get_privacy_models_using_get) | **GET** /resources/privacy-models | getPrivacyModels
[**get_safe_harbor_categories_using_get**](ResourcesApiApi.md#get_safe_harbor_categories_using_get) | **GET** /resources/safe-harbor-categories | getSafeHarborCategories


# **get_expert_attributes_using_get**
> List[Attribute] get_expert_attributes_using_get()

getExpertAttributes

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.attribute import Attribute
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApiApi(api_client)

    try:
        # getExpertAttributes
        api_response = api_instance.get_expert_attributes_using_get()
        print("The response of ResourcesApiApi->get_expert_attributes_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApiApi->get_expert_attributes_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Attribute]**](Attribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expert_default_values_using_get**
> Dict[str, object] get_expert_default_values_using_get()

getExpertDefaultValues

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApiApi(api_client)

    try:
        # getExpertDefaultValues
        api_response = api_instance.get_expert_default_values_using_get()
        print("The response of ResourcesApiApi->get_expert_default_values_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApiApi->get_expert_default_values_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hierarchies_using_get**
> Dict[str, object] get_hierarchies_using_get()

getHierarchies

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApiApi(api_client)

    try:
        # getHierarchies
        api_response = api_instance.get_hierarchies_using_get()
        print("The response of ResourcesApiApi->get_hierarchies_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApiApi->get_hierarchies_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hierarchy_using_get**
> Dict[str, object] get_hierarchy_using_get(attribute_name)

getHierarchy

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApiApi(api_client)
    attribute_name = 'attribute_name_example' # str | attributeName

    try:
        # getHierarchy
        api_response = api_instance.get_hierarchy_using_get(attribute_name)
        print("The response of ResourcesApiApi->get_hierarchy_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApiApi->get_hierarchy_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_name** | **str**| attributeName | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipp_name_using_get**
> List[str] get_ipp_name_using_get()

getIppName

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApiApi(api_client)

    try:
        # getIppName
        api_response = api_instance.get_ipp_name_using_get()
        print("The response of ResourcesApiApi->get_ipp_name_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApiApi->get_ipp_name_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_numero_sejour_name_using_get**
> List[str] get_numero_sejour_name_using_get()

getNumeroSejourName

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApiApi(api_client)

    try:
        # getNumeroSejourName
        api_response = api_instance.get_numero_sejour_name_using_get()
        print("The response of ResourcesApiApi->get_numero_sejour_name_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApiApi->get_numero_sejour_name_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privacy_models_using_get**
> List[PrivacyModel] get_privacy_models_using_get()

getPrivacyModels

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.privacy_model import PrivacyModel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApiApi(api_client)

    try:
        # getPrivacyModels
        api_response = api_instance.get_privacy_models_using_get()
        print("The response of ResourcesApiApi->get_privacy_models_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApiApi->get_privacy_models_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PrivacyModel]**](PrivacyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_safe_harbor_categories_using_get**
> List[str] get_safe_harbor_categories_using_get()

getSafeHarborCategories

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ResourcesApiApi(api_client)

    try:
        # getSafeHarborCategories
        api_response = api_instance.get_safe_harbor_categories_using_get()
        print("The response of ResourcesApiApi->get_safe_harbor_categories_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApiApi->get_safe_harbor_categories_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

