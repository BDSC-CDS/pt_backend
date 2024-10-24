# AttributeTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quasi_identifying** | **List[str]** |  | [optional] 
**sensitive** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.attribute_types import AttributeTypes

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeTypes from a JSON string
attribute_types_instance = AttributeTypes.from_json(json)
# print the JSON string representation of the object
print AttributeTypes.to_json()

# convert the object into a dict
attribute_types_dict = attribute_types_instance.to_dict()
# create an instance of AttributeTypes from a dict
attribute_types_form_dict = attribute_types.from_dict(attribute_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


