# TemplatebackendConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**userid** | **int** |  | [optional] 
**tenantid** | **int** |  | [optional] 
**config_name** | **str** |  | [optional] 
**questionnaireid** | **int** |  | [optional] 
**has_scramble_field** | **bool** |  | [optional] 
**has_date_shift** | **bool** |  | [optional] 
**hassub_field_list** | **bool** |  | [optional] 
**hassub_field_regex** | **bool** |  | [optional] 
**scramble_field_fields** | **List[str]** |  | [optional] 
**date_shift_lowrange** | **int** |  | [optional] 
**date_shift_highrange** | **int** |  | [optional] 
**sub_field_list_field** | **str** |  | [optional] 
**sub_field_list_substitute** | **List[str]** |  | [optional] 
**sub_field_list_replacement** | **str** |  | [optional] 
**sub_field_regex_field** | **str** |  | [optional] 
**sub_field_regex_regex** | **str** |  | [optional] 
**sub_field_regex_replacement** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_config import TemplatebackendConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendConfig from a JSON string
templatebackend_config_instance = TemplatebackendConfig.from_json(json)
# print the JSON string representation of the object
print TemplatebackendConfig.to_json()

# convert the object into a dict
templatebackend_config_dict = templatebackend_config_instance.to_dict()
# create an instance of TemplatebackendConfig from a dict
templatebackend_config_form_dict = templatebackend_config.from_dict(templatebackend_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


