# TemplatebackendListQuestionnaireResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**questionnaires** | [**List[TemplatebackendQuestionnaire]**](TemplatebackendQuestionnaire.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_list_questionnaire_result import TemplatebackendListQuestionnaireResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendListQuestionnaireResult from a JSON string
templatebackend_list_questionnaire_result_instance = TemplatebackendListQuestionnaireResult.from_json(json)
# print the JSON string representation of the object
print TemplatebackendListQuestionnaireResult.to_json()

# convert the object into a dict
templatebackend_list_questionnaire_result_dict = templatebackend_list_questionnaire_result_instance.to_dict()
# create an instance of TemplatebackendListQuestionnaireResult from a dict
templatebackend_list_questionnaire_result_form_dict = templatebackend_list_questionnaire_result.from_dict(templatebackend_list_questionnaire_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


