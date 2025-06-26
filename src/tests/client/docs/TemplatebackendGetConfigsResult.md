# TemplatebackendGetConfigsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[TemplatebackendConfig]**](TemplatebackendConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_get_configs_result import TemplatebackendGetConfigsResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendGetConfigsResult from a JSON string
templatebackend_get_configs_result_instance = TemplatebackendGetConfigsResult.from_json(json)
# print the JSON string representation of the object
print TemplatebackendGetConfigsResult.to_json()

# convert the object into a dict
templatebackend_get_configs_result_dict = templatebackend_get_configs_result_instance.to_dict()
# create an instance of TemplatebackendGetConfigsResult from a dict
templatebackend_get_configs_result_form_dict = templatebackend_get_configs_result.from_dict(templatebackend_get_configs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


