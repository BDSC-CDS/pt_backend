# TemplatebackendQuestionnaire


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**reply_editable** | **bool** |  | [optional] 
**versions** | [**List[TemplatebackendQuestionnaireVersion]**](TemplatebackendQuestionnaireVersion.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_questionnaire import TemplatebackendQuestionnaire

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendQuestionnaire from a JSON string
templatebackend_questionnaire_instance = TemplatebackendQuestionnaire.from_json(json)
# print the JSON string representation of the object
print TemplatebackendQuestionnaire.to_json()

# convert the object into a dict
templatebackend_questionnaire_dict = templatebackend_questionnaire_instance.to_dict()
# create an instance of TemplatebackendQuestionnaire from a dict
templatebackend_questionnaire_form_dict = templatebackend_questionnaire.from_dict(templatebackend_questionnaire_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


