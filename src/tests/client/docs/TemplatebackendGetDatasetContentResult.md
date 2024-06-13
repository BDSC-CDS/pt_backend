# TemplatebackendGetDatasetContentResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[TemplatebackendColumn]**](TemplatebackendColumn.md) |  | [optional] 

## Example

```python
from openapi_client.models.templatebackend_get_dataset_content_result import TemplatebackendGetDatasetContentResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatebackendGetDatasetContentResult from a JSON string
templatebackend_get_dataset_content_result_instance = TemplatebackendGetDatasetContentResult.from_json(json)
# print the JSON string representation of the object
print TemplatebackendGetDatasetContentResult.to_json()

# convert the object into a dict
templatebackend_get_dataset_content_result_dict = templatebackend_get_dataset_content_result_instance.to_dict()
# create an instance of TemplatebackendGetDatasetContentResult from a dict
templatebackend_get_dataset_content_result_form_dict = templatebackend_get_dataset_content_result.from_dict(templatebackend_get_dataset_content_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


