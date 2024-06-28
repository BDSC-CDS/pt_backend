# TemplatebackendListRepliesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replies** | [**List[TemplatebackendQuestionnaireReply]**](TemplatebackendQuestionnaireReply.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_list_replies_result import TemplatebackendListRepliesResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendListRepliesResult from a JSON string
templatebackend_list_replies_result_instance = TemplatebackendListRepliesResult.from_json(json)
# print the JSON string representation of the object
print TemplatebackendListRepliesResult.to_json()

# convert the object into a dict
templatebackend_list_replies_result_dict = templatebackend_list_replies_result_instance.to_dict()
# create an instance of TemplatebackendListRepliesResult from a dict
templatebackend_list_replies_result_form_dict = templatebackend_list_replies_result.from_dict(templatebackend_list_replies_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


