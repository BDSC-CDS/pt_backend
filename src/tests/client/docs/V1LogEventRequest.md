# V1LogEventRequest

The request message containing the audit log details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userid** | **int** |  | [optional] 
**service** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**response** | **str** |  | [optional] 
**error** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.v1_log_event_request import V1LogEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1LogEventRequest from a JSON string
v1_log_event_request_instance = V1LogEventRequest.from_json(json)
# print the JSON string representation of the object
print V1LogEventRequest.to_json()

# convert the object into a dict
v1_log_event_request_dict = v1_log_event_request_instance.to_dict()
# create an instance of V1LogEventRequest from a dict
v1_log_event_request_form_dict = v1_log_event_request.from_dict(v1_log_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


