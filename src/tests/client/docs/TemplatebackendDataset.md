# TemplatebackendDataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**userid** | **int** |  | [optional] 
**tenantid** | **int** |  | [optional] 
**dataset_name** | **str** |  | [optional] 
**original_filename** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_dataset import TemplatebackendDataset

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendDataset from a JSON string
templatebackend_dataset_instance = TemplatebackendDataset.from_json(json)
# print the JSON string representation of the object
print TemplatebackendDataset.to_json()

# convert the object into a dict
templatebackend_dataset_dict = templatebackend_dataset_instance.to_dict()
# create an instance of TemplatebackendDataset from a dict
templatebackend_dataset_form_dict = templatebackend_dataset.from_dict(templatebackend_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


