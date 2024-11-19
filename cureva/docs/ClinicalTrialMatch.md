# ClinicalTrialMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial_id** | **str** | The unique identifier of the clinical trial | 
**trial_name** | **str** | The name of the clinical trial | 
**locations** | [**List[Location]**](Location.md) |  | 
**summary** | **str** | Detailed description of the clinical trial | 
**status** | **str** | Status about the clinical trial | [optional] 

## Example

```python
from openapi_client.models.clinical_trial_match import ClinicalTrialMatch

# TODO update the JSON string below
json = "{}"
# create an instance of ClinicalTrialMatch from a JSON string
clinical_trial_match_instance = ClinicalTrialMatch.from_json(json)
# print the JSON string representation of the object
print(ClinicalTrialMatch.to_json())

# convert the object into a dict
clinical_trial_match_dict = clinical_trial_match_instance.to_dict()
# create an instance of ClinicalTrialMatch from a dict
clinical_trial_match_from_dict = ClinicalTrialMatch.from_dict(clinical_trial_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


