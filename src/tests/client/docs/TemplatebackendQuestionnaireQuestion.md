# TemplatebackendQuestionnaireQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**tab** | **str** |  | [optional] 
**question** | **str** |  | [optional] 
**risk_weight** | **int** |  | [optional] 
**answer_type** | **str** |  | [optional] 
**flag** | **str** |  | [optional] 
**tooltip** | **str** |  | [optional] 
**answers** | [**List[TemplatebackendQuestionnaireQuestionAnswer]**](TemplatebackendQuestionnaireQuestionAnswer.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_questionnaire_question import TemplatebackendQuestionnaireQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendQuestionnaireQuestion from a JSON string
templatebackend_questionnaire_question_instance = TemplatebackendQuestionnaireQuestion.from_json(json)
# print the JSON string representation of the object
print TemplatebackendQuestionnaireQuestion.to_json()

# convert the object into a dict
templatebackend_questionnaire_question_dict = templatebackend_questionnaire_question_instance.to_dict()
# create an instance of TemplatebackendQuestionnaireQuestion from a dict
templatebackend_questionnaire_question_form_dict = templatebackend_questionnaire_question.from_dict(templatebackend_questionnaire_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


