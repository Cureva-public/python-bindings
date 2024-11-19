# V1ClinicalmatchPostRequestLocation

The geographic location of the patient encounter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude of the location. | 
**longitude** | **float** | The longitude of the location. | 

## Example

```python
from openapi_client.models.v1_clinicalmatch_post_request_location import V1ClinicalmatchPostRequestLocation

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClinicalmatchPostRequestLocation from a JSON string
v1_clinicalmatch_post_request_location_instance = V1ClinicalmatchPostRequestLocation.from_json(json)
# print the JSON string representation of the object
print(V1ClinicalmatchPostRequestLocation.to_json())

# convert the object into a dict
v1_clinicalmatch_post_request_location_dict = v1_clinicalmatch_post_request_location_instance.to_dict()
# create an instance of V1ClinicalmatchPostRequestLocation from a dict
v1_clinicalmatch_post_request_location_from_dict = V1ClinicalmatchPostRequestLocation.from_dict(v1_clinicalmatch_post_request_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


