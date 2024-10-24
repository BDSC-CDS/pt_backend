# openapi_client.RiskAssessmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**risk_assessment_service_get_risk_assessment**](RiskAssessmentApi.md#risk_assessment_service_get_risk_assessment) | **GET** /api/v1/riskassessment | Get risk assessment


# **risk_assessment_service_get_risk_assessment**
> TemplatebackendGetRiskAssessmentReply risk_assessment_service_get_risk_assessment()

Get risk assessment

This endpoint allow getting a single user's risk assessment

### Example

* Api Key Authentication (Bearer):

```python
import time
import os
import openapi_client
from openapi_client.models.templatebackend_get_risk_assessment_reply import TemplatebackendGetRiskAssessmentReply
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
    api_instance = openapi_client.RiskAssessmentApi(api_client)

    try:
        # Get risk assessment
        api_response = api_instance.risk_assessment_service_get_risk_assessment()
        print("The response of RiskAssessmentApi->risk_assessment_service_get_risk_assessment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RiskAssessmentApi->risk_assessment_service_get_risk_assessment: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TemplatebackendGetRiskAssessmentReply**](TemplatebackendGetRiskAssessmentReply.md)

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

