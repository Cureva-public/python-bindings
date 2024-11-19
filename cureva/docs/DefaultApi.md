# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_clinicalmatch_post**](DefaultApi.md#v1_clinicalmatch_post) | **POST** /v1/clinicalmatch | Submit patient notes for clinical trial matching
[**version_get**](DefaultApi.md#version_get) | **GET** /version | Get API version


# **v1_clinicalmatch_post**
> V1ClinicalmatchPost200Response v1_clinicalmatch_post(patient_notes_file, file_size_bytes, location=location)

Submit patient notes for clinical trial matching

Submits a file containing doctor notes about a patient, and a byte count for the file, to find relevant clinical trials.

### Example


```python
import openapi_client
from openapi_client.models.v1_clinicalmatch_post200_response import V1ClinicalmatchPost200Response
from openapi_client.models.v1_clinicalmatch_post_request_location import V1ClinicalmatchPostRequestLocation
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    patient_notes_file = None # bytearray | The file containing notes about the patient from the doctor visit in plain text format.
    file_size_bytes = None # bytearray | The number of bytes in the patient notes file.
    location = openapi_client.V1ClinicalmatchPostRequestLocation() # V1ClinicalmatchPostRequestLocation |  (optional)

    try:
        # Submit patient notes for clinical trial matching
        api_response = api_instance.v1_clinicalmatch_post(patient_notes_file, file_size_bytes, location=location)
        print("The response of DefaultApi->v1_clinicalmatch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_clinicalmatch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patient_notes_file** | **bytearray**| The file containing notes about the patient from the doctor visit in plain text format. | 
 **file_size_bytes** | **bytearray**| The number of bytes in the patient notes file. | 
 **location** | [**V1ClinicalmatchPostRequestLocation**](V1ClinicalmatchPostRequestLocation.md)|  | [optional] 

### Return type

[**V1ClinicalmatchPost200Response**](V1ClinicalmatchPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching clinical trials |  -  |
**400** | Invalid request format or file size mismatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version_get**
> VersionGet200Response version_get()

Get API version

Returns the version of the Clinical Match API.

### Example


```python
import openapi_client
from openapi_client.models.version_get200_response import VersionGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get API version
        api_response = api_instance.version_get()
        print("The response of DefaultApi->version_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->version_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VersionGet200Response**](VersionGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API version information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

