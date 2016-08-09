# crowdemotion_api_client_python.MetricApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metric_get**](MetricApi.md#metric_get) | **GET** /metric | List all registered metrics
[**metric_metric_id_delete**](MetricApi.md#metric_metric_id_delete) | **DELETE** /metric/{metric_id} | Delete a Metric
[**metric_metric_id_get**](MetricApi.md#metric_metric_id_get) | **GET** /metric/{metric_id} | Find a Metric
[**metric_post**](MetricApi.md#metric_post) | **POST** /metric | Create Metric


# **metric_get**
> list[Metric] metric_get(skip=skip, limit=limit, where=where, sort=sort)

List all registered metrics

<p>Metrics are linked to time-series and define their meaning.</p> <p>Common metric ID are listed below:</p> <table>   <tr><td>id</td><td>Value</td></tr>   <tr><td>1</td><td>Timestamp</td></tr>   <tr><td>2</td><td>Neutral</td></tr>   <tr><td>3</td><td>Happiness</td></tr>   <tr><td>4</td><td>Surprise</td></tr>   <tr><td>5</td><td>Puzzlement</td></tr>   <tr><td>6</td><td>Disgust</td></tr>   <tr><td>7</td><td>Fear</td></tr>   <tr><td>8</td><td>Sadness</td></tr> </table> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

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
api_instance = crowdemotion_api_client_python.MetricApi()
skip = 56 # int | The number of results to skip. (optional)
limit = 56 # int | The maximum number of results to return. (optional)
where = 'where_example' # str | JSON formatted string condition. (optional)
sort = 'sort_example' # str | Attribute used to sort results. (optional)

try: 
    # List all registered metrics
    api_response = api_instance.metric_get(skip=skip, limit=limit, where=where, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MetricApi->metric_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| The number of results to skip. | [optional] 
 **limit** | **int**| The maximum number of results to return. | [optional] 
 **where** | **str**| JSON formatted string condition. | [optional] 
 **sort** | **str**| Attribute used to sort results. | [optional] 

### Return type

[**list[Metric]**](Metric.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_metric_id_delete**
> Metric metric_metric_id_delete(metric_id)

Delete a Metric

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
api_instance = crowdemotion_api_client_python.MetricApi()
metric_id = 56 # int | ID of Metric to be deleted.

try: 
    # Delete a Metric
    api_response = api_instance.metric_metric_id_delete(metric_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MetricApi->metric_metric_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **int**| ID of Metric to be deleted. | 

### Return type

[**Metric**](Metric.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_metric_id_get**
> Metric metric_metric_id_get(metric_id)

Find a Metric

<p>Metrics are linked to time-series and define their meaning.</p> <p>Common metric ID are listed below:</p> <table>   <tr><td>id</td><td>Value</td></tr>   <tr><td>1</td><td>Timestamp</td></tr>   <tr><td>2</td><td>Neutral</td></tr>   <tr><td>3</td><td>Happiness</td></tr>   <tr><td>4</td><td>Surprise</td></tr>   <tr><td>5</td><td>Puzzlement</td></tr>   <tr><td>6</td><td>Disgust</td></tr>   <tr><td>7</td><td>Fear</td></tr>   <tr><td>8</td><td>Sadness</td></tr> </table> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

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
api_instance = crowdemotion_api_client_python.MetricApi()
metric_id = 56 # int | ID of Metric to find.

try: 
    # Find a Metric
    api_response = api_instance.metric_metric_id_get(metric_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MetricApi->metric_metric_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **int**| ID of Metric to find. | 

### Return type

[**Metric**](Metric.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metric_post**
> Metric metric_post(body)

Create Metric

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
api_instance = crowdemotion_api_client_python.MetricApi()
body = crowdemotion_api_client_python.MetricCreation() # MetricCreation | Request body

try: 
    # Create Metric
    api_response = api_instance.metric_post(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MetricApi->metric_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetricCreation**](MetricCreation.md)| Request body | 

### Return type

[**Metric**](Metric.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

