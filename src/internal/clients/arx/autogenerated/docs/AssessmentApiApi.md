# openapi_client.AssessmentApiApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assess_using_post**](AssessmentApiApi.md#assess_using_post) | **POST** /assessment | assess


# **assess_using_post**
> JobResults assess_using_post(body)

assess

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
    api_instance = openapi_client.AssessmentApiApi(api_client)
    body = None # Dict[str, object] | body

    try:
        # assess
        api_response = api_instance.assess_using_post(body)
        print("The response of AssessmentApiApi->assess_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssessmentApiApi->assess_using_post: %s\n" % e)
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

