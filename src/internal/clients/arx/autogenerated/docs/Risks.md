# Risks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_average_prosecutor** | **float** |  | [optional] 
**expected_highest_prosecutor** | **float** |  | [optional] 
**expected_marketer** | **float** |  | [optional] 
**initial_average_prosecutor** | **float** |  | [optional] 
**initial_highest_prosecutor** | **float** |  | [optional] 
**initial_marketer** | **float** |  | [optional] 
**residual_average_prosecutor** | **float** |  | [optional] 
**residual_highest_prosecutor** | **float** |  | [optional] 
**residual_marketer** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.risks import Risks

# TODO update the JSON string below
json = "{}"
# create an instance of Risks from a JSON string
risks_instance = Risks.from_json(json)
# print the JSON string representation of the object
print Risks.to_json()

# convert the object into a dict
risks_dict = risks_instance.to_dict()
# create an instance of Risks from a dict
risks_form_dict = risks.from_dict(risks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


