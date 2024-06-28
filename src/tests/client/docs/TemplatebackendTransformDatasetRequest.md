# TemplatebackendTransformDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **int** |  | [optional] 
**config_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_transform_dataset_request import TemplatebackendTransformDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendTransformDatasetRequest from a JSON string
templatebackend_transform_dataset_request_instance = TemplatebackendTransformDatasetRequest.from_json(json)
# print the JSON string representation of the object
print TemplatebackendTransformDatasetRequest.to_json()

# convert the object into a dict
templatebackend_transform_dataset_request_dict = templatebackend_transform_dataset_request_instance.to_dict()
# create an instance of TemplatebackendTransformDatasetRequest from a dict
templatebackend_transform_dataset_request_form_dict = templatebackend_transform_dataset_request.from_dict(templatebackend_transform_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


