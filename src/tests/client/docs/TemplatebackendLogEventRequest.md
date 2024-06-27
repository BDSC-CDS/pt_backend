# TemplatebackendLogEventRequest


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
from openapi_client.models.templatebackend_log_event_request import TemplatebackendLogEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendLogEventRequest from a JSON string
templatebackend_log_event_request_instance = TemplatebackendLogEventRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendLogEventRequest.to_json()

# convert the object into a dict
templatebackend_log_event_request_dict = templatebackend_log_event_request_instance.to_dict()
# create an instance of TemplatebackendLogEventRequest from a dict
templatebackend_log_event_request_form_dict = templatebackend_log_event_request.from_dict(templatebackend_log_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


