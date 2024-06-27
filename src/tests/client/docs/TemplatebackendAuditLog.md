# TemplatebackendAuditLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**userid** | **int** |  | [optional] 
**service** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**response** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**error** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_audit_log import TemplatebackendAuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendAuditLog from a JSON string
templatebackend_audit_log_instance = TemplatebackendAuditLog.from_json(json)
# print the JSON string representation of the object
print TemplatebackendAuditLog.to_json()

# convert the object into a dict
templatebackend_audit_log_dict = templatebackend_audit_log_instance.to_dict()
# create an instance of TemplatebackendAuditLog from a dict
templatebackend_audit_log_form_dict = templatebackend_audit_log.from_dict(templatebackend_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


