# Attribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arx_name** | **str** |  | [optional] 
**attribute_type** | **str** |  | [optional] 
**dataset_name** | **str** |  | [optional] 
**var_date** | **bool** |  | [optional] 
**hierarchy** | **List[List[str]]** |  | [optional] 
**identifying** | **bool** |  | [optional] 
**ippor_numero_sejour** | **bool** |  | [optional] 
**quasi_identifying** | **bool** |  | [optional] 
**sensitive** | **bool** |  | [optional] 
**weight** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.attribute import Attribute

# TODO update the JSON string below
json = "{}"
# create an instance of Attribute from a JSON string
attribute_instance = Attribute.from_json(json)
# print the JSON string representation of the object
print Attribute.to_json()

# convert the object into a dict
attribute_dict = attribute_instance.to_dict()
# create an instance of Attribute from a dict
attribute_form_dict = attribute.from_dict(attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


