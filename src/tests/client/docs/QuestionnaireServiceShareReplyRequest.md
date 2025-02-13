# QuestionnaireServiceShareReplyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sharedwith_userid** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.questionnaire_service_share_reply_request import QuestionnaireServiceShareReplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionnaireServiceShareReplyRequest from a JSON string
questionnaire_service_share_reply_request_instance = QuestionnaireServiceShareReplyRequest.from_json(json)
# print the JSON string representation of the object
print QuestionnaireServiceShareReplyRequest.to_json()

# convert the object into a dict
questionnaire_service_share_reply_request_dict = questionnaire_service_share_reply_request_instance.to_dict()
# create an instance of QuestionnaireServiceShareReplyRequest from a dict
questionnaire_service_share_reply_request_form_dict = questionnaire_service_share_reply_request.from_dict(questionnaire_service_share_reply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


