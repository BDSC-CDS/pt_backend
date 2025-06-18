# openapi_client.UsersServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_service_create_user**](UsersServiceApi.md#users_service_create_user) | **POST** /api/rest/v1/users | Create a user
[**users_service_delete_user**](UsersServiceApi.md#users_service_delete_user) | **DELETE** /api/rest/v1/users/{id} | Delete a user
[**users_service_get_user**](UsersServiceApi.md#users_service_get_user) | **GET** /api/rest/v1/users/{id} | Get a user
[**users_service_get_user_me**](UsersServiceApi.md#users_service_get_user_me) | **GET** /api/rest/v1/users/me | Get my own user
[**users_service_reset_password**](UsersServiceApi.md#users_service_reset_password) | **POST** /api/rest/v1/users/{id}/password/reset | Reset password
[**users_service_search_users**](UsersServiceApi.md#users_service_search_users) | **POST** /api/rest/v1/users/search | Search users
[**users_service_update_password**](UsersServiceApi.md#users_service_update_password) | **PUT** /api/rest/v1/users/me/password | Update password


# **users_service_create_user**
> TemplatebackendCreateUserReply users_service_create_user(body)

Create a user

This endpoint creates a user

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_create_user_reply import TemplatebackendCreateUserReply
from openapi_client.models.templatebackend_user import TemplatebackendUser
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
    api_instance = openapi_client.UsersServiceApi(api_client)
    body = openapi_client.TemplatebackendUser() # TemplatebackendUser | 

    try:
        # Create a user
        api_response = api_instance.users_service_create_user(body)
        print("The response of UsersServiceApi->users_service_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersServiceApi->users_service_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendUser**](TemplatebackendUser.md)|  | 

### Return type

[**TemplatebackendCreateUserReply**](TemplatebackendCreateUserReply.md)

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

# **users_service_delete_user**
> TemplatebackendDeleteUserReply users_service_delete_user(id)

Delete a user

This endpoint deletes a user

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_delete_user_reply import TemplatebackendDeleteUserReply
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
    api_instance = openapi_client.UsersServiceApi(api_client)
    id = 56 # int | 

    try:
        # Delete a user
        api_response = api_instance.users_service_delete_user(id)
        print("The response of UsersServiceApi->users_service_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersServiceApi->users_service_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendDeleteUserReply**](TemplatebackendDeleteUserReply.md)

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

# **users_service_get_user**
> TemplatebackendGetUserReply users_service_get_user(id)

Get a user

This endpoint returns a user

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_user_reply import TemplatebackendGetUserReply
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
    api_instance = openapi_client.UsersServiceApi(api_client)
    id = 56 # int | 

    try:
        # Get a user
        api_response = api_instance.users_service_get_user(id)
        print("The response of UsersServiceApi->users_service_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersServiceApi->users_service_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TemplatebackendGetUserReply**](TemplatebackendGetUserReply.md)

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

# **users_service_get_user_me**
> TemplatebackendGetUserMeReply users_service_get_user_me()

Get my own user

This endpoint returns the details of the authenticated user

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_user_me_reply import TemplatebackendGetUserMeReply
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
    api_instance = openapi_client.UsersServiceApi(api_client)

    try:
        # Get my own user
        api_response = api_instance.users_service_get_user_me()
        print("The response of UsersServiceApi->users_service_get_user_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersServiceApi->users_service_get_user_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TemplatebackendGetUserMeReply**](TemplatebackendGetUserMeReply.md)

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

# **users_service_reset_password**
> TemplatebackendResetPasswordReply users_service_reset_password(id, body)

Reset password

This endpoint resets a user's password

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_reset_password_reply import TemplatebackendResetPasswordReply
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
    api_instance = openapi_client.UsersServiceApi(api_client)
    id = 56 # int | 
    body = None # object | 

    try:
        # Reset password
        api_response = api_instance.users_service_reset_password(id, body)
        print("The response of UsersServiceApi->users_service_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersServiceApi->users_service_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | **object**|  | 

### Return type

[**TemplatebackendResetPasswordReply**](TemplatebackendResetPasswordReply.md)

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

# **users_service_search_users**
> TemplatebackendSearchUsersReply users_service_search_users(body)

Search users

This endpoint searches for users

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_search_users_reply import TemplatebackendSearchUsersReply
from openapi_client.models.templatebackend_search_users_request import TemplatebackendSearchUsersRequest
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
    api_instance = openapi_client.UsersServiceApi(api_client)
    body = openapi_client.TemplatebackendSearchUsersRequest() # TemplatebackendSearchUsersRequest | 

    try:
        # Search users
        api_response = api_instance.users_service_search_users(body)
        print("The response of UsersServiceApi->users_service_search_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersServiceApi->users_service_search_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendSearchUsersRequest**](TemplatebackendSearchUsersRequest.md)|  | 

### Return type

[**TemplatebackendSearchUsersReply**](TemplatebackendSearchUsersReply.md)

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

# **users_service_update_password**
> TemplatebackendUpdatePasswordReply users_service_update_password(body)

Update password

This endpoint updates the password of the authenticated user

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_update_password_reply import TemplatebackendUpdatePasswordReply
from openapi_client.models.templatebackend_update_password_request import TemplatebackendUpdatePasswordRequest
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
    api_instance = openapi_client.UsersServiceApi(api_client)
    body = openapi_client.TemplatebackendUpdatePasswordRequest() # TemplatebackendUpdatePasswordRequest | 

    try:
        # Update password
        api_response = api_instance.users_service_update_password(body)
        print("The response of UsersServiceApi->users_service_update_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersServiceApi->users_service_update_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TemplatebackendUpdatePasswordRequest**](TemplatebackendUpdatePasswordRequest.md)|  | 

### Return type

[**TemplatebackendUpdatePasswordReply**](TemplatebackendUpdatePasswordReply.md)

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

