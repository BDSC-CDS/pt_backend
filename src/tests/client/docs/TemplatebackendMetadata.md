# TemplatebackendMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userid** | **int** |  | [optional] 
**tenantid** | **int** |  | [optional] 
**dataset_id** | **int** |  | [optional] 
**column_id** | **int** |  | [optional] 
**column_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_metadata import TemplatebackendMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendMetadata from a JSON string
templatebackend_metadata_instance = TemplatebackendMetadata.from_json(json)
# print the JSON string representation of the object
print TemplatebackendMetadata.to_json()

# convert the object into a dict
templatebackend_metadata_dict = templatebackend_metadata_instance.to_dict()
# create an instance of TemplatebackendMetadata from a dict
templatebackend_metadata_form_dict = templatebackend_metadata.from_dict(templatebackend_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


