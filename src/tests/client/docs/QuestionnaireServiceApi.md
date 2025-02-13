# openapi_client.QuestionnaireServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**questionnaire_service_create_questionnaire**](QuestionnaireServiceApi.md#questionnaire_service_create_questionnaire) | **POST** /api/v1/questionnaire | Create a questionnaire
[**questionnaire_service_create_questionnaire_version**](QuestionnaireServiceApi.md#questionnaire_service_create_questionnaire_version) | **POST** /api/v1/questionnaire/version | Create a questionnaire version
[**questionnaire_service_create_reply**](QuestionnaireServiceApi.md#questionnaire_service_create_reply) | **POST** /api/v1/questionnaire/replies | Create questionnaires reply
[**questionnaire_service_delete_questionnaire**](QuestionnaireServiceApi.md#questionnaire_service_delete_questionnaire) | **DELETE** /api/v1/questionnaire/{id} | Create a questionnaire
[**questionnaire_service_get_questionnaire**](QuestionnaireServiceApi.md#questionnaire_service_get_questionnaire) | **GET** /api/v1/questionnaire/{id} | Get questionnaires
[**questionnaire_service_get_reply**](QuestionnaireServiceApi.md#questionnaire_service_get_reply) | **GET** /api/v1/questionnaire/replies/{id} | Get a questionnaires reply
[**questionnaire_service_list_questionnaire**](QuestionnaireServiceApi.md#questionnaire_service_list_questionnaire) | **GET** /api/v1/questionnaire | List questionnaires
[**questionnaire_service_list_replies**](QuestionnaireServiceApi.md#questionnaire_service_list_replies) | **GET** /api/v1/questionnaire/replies | List questionnaires replies
[**questionnaire_service_share_reply**](QuestionnaireServiceApi.md#questionnaire_service_share_reply) | **POST** /api/v1/questionnaire/replies/{id}/share | Share questionnaires reply


# **questionnaire_service_create_questionnaire**
> TemplatebackendCreateQuestionnaireReply questionnaire_service_create_questionnaire(body)

Create a questionnaire

This endpoint creates a questionnaire

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_create_questionnaire_reply import TemplatebackendCreateQuestionnaireReply
from openapi_client.models.templatebackend_create_questionnaire_request import TemplatebackendCreateQuestionnaireRequest
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
    api_instance = openapi_client.QuestionnaireServiceApi(api_client)
    body = openapi_client.TemplatebackendCreateQuestionnaireRequest() # TemplatebackendCreateQuestionnaireRequest | 

    try:
        # Create a questionnaire
        api_response = api_instance.questionnaire_service_create_questionnaire(body)
        print("The response of QuestionnaireServiceApi->questionnaire_service_create_questionnaire:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireServiceApi->questionnaire_service_create_questionnaire: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendCreateQuestionnaireRequest**](TemplatebackendCreateQuestionnaireRequest.md)|  | 

### Return type

[**TemplatebackendCreateQuestionnaireReply**](TemplatebackendCreateQuestionnaireReply.md)

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

# **questionnaire_service_create_questionnaire_version**
> TemplatebackendCreateQuestionnaireVersionReply questionnaire_service_create_questionnaire_version(body)

Create a questionnaire version

This endpoint creates a questionnaire version

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_create_questionnaire_version_reply import TemplatebackendCreateQuestionnaireVersionReply
from openapi_client.models.templatebackend_create_questionnaire_version_request import TemplatebackendCreateQuestionnaireVersionRequest
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
    api_instance = openapi_client.QuestionnaireServiceApi(api_client)
    body = openapi_client.TemplatebackendCreateQuestionnaireVersionRequest() # TemplatebackendCreateQuestionnaireVersionRequest | 

    try:
        # Create a questionnaire version
        api_response = api_instance.questionnaire_service_create_questionnaire_version(body)
        print("The response of QuestionnaireServiceApi->questionnaire_service_create_questionnaire_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireServiceApi->questionnaire_service_create_questionnaire_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendCreateQuestionnaireVersionRequest**](TemplatebackendCreateQuestionnaireVersionRequest.md)|  | 

### Return type

[**TemplatebackendCreateQuestionnaireVersionReply**](TemplatebackendCreateQuestionnaireVersionReply.md)

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

# **questionnaire_service_create_reply**
> TemplatebackendCreateReplyReply questionnaire_service_create_reply(body)

Create questionnaires reply

This endpoint allows ceating a user's questionnaires reply

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_create_reply_reply import TemplatebackendCreateReplyReply
from openapi_client.models.templatebackend_create_reply_request import TemplatebackendCreateReplyRequest
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
    api_instance = openapi_client.QuestionnaireServiceApi(api_client)
    body = openapi_client.TemplatebackendCreateReplyRequest() # TemplatebackendCreateReplyRequest | 

    try:
        # Create questionnaires reply
        api_response = api_instance.questionnaire_service_create_reply(body)
        print("The response of QuestionnaireServiceApi->questionnaire_service_create_reply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireServiceApi->questionnaire_service_create_reply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendCreateReplyRequest**](TemplatebackendCreateReplyRequest.md)|  | 

### Return type

[**TemplatebackendCreateReplyReply**](TemplatebackendCreateReplyReply.md)

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

# **questionnaire_service_delete_questionnaire**
> TemplatebackendDeleteQuestionnaireReply questionnaire_service_delete_questionnaire(id)

Create a questionnaire

This endpoint creates a questionnaire

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_delete_questionnaire_reply import TemplatebackendDeleteQuestionnaireReply
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
    api_instance = openapi_client.QuestionnaireServiceApi(api_client)
    id = 'id_example' # str | 

    try:
        # Create a questionnaire
        api_response = api_instance.questionnaire_service_delete_questionnaire(id)
        print("The response of QuestionnaireServiceApi->questionnaire_service_delete_questionnaire:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireServiceApi->questionnaire_service_delete_questionnaire: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TemplatebackendDeleteQuestionnaireReply**](TemplatebackendDeleteQuestionnaireReply.md)

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

# **questionnaire_service_get_questionnaire**
> TemplatebackendGetQuestionnaireReply questionnaire_service_get_questionnaire(id)

Get questionnaires

This endpoint allow getting a single user's questionnaire

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_questionnaire_reply import TemplatebackendGetQuestionnaireReply
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
    api_instance = openapi_client.QuestionnaireServiceApi(api_client)
    id = 56 # int | 

    try:
        # Get questionnaires
        api_response = api_instance.questionnaire_service_get_questionnaire(id)
        print("The response of QuestionnaireServiceApi->questionnaire_service_get_questionnaire:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireServiceApi->questionnaire_service_get_questionnaire: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendGetQuestionnaireReply**](TemplatebackendGetQuestionnaireReply.md)

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

# **questionnaire_service_get_reply**
> TemplatebackendGetReplyReply questionnaire_service_get_reply(id)

Get a questionnaires reply

This endpoint allows getting a user's questionnaires reply

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_reply_reply import TemplatebackendGetReplyReply
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
    api_instance = openapi_client.QuestionnaireServiceApi(api_client)
    id = 56 # int | uint32 questionnaire_version_id = 1;

    try:
        # Get a questionnaires reply
        api_response = api_instance.questionnaire_service_get_reply(id)
        print("The response of QuestionnaireServiceApi->questionnaire_service_get_reply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireServiceApi->questionnaire_service_get_reply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| uint32 questionnaire_version_id &#x3D; 1; | 

### Return type

[**TemplatebackendGetReplyReply**](TemplatebackendGetReplyReply.md)

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

# **questionnaire_service_list_questionnaire**
> TemplatebackendListQuestionnaireReply questionnaire_service_list_questionnaire(offset=offset, limit=limit)

List questionnaires

This endpoint allows listing a user's questionnaires

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_list_questionnaire_reply import TemplatebackendListQuestionnaireReply
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
    api_instance = openapi_client.QuestionnaireServiceApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # List questionnaires
        api_response = api_instance.questionnaire_service_list_questionnaire(offset=offset, limit=limit)
        print("The response of QuestionnaireServiceApi->questionnaire_service_list_questionnaire:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireServiceApi->questionnaire_service_list_questionnaire: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**TemplatebackendListQuestionnaireReply**](TemplatebackendListQuestionnaireReply.md)

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

# **questionnaire_service_list_replies**
> TemplatebackendListRepliesReply questionnaire_service_list_replies(offset=offset, limit=limit)

List questionnaires replies

This endpoint allows listing a user's questionnaires replies

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_list_replies_reply import TemplatebackendListRepliesReply
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
    api_instance = openapi_client.QuestionnaireServiceApi(api_client)
    offset = 56 # int | uint32 questionnaire_version_id = 1; (optional)
    limit = 56 # int |  (optional)

    try:
        # List questionnaires replies
        api_response = api_instance.questionnaire_service_list_replies(offset=offset, limit=limit)
        print("The response of QuestionnaireServiceApi->questionnaire_service_list_replies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireServiceApi->questionnaire_service_list_replies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| uint32 questionnaire_version_id &#x3D; 1; | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**TemplatebackendListRepliesReply**](TemplatebackendListRepliesReply.md)

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

# **questionnaire_service_share_reply**
> TemplatebackendShareReplyReply questionnaire_service_share_reply(id, body)

Share questionnaires reply

This endpoint allows sharing a user's questionnaires reply

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.questionnaire_service_share_reply_request import QuestionnaireServiceShareReplyRequest
from openapi_client.models.templatebackend_share_reply_reply import TemplatebackendShareReplyReply
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
    api_instance = openapi_client.QuestionnaireServiceApi(api_client)
    id = 56 # int | 
    body = openapi_client.QuestionnaireServiceShareReplyRequest() # QuestionnaireServiceShareReplyRequest | 

    try:
        # Share questionnaires reply
        api_response = api_instance.questionnaire_service_share_reply(id, body)
        print("The response of QuestionnaireServiceApi->questionnaire_service_share_reply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionnaireServiceApi->questionnaire_service_share_reply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**QuestionnaireServiceShareReplyRequest**](QuestionnaireServiceShareReplyRequest.md)|  | 

### Return type

[**TemplatebackendShareReplyReply**](TemplatebackendShareReplyReply.md)

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

