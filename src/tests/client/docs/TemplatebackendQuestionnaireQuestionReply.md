# TemplatebackendQuestionnaireQuestionReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**questionnaire_question_id** | **int** |  | [optional] 
**answer** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_questionnaire_question_reply import TemplatebackendQuestionnaireQuestionReply

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendQuestionnaireQuestionReply from a JSON string
templatebackend_questionnaire_question_reply_instance = TemplatebackendQuestionnaireQuestionReply.from_json(json)
# print the JSON string representation of the object
print TemplatebackendQuestionnaireQuestionReply.to_json()

# convert the object into a dict
templatebackend_questionnaire_question_reply_dict = templatebackend_questionnaire_question_reply_instance.to_dict()
# create an instance of TemplatebackendQuestionnaireQuestionReply from a dict
templatebackend_questionnaire_question_reply_form_dict = templatebackend_questionnaire_question_reply.from_dict(templatebackend_questionnaire_question_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


