# TemplatebackendSearchUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_like** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_search_users_request import TemplatebackendSearchUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendSearchUsersRequest from a JSON string
templatebackend_search_users_request_instance = TemplatebackendSearchUsersRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendSearchUsersRequest.to_json()

# convert the object into a dict
templatebackend_search_users_request_dict = templatebackend_search_users_request_instance.to_dict()
# create an instance of TemplatebackendSearchUsersRequest from a dict
templatebackend_search_users_request_form_dict = templatebackend_search_users_request.from_dict(templatebackend_search_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


