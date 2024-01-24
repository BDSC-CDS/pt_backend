# TemplatebackendUpdatePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_update_password_request import TemplatebackendUpdatePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendUpdatePasswordRequest from a JSON string
templatebackend_update_password_request_instance = TemplatebackendUpdatePasswordRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendUpdatePasswordRequest.to_json()

# convert the object into a dict
templatebackend_update_password_request_dict = templatebackend_update_password_request_instance.to_dict()
# create an instance of TemplatebackendUpdatePasswordRequest from a dict
templatebackend_update_password_request_form_dict = templatebackend_update_password_request.from_dict(templatebackend_update_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


