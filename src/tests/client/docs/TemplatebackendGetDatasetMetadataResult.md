# TemplatebackendGetDatasetMetadataResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[TemplatebackendMetadata]**](TemplatebackendMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_get_dataset_metadata_result import TemplatebackendGetDatasetMetadataResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendGetDatasetMetadataResult from a JSON string
templatebackend_get_dataset_metadata_result_instance = TemplatebackendGetDatasetMetadataResult.from_json(json)
# print the JSON string representation of the object
print TemplatebackendGetDatasetMetadataResult.to_json()

# convert the object into a dict
templatebackend_get_dataset_metadata_result_dict = templatebackend_get_dataset_metadata_result_instance.to_dict()
# create an instance of TemplatebackendGetDatasetMetadataResult from a dict
templatebackend_get_dataset_metadata_result_form_dict = templatebackend_get_dataset_metadata_result.from_dict(templatebackend_get_dataset_metadata_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


