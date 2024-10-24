# openapi_client.RecordsApiApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_records_using_get**](RecordsApiApi.md#get_all_records_using_get) | **GET** /records/all | getAllRecords
[**get_records_by_period_and_username_using_get**](RecordsApiApi.md#get_records_by_period_and_username_using_get) | **GET** /records/period-username/{beginDate}/{endDate}/{username} | getRecordsByPeriodAndUsername
[**get_records_by_period_using_get**](RecordsApiApi.md#get_records_by_period_using_get) | **GET** /records/period/{beginDate}/{endDate} | getRecordsByPeriod
[**get_records_by_username_using_get**](RecordsApiApi.md#get_records_by_username_using_get) | **GET** /records/username/{username} | getRecordsByUsername


# **get_all_records_using_get**
> List[Record] get_all_records_using_get()

getAllRecords

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.record import Record
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
    api_instance = openapi_client.RecordsApiApi(api_client)

    try:
        # getAllRecords
        api_response = api_instance.get_all_records_using_get()
        print("The response of RecordsApiApi->get_all_records_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApiApi->get_all_records_using_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Record]**](Record.md)

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

# **get_records_by_period_and_username_using_get**
> List[object] get_records_by_period_and_username_using_get(begin_date, end_date, username)

getRecordsByPeriodAndUsername

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
    api_instance = openapi_client.RecordsApiApi(api_client)
    begin_date = '2013-10-20T19:20:30+01:00' # datetime | beginDate
    end_date = '2013-10-20T19:20:30+01:00' # datetime | endDate
    username = 'username_example' # str | username

    try:
        # getRecordsByPeriodAndUsername
        api_response = api_instance.get_records_by_period_and_username_using_get(begin_date, end_date, username)
        print("The response of RecordsApiApi->get_records_by_period_and_username_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApiApi->get_records_by_period_and_username_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_date** | **datetime**| beginDate | 
 **end_date** | **datetime**| endDate | 
 **username** | **str**| username | 

### Return type

**List[object]**

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

# **get_records_by_period_using_get**
> List[Record] get_records_by_period_using_get(begin_date, end_date)

getRecordsByPeriod

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.record import Record
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
    api_instance = openapi_client.RecordsApiApi(api_client)
    begin_date = '2013-10-20T19:20:30+01:00' # datetime | beginDate
    end_date = '2013-10-20T19:20:30+01:00' # datetime | endDate

    try:
        # getRecordsByPeriod
        api_response = api_instance.get_records_by_period_using_get(begin_date, end_date)
        print("The response of RecordsApiApi->get_records_by_period_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApiApi->get_records_by_period_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_date** | **datetime**| beginDate | 
 **end_date** | **datetime**| endDate | 

### Return type

[**List[Record]**](Record.md)

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

# **get_records_by_username_using_get**
> List[object] get_records_by_username_using_get(username)

getRecordsByUsername

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
    api_instance = openapi_client.RecordsApiApi(api_client)
    username = 'username_example' # str | username

    try:
        # getRecordsByUsername
        api_response = api_instance.get_records_by_username_using_get(username)
        print("The response of RecordsApiApi->get_records_by_username_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApiApi->get_records_by_username_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

**List[object]**

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

