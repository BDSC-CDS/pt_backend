# TemplatebackendCreateHelloReply


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_create_hello_reply import TemplatebackendCreateHelloReply

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendCreateHelloReply from a JSON string
templatebackend_create_hello_reply_instance = TemplatebackendCreateHelloReply.from_json(json)
# print the JSON string representation of the object
print TemplatebackendCreateHelloReply.to_json()

# convert the object into a dict
templatebackend_create_hello_reply_dict = templatebackend_create_hello_reply_instance.to_dict()
# create an instance of TemplatebackendCreateHelloReply from a dict
templatebackend_create_hello_reply_form_dict = templatebackend_create_hello_reply.from_dict(templatebackend_create_hello_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


