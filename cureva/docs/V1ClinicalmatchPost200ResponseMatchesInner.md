# V1ClinicalmatchPost200ResponseMatchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial_id** | **str** | The ID of the matched clinical trial | [optional] 
**trial_name** | **str** | The name of the clinical trial | [optional] 
**locations** | [**List[Location]**](Location.md) |  | [optional] 
**summary** | **str** | Detailed description of the clinical trial | [optional] 
**status** | **str** | Status about the clinical trial | [optional] 

## Example

```python
from openapi_client.models.v1_clinicalmatch_post200_response_matches_inner import V1ClinicalmatchPost200ResponseMatchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClinicalmatchPost200ResponseMatchesInner from a JSON string
v1_clinicalmatch_post200_response_matches_inner_instance = V1ClinicalmatchPost200ResponseMatchesInner.from_json(json)
# print the JSON string representation of the object
print(V1ClinicalmatchPost200ResponseMatchesInner.to_json())

# convert the object into a dict
v1_clinicalmatch_post200_response_matches_inner_dict = v1_clinicalmatch_post200_response_matches_inner_instance.to_dict()
# create an instance of V1ClinicalmatchPost200ResponseMatchesInner from a dict
v1_clinicalmatch_post200_response_matches_inner_from_dict = V1ClinicalmatchPost200ResponseMatchesInner.from_dict(v1_clinicalmatch_post200_response_matches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


