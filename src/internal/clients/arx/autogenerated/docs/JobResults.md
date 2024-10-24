# JobResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results_metadata** | [**Dict[str, ResultMetadata]**](ResultMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.job_results import JobResults

# TODO update the JSON string below
json = "{}"
# create an instance of JobResults from a JSON string
job_results_instance = JobResults.from_json(json)
# print the JSON string representation of the object
print JobResults.to_json()

# convert the object into a dict
job_results_dict = job_results_instance.to_dict()
# create an instance of JobResults from a dict
job_results_form_dict = job_results.from_dict(job_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


