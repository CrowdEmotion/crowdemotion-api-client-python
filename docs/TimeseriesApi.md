# crowdemotion_api_client_python.TimeseriesApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeseries_delete**](TimeseriesApi.md#timeseries_delete) | **DELETE** /timeseries | Delete a Timeseries
[**timeseries_get**](TimeseriesApi.md#timeseries_get) | **GET** /timeseries | Get all recorded timeseries for a Response


# **timeseries_delete**
> str timeseries_delete(response_id, metric_id=metric_id)

Delete a Timeseries

<p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

### Example 
```python
import time
import crowdemotion_api_client_python
from crowdemotion_api_client_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
crowdemotion_api_client_python.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# crowdemotion_api_client_python.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = crowdemotion_api_client_python.TimeseriesApi()
response_id = 56 # int | ID of the Response associated to the TimeSeries.
metric_id = 56 # int | ID of the Metric of the Timeseries to be deleted. (optional)

try: 
    # Delete a Timeseries
    api_response = api_instance.timeseries_delete(response_id, metric_id=metric_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TimeseriesApi->timeseries_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response associated to the TimeSeries. | 
 **metric_id** | **int**| ID of the Metric of the Timeseries to be deleted. | [optional] 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseries_get**
> list[Timeseries] timeseries_get(response_id, metric_id=metric_id, normalize=normalize, format=format)

Get all recorded timeseries for a Response

<p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

### Example 
```python
import time
import crowdemotion_api_client_python
from crowdemotion_api_client_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
crowdemotion_api_client_python.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# crowdemotion_api_client_python.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = crowdemotion_api_client_python.TimeseriesApi()
response_id = 56 # int | ID of the Response associated to the TimeSeries.
metric_id = 56 # int | ID of the Metric associated to the TimeSeries. (optional)
normalize = true # bool | Return data beetwen 0 and 1. Default: false. (optional)
format = 'format_example' # str | If value is 'csv' then data is passed back in CSV format insted of the default time-series format. Example: csv. (optional)

try: 
    # Get all recorded timeseries for a Response
    api_response = api_instance.timeseries_get(response_id, metric_id=metric_id, normalize=normalize, format=format)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TimeseriesApi->timeseries_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response associated to the TimeSeries. | 
 **metric_id** | **int**| ID of the Metric associated to the TimeSeries. | [optional] 
 **normalize** | **bool**| Return data beetwen 0 and 1. Default: false. | [optional] 
 **format** | **str**| If value is &#39;csv&#39; then data is passed back in CSV format insted of the default time-series format. Example: csv. | [optional] 

### Return type

[**list[Timeseries]**](Timeseries.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

