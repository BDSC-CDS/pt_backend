# TemplatebackendMedication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**dosage** | **str** |  | [optional] 
**frequency** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_medication import TemplatebackendMedication

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendMedication from a JSON string
templatebackend_medication_instance = TemplatebackendMedication.from_json(json)
# print the JSON string representation of the object
print TemplatebackendMedication.to_json()

# convert the object into a dict
templatebackend_medication_dict = templatebackend_medication_instance.to_dict()
# create an instance of TemplatebackendMedication from a dict
templatebackend_medication_form_dict = templatebackend_medication.from_dict(templatebackend_medication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


