# TemplatebackendStoreDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_name** | **str** |  | [optional] 
**dataset** | **str** |  | [optional] 
**types** | **str** |  | [optional] 
**identifiers** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_store_dataset_request import TemplatebackendStoreDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendStoreDatasetRequest from a JSON string
templatebackend_store_dataset_request_instance = TemplatebackendStoreDatasetRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendStoreDatasetRequest.to_json()

# convert the object into a dict
templatebackend_store_dataset_request_dict = templatebackend_store_dataset_request_instance.to_dict()
# create an instance of TemplatebackendStoreDatasetRequest from a dict
templatebackend_store_dataset_request_form_dict = templatebackend_store_dataset_request.from_dict(templatebackend_store_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


