# openapi_client.DeidentificationApiApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_expert_by_average_prosecutor_risk_level_using_post**](DeidentificationApiApi.md#apply_expert_by_average_prosecutor_risk_level_using_post) | **POST** /deidentification/expert/average-prosecutor-risk-level | applyExpertByAverageProsecutorRiskLevel
[**apply_expert_by_highest_prosecutor_risk_level_using_post**](DeidentificationApiApi.md#apply_expert_by_highest_prosecutor_risk_level_using_post) | **POST** /deidentification/expert/highest-prosecutor-risk-level | applyExpertByHighestProsecutorRiskLevel
[**apply_expert_by_marketer_risk_level_using_post**](DeidentificationApiApi.md#apply_expert_by_marketer_risk_level_using_post) | **POST** /deidentification/expert/marketer-risk-level | applyExpertByMarketerRiskLevel
[**apply_expert_by_privacy_models_using_post**](DeidentificationApiApi.md#apply_expert_by_privacy_models_using_post) | **POST** /deidentification/expert/privacy-models | applyExpertByPrivacyModels
[**apply_expert_internal_chuv_context_using_post**](DeidentificationApiApi.md#apply_expert_internal_chuv_context_using_post) | **POST** /deidentification/expert/internal-chuv | applyExpertInternalCHUVContext
[**apply_expert_multicentric_context_using_post**](DeidentificationApiApi.md#apply_expert_multicentric_context_using_post) | **POST** /deidentification/expert/multicentric | applyExpertMulticentricContext
[**apply_expert_publication_context_using_post**](DeidentificationApiApi.md#apply_expert_publication_context_using_post) | **POST** /deidentification/expert/publication | applyExpertPublicationContext
[**apply_safe_harbor_using_post**](DeidentificationApiApi.md#apply_safe_harbor_using_post) | **POST** /deidentification/safe-harbor | applySafeHarbor
[**code_using_post**](DeidentificationApiApi.md#code_using_post) | **POST** /deidentification/code | code
[**decode_using_post**](DeidentificationApiApi.md#decode_using_post) | **POST** /deidentification/decode | decode


# **apply_expert_by_average_prosecutor_risk_level_using_post**
> JobResults apply_expert_by_average_prosecutor_risk_level_using_post(body)

applyExpertByAverageProsecutorRiskLevel

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # applyExpertByAverageProsecutorRiskLevel
        api_response = api_instance.apply_expert_by_average_prosecutor_risk_level_using_post(body)
        print("The response of DeidentificationApiApi->apply_expert_by_average_prosecutor_risk_level_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->apply_expert_by_average_prosecutor_risk_level_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_expert_by_highest_prosecutor_risk_level_using_post**
> JobResults apply_expert_by_highest_prosecutor_risk_level_using_post(body)

applyExpertByHighestProsecutorRiskLevel

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # applyExpertByHighestProsecutorRiskLevel
        api_response = api_instance.apply_expert_by_highest_prosecutor_risk_level_using_post(body)
        print("The response of DeidentificationApiApi->apply_expert_by_highest_prosecutor_risk_level_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->apply_expert_by_highest_prosecutor_risk_level_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_expert_by_marketer_risk_level_using_post**
> JobResults apply_expert_by_marketer_risk_level_using_post(body)

applyExpertByMarketerRiskLevel

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # applyExpertByMarketerRiskLevel
        api_response = api_instance.apply_expert_by_marketer_risk_level_using_post(body)
        print("The response of DeidentificationApiApi->apply_expert_by_marketer_risk_level_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->apply_expert_by_marketer_risk_level_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_expert_by_privacy_models_using_post**
> JobResults apply_expert_by_privacy_models_using_post(body)

applyExpertByPrivacyModels

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # applyExpertByPrivacyModels
        api_response = api_instance.apply_expert_by_privacy_models_using_post(body)
        print("The response of DeidentificationApiApi->apply_expert_by_privacy_models_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->apply_expert_by_privacy_models_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_expert_internal_chuv_context_using_post**
> JobResults apply_expert_internal_chuv_context_using_post(body)

applyExpertInternalCHUVContext

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # applyExpertInternalCHUVContext
        api_response = api_instance.apply_expert_internal_chuv_context_using_post(body)
        print("The response of DeidentificationApiApi->apply_expert_internal_chuv_context_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->apply_expert_internal_chuv_context_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_expert_multicentric_context_using_post**
> JobResults apply_expert_multicentric_context_using_post(body)

applyExpertMulticentricContext

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # applyExpertMulticentricContext
        api_response = api_instance.apply_expert_multicentric_context_using_post(body)
        print("The response of DeidentificationApiApi->apply_expert_multicentric_context_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->apply_expert_multicentric_context_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_expert_publication_context_using_post**
> JobResults apply_expert_publication_context_using_post(body)

applyExpertPublicationContext

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # applyExpertPublicationContext
        api_response = api_instance.apply_expert_publication_context_using_post(body)
        print("The response of DeidentificationApiApi->apply_expert_publication_context_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->apply_expert_publication_context_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_safe_harbor_using_post**
> JobResults apply_safe_harbor_using_post(body)

applySafeHarbor

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # applySafeHarbor
        api_response = api_instance.apply_safe_harbor_using_post(body)
        print("The response of DeidentificationApiApi->apply_safe_harbor_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->apply_safe_harbor_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_using_post**
> JobResults code_using_post(body)

code

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # code
        api_response = api_instance.code_using_post(body)
        print("The response of DeidentificationApiApi->code_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->code_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_using_post**
> JobResults decode_using_post(body)

decode

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.job_results import JobResults
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
    api_instance = openapi_client.DeidentificationApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # decode
        api_response = api_instance.decode_using_post(body)
        print("The response of DeidentificationApiApi->decode_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeidentificationApiApi->decode_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dict[str, object]**](object.md)| body | 

### Return type

[**JobResults**](JobResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

