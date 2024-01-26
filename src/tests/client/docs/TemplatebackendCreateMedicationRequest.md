# TemplatebackendCreateMedicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medication** | [**TemplatebackendMedication**](TemplatebackendMedication.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_create_medication_request import TemplatebackendCreateMedicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendCreateMedicationRequest from a JSON string
templatebackend_create_medication_request_instance = TemplatebackendCreateMedicationRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendCreateMedicationRequest.to_json()

# convert the object into a dict
templatebackend_create_medication_request_dict = templatebackend_create_medication_request_instance.to_dict()
# create an instance of TemplatebackendCreateMedicationRequest from a dict
templatebackend_create_medication_request_form_dict = templatebackend_create_medication_request.from_dict(templatebackend_create_medication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


