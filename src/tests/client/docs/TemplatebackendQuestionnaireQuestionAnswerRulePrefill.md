# TemplatebackendQuestionnaireQuestionAnswerRulePrefill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**question_id** | **int** |  | [optional] 
**answer_id** | **int** |  | [optional] 
**answer_text** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_questionnaire_question_answer_rule_prefill import TemplatebackendQuestionnaireQuestionAnswerRulePrefill

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendQuestionnaireQuestionAnswerRulePrefill from a JSON string
templatebackend_questionnaire_question_answer_rule_prefill_instance = TemplatebackendQuestionnaireQuestionAnswerRulePrefill.from_json(json)
# print the JSON string representation of the object
print TemplatebackendQuestionnaireQuestionAnswerRulePrefill.to_json()

# convert the object into a dict
templatebackend_questionnaire_question_answer_rule_prefill_dict = templatebackend_questionnaire_question_answer_rule_prefill_instance.to_dict()
# create an instance of TemplatebackendQuestionnaireQuestionAnswerRulePrefill from a dict
templatebackend_questionnaire_question_answer_rule_prefill_form_dict = templatebackend_questionnaire_question_answer_rule_prefill.from_dict(templatebackend_questionnaire_question_answer_rule_prefill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


