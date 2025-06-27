# TemplatebackendSubstituteFieldListConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**field** | **str** |  | [optional] 
**substitution_list** | **List[str]** |  | [optional] 
**replacement** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_substitute_field_list_config import TemplatebackendSubstituteFieldListConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendSubstituteFieldListConfig from a JSON string
templatebackend_substitute_field_list_config_instance = TemplatebackendSubstituteFieldListConfig.from_json(json)
# print the JSON string representation of the object
print TemplatebackendSubstituteFieldListConfig.to_json()

# convert the object into a dict
templatebackend_substitute_field_list_config_dict = templatebackend_substitute_field_list_config_instance.to_dict()
# create an instance of TemplatebackendSubstituteFieldListConfig from a dict
templatebackend_substitute_field_list_config_form_dict = templatebackend_substitute_field_list_config.from_dict(templatebackend_substitute_field_list_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


