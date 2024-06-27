# V1LogEventResponse

The response message for logging an event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.v1_log_event_response import V1LogEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1LogEventResponse from a JSON string
v1_log_event_response_instance = V1LogEventResponse.from_json(json)
# print the JSON string representation of the object
print V1LogEventResponse.to_json()

# convert the object into a dict
v1_log_event_response_dict = v1_log_event_response_instance.to_dict()
# create an instance of V1LogEventResponse from a dict
v1_log_event_response_form_dict = v1_log_event_response.from_dict(v1_log_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


