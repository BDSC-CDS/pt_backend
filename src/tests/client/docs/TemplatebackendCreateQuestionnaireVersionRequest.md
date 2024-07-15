# TemplatebackendCreateQuestionnaireVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**version** | [**TemplatebackendQuestionnaireVersion**](TemplatebackendQuestionnaireVersion.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_create_questionnaire_version_request import TemplatebackendCreateQuestionnaireVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendCreateQuestionnaireVersionRequest from a JSON string
templatebackend_create_questionnaire_version_request_instance = TemplatebackendCreateQuestionnaireVersionRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendCreateQuestionnaireVersionRequest.to_json()

# convert the object into a dict
templatebackend_create_questionnaire_version_request_dict = templatebackend_create_questionnaire_version_request_instance.to_dict()
# create an instance of TemplatebackendCreateQuestionnaireVersionRequest from a dict
templatebackend_create_questionnaire_version_request_form_dict = templatebackend_create_questionnaire_version_request.from_dict(templatebackend_create_questionnaire_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


