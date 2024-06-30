# TemplatebackendCreateReplyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply** | [**TemplatebackendQuestionnaireReply**](TemplatebackendQuestionnaireReply.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_create_reply_request import TemplatebackendCreateReplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendCreateReplyRequest from a JSON string
templatebackend_create_reply_request_instance = TemplatebackendCreateReplyRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendCreateReplyRequest.to_json()

# convert the object into a dict
templatebackend_create_reply_request_dict = templatebackend_create_reply_request_instance.to_dict()
# create an instance of TemplatebackendCreateReplyRequest from a dict
templatebackend_create_reply_request_form_dict = templatebackend_create_reply_request.from_dict(templatebackend_create_reply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


