# TemplatebackendCreateTransformConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**TemplatebackendTransformConfig**](TemplatebackendTransformConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_create_transform_config_request import TemplatebackendCreateTransformConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendCreateTransformConfigRequest from a JSON string
templatebackend_create_transform_config_request_instance = TemplatebackendCreateTransformConfigRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendCreateTransformConfigRequest.to_json()

# convert the object into a dict
templatebackend_create_transform_config_request_dict = templatebackend_create_transform_config_request_instance.to_dict()
# create an instance of TemplatebackendCreateTransformConfigRequest from a dict
templatebackend_create_transform_config_request_form_dict = templatebackend_create_transform_config_request.from_dict(templatebackend_create_transform_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


