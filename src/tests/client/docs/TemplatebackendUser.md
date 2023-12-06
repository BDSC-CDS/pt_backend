# TemplatebackendUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**totp_enabled** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**password_changed** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_user import TemplatebackendUser

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendUser from a JSON string
templatebackend_user_instance = TemplatebackendUser.from_json(json)
# print the JSON string representation of the object
print TemplatebackendUser.to_json()

# convert the object into a dict
templatebackend_user_dict = templatebackend_user_instance.to_dict()
# create an instance of TemplatebackendUser from a dict
templatebackend_user_form_dict = templatebackend_user.from_dict(templatebackend_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


