# TemplatebackendQuestionnaireQuestionAnswer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**text** | **str** |  | [optional] 
**risk_level** | **int** |  | [optional] 
**high_risk** | **bool** |  | [optional] 
**rule_prefills** | [**List[TemplatebackendQuestionnaireQuestionAnswerRulePrefill]**](TemplatebackendQuestionnaireQuestionAnswerRulePrefill.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_questionnaire_question_answer import TemplatebackendQuestionnaireQuestionAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendQuestionnaireQuestionAnswer from a JSON string
templatebackend_questionnaire_question_answer_instance = TemplatebackendQuestionnaireQuestionAnswer.from_json(json)
# print the JSON string representation of the object
print TemplatebackendQuestionnaireQuestionAnswer.to_json()

# convert the object into a dict
templatebackend_questionnaire_question_answer_dict = templatebackend_questionnaire_question_answer_instance.to_dict()
# create an instance of TemplatebackendQuestionnaireQuestionAnswer from a dict
templatebackend_questionnaire_question_answer_form_dict = templatebackend_questionnaire_question_answer.from_dict(templatebackend_questionnaire_question_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


