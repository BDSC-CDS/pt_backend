# TemplatebackendCreateQuestionnaireRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**questionnaire** | [**TemplatebackendQuestionnaire**](TemplatebackendQuestionnaire.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_create_questionnaire_request import TemplatebackendCreateQuestionnaireRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendCreateQuestionnaireRequest from a JSON string
templatebackend_create_questionnaire_request_instance = TemplatebackendCreateQuestionnaireRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendCreateQuestionnaireRequest.to_json()

# convert the object into a dict
templatebackend_create_questionnaire_request_dict = templatebackend_create_questionnaire_request_instance.to_dict()
# create an instance of TemplatebackendCreateQuestionnaireRequest from a dict
templatebackend_create_questionnaire_request_form_dict = templatebackend_create_questionnaire_request.from_dict(templatebackend_create_questionnaire_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


