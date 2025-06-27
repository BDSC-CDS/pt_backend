# TemplatebackendListTransformConfigsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[TemplatebackendTransformConfig]**](TemplatebackendTransformConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_list_transform_configs_result import TemplatebackendListTransformConfigsResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendListTransformConfigsResult from a JSON string
templatebackend_list_transform_configs_result_instance = TemplatebackendListTransformConfigsResult.from_json(json)
# print the JSON string representation of the object
print TemplatebackendListTransformConfigsResult.to_json()

# convert the object into a dict
templatebackend_list_transform_configs_result_dict = templatebackend_list_transform_configs_result_instance.to_dict()
# create an instance of TemplatebackendListTransformConfigsResult from a dict
templatebackend_list_transform_configs_result_form_dict = templatebackend_list_transform_configs_result.from_dict(templatebackend_list_transform_configs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


