# IndexServiceCreateHelloRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.index_service_create_hello_request import IndexServiceCreateHelloRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IndexServiceCreateHelloRequest from a JSON string
index_service_create_hello_request_instance = IndexServiceCreateHelloRequest.from_json(json)
# print the JSON string representation of the object
print IndexServiceCreateHelloRequest.to_json()

# convert the object into a dict
index_service_create_hello_request_dict = index_service_create_hello_request_instance.to_dict()
# create an instance of IndexServiceCreateHelloRequest from a dict
index_service_create_hello_request_form_dict = index_service_create_hello_request.from_dict(index_service_create_hello_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


