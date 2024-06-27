# V1AuditLog

The audit log message.

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
from openapi_client.models.v1_audit_log import V1AuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of V1AuditLog from a JSON string
v1_audit_log_instance = V1AuditLog.from_json(json)
# print the JSON string representation of the object
print V1AuditLog.to_json()

# convert the object into a dict
v1_audit_log_dict = v1_audit_log_instance.to_dict()
# create an instance of V1AuditLog from a dict
v1_audit_log_form_dict = v1_audit_log.from_dict(v1_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


