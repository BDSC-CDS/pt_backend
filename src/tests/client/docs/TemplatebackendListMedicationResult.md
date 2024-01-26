# TemplatebackendListMedicationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medications** | [**List[TemplatebackendMedication]**](TemplatebackendMedication.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_list_medication_result import TemplatebackendListMedicationResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendListMedicationResult from a JSON string
templatebackend_list_medication_result_instance = TemplatebackendListMedicationResult.from_json(json)
# print the JSON string representation of the object
print TemplatebackendListMedicationResult.to_json()

# convert the object into a dict
templatebackend_list_medication_result_dict = templatebackend_list_medication_result_instance.to_dict()
# create an instance of TemplatebackendListMedicationResult from a dict
templatebackend_list_medication_result_form_dict = templatebackend_list_medication_result.from_dict(templatebackend_list_medication_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


