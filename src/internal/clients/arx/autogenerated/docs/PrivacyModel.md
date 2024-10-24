# PrivacyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**involved_attribute** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**params** | [**List[Param]**](Param.md) |  | [optional] 

## Example

```python
from openapi_client.models.privacy_model import PrivacyModel

# TODO update the JSON string below
json = "{}"
# create an instance of PrivacyModel from a JSON string
privacy_model_instance = PrivacyModel.from_json(json)
# print the JSON string representation of the object
print PrivacyModel.to_json()

# convert the object into a dict
privacy_model_dict = privacy_model_instance.to_dict()
# create an instance of PrivacyModel from a dict
privacy_model_form_dict = privacy_model.from_dict(privacy_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


