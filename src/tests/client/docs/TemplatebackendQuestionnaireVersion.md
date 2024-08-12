# TemplatebackendQuestionnaireVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**questions** | [**List[TemplatebackendQuestionnaireQuestion]**](TemplatebackendQuestionnaireQuestion.md) |  | [optional] 
**published** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_questionnaire_version import TemplatebackendQuestionnaireVersion

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendQuestionnaireVersion from a JSON string
templatebackend_questionnaire_version_instance = TemplatebackendQuestionnaireVersion.from_json(json)
# print the JSON string representation of the object
print TemplatebackendQuestionnaireVersion.to_json()

# convert the object into a dict
templatebackend_questionnaire_version_dict = templatebackend_questionnaire_version_instance.to_dict()
# create an instance of TemplatebackendQuestionnaireVersion from a dict
templatebackend_questionnaire_version_form_dict = templatebackend_questionnaire_version.from_dict(templatebackend_questionnaire_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


