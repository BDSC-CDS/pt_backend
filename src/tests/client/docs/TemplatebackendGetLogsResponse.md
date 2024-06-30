# TemplatebackendGetLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[TemplatebackendAuditLog]**](TemplatebackendAuditLog.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_get_logs_response import TemplatebackendGetLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendGetLogsResponse from a JSON string
templatebackend_get_logs_response_instance = TemplatebackendGetLogsResponse.from_json(json)
# print the JSON string representation of the object
print TemplatebackendGetLogsResponse.to_json()

# convert the object into a dict
templatebackend_get_logs_response_dict = templatebackend_get_logs_response_instance.to_dict()
# create an instance of TemplatebackendGetLogsResponse from a dict
templatebackend_get_logs_response_form_dict = templatebackend_get_logs_response.from_dict(templatebackend_get_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


