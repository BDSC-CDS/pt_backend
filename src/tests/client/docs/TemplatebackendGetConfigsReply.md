# TemplatebackendGetConfigsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**TemplatebackendGetConfigsResult**](TemplatebackendGetConfigsResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_get_configs_reply import TemplatebackendGetConfigsReply

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendGetConfigsReply from a JSON string
templatebackend_get_configs_reply_instance = TemplatebackendGetConfigsReply.from_json(json)
# print the JSON string representation of the object
print TemplatebackendGetConfigsReply.to_json()

# convert the object into a dict
templatebackend_get_configs_reply_dict = templatebackend_get_configs_reply_instance.to_dict()
# create an instance of TemplatebackendGetConfigsReply from a dict
templatebackend_get_configs_reply_form_dict = templatebackend_get_configs_reply.from_dict(templatebackend_get_configs_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


