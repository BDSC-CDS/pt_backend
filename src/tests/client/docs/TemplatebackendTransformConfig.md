# TemplatebackendTransformConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**userid** | **int** |  | [optional] 
**tenantid** | **int** |  | [optional] 
**questionnaireid** | **int** |  | [optional] 
**date_shift** | [**TemplatebackendDateShiftConfig**](TemplatebackendDateShiftConfig.md) |  | [optional] 
**scramble_field** | [**TemplatebackendScrambleFieldConfig**](TemplatebackendScrambleFieldConfig.md) |  | [optional] 
**sub_field_list_list** | [**List[TemplatebackendSubstituteFieldListConfig]**](TemplatebackendSubstituteFieldListConfig.md) |  | [optional] 
**sub_field_regex_list** | [**List[TemplatebackendSubstituteFieldRegexConfig]**](TemplatebackendSubstituteFieldRegexConfig.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_transform_config import TemplatebackendTransformConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendTransformConfig from a JSON string
templatebackend_transform_config_instance = TemplatebackendTransformConfig.from_json(json)
# print the JSON string representation of the object
print TemplatebackendTransformConfig.to_json()

# convert the object into a dict
templatebackend_transform_config_dict = templatebackend_transform_config_instance.to_dict()
# create an instance of TemplatebackendTransformConfig from a dict
templatebackend_transform_config_form_dict = templatebackend_transform_config.from_dict(templatebackend_transform_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


