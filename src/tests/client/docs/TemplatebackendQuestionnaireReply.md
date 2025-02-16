# TemplatebackendQuestionnaireReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**questionnaire_version_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**replies** | [**List[TemplatebackendQuestionnaireQuestionReply]**](TemplatebackendQuestionnaireQuestionReply.md) |  | [optional] 
**user_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_questionnaire_reply import TemplatebackendQuestionnaireReply

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendQuestionnaireReply from a JSON string
templatebackend_questionnaire_reply_instance = TemplatebackendQuestionnaireReply.from_json(json)
# print the JSON string representation of the object
print TemplatebackendQuestionnaireReply.to_json()

# convert the object into a dict
templatebackend_questionnaire_reply_dict = templatebackend_questionnaire_reply_instance.to_dict()
# create an instance of TemplatebackendQuestionnaireReply from a dict
templatebackend_questionnaire_reply_form_dict = templatebackend_questionnaire_reply.from_dict(templatebackend_questionnaire_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


