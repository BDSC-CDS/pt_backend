# V1GetLogsResponse

The response message containing the list of logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[V1AuditLog]**](V1AuditLog.md) |  | [optional] 

## Example

```python
from openapi_client.models.v1_get_logs_response import V1GetLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GetLogsResponse from a JSON string
v1_get_logs_response_instance = V1GetLogsResponse.from_json(json)
# print the JSON string representation of the object
print V1GetLogsResponse.to_json()

# convert the object into a dict
v1_get_logs_response_dict = v1_get_logs_response_instance.to_dict()
# create an instance of V1GetLogsResponse from a dict
v1_get_logs_response_form_dict = v1_get_logs_response.from_dict(v1_get_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


