# TemplatebackendCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**totp** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_credentials import TemplatebackendCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendCredentials from a JSON string
templatebackend_credentials_instance = TemplatebackendCredentials.from_json(json)
# print the JSON string representation of the object
print TemplatebackendCredentials.to_json()

# convert the object into a dict
templatebackend_credentials_dict = templatebackend_credentials_instance.to_dict()
# create an instance of TemplatebackendCredentials from a dict
templatebackend_credentials_form_dict = templatebackend_credentials.from_dict(templatebackend_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


