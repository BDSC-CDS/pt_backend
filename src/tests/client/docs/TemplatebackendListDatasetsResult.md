# TemplatebackendListDatasetsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | [**List[TemplatebackendDataset]**](TemplatebackendDataset.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_list_datasets_result import TemplatebackendListDatasetsResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendListDatasetsResult from a JSON string
templatebackend_list_datasets_result_instance = TemplatebackendListDatasetsResult.from_json(json)
# print the JSON string representation of the object
print TemplatebackendListDatasetsResult.to_json()

# convert the object into a dict
templatebackend_list_datasets_result_dict = templatebackend_list_datasets_result_instance.to_dict()
# create an instance of TemplatebackendListDatasetsResult from a dict
templatebackend_list_datasets_result_form_dict = templatebackend_list_datasets_result.from_dict(templatebackend_list_datasets_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


