# TemplatebackendCreateMedicationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TemplatebackendCreateMedicationResult**](TemplatebackendCreateMedicationResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_create_medication_reply import TemplatebackendCreateMedicationReply

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendCreateMedicationReply from a JSON string
templatebackend_create_medication_reply_instance = TemplatebackendCreateMedicationReply.from_json(json)
# print the JSON string representation of the object
print TemplatebackendCreateMedicationReply.to_json()

# convert the object into a dict
templatebackend_create_medication_reply_dict = templatebackend_create_medication_reply_instance.to_dict()
# create an instance of TemplatebackendCreateMedicationReply from a dict
templatebackend_create_medication_reply_form_dict = templatebackend_create_medication_reply.from_dict(templatebackend_create_medication_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


