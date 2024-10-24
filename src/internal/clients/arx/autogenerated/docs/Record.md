# Record


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_types** | [**AttributeTypes**](AttributeTypes.md) |  | [optional] 
**id** | **int** |  | [optional] 
**job_date** | **str** |  | [optional] 
**job_type** | **str** |  | [optional] 
**nb_columns** | **int** |  | [optional] 
**nb_rows** | **int** |  | [optional] 
**risks** | [**Risks**](Risks.md) |  | [optional] 
**statistics** | [**Statistics**](Statistics.md) |  | [optional] 

## Example

```python
from openapi_client.models.record import Record

# TODO update the JSON string below
json = "{}"
# create an instance of Record from a JSON string
record_instance = Record.from_json(json)
# print the JSON string representation of the object
print Record.to_json()

# convert the object into a dict
record_dict = record_instance.to_dict()
# create an instance of Record from a dict
record_form_dict = record.from_dict(record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


