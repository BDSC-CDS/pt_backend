# TemplatebackendChangeTypesDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **int** |  | [optional] 
**metadata** | [**List[TemplatebackendMetadata]**](TemplatebackendMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_change_types_dataset_request import TemplatebackendChangeTypesDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendChangeTypesDatasetRequest from a JSON string
templatebackend_change_types_dataset_request_instance = TemplatebackendChangeTypesDatasetRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendChangeTypesDatasetRequest.to_json()

# convert the object into a dict
templatebackend_change_types_dataset_request_dict = templatebackend_change_types_dataset_request_instance.to_dict()
# create an instance of TemplatebackendChangeTypesDatasetRequest from a dict
templatebackend_change_types_dataset_request_form_dict = templatebackend_change_types_dataset_request.from_dict(templatebackend_change_types_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


