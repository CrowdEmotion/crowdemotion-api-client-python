# crowdemotion_api_client_python.ResponseApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**response_get**](ResponseApi.md#response_get) | **GET** /response | Find all Responses
[**response_post**](ResponseApi.md#response_post) | **POST** /response | Create a Response
[**response_response_id_delete**](ResponseApi.md#response_response_id_delete) | **DELETE** /response/{response_id} | Delete a Response
[**response_response_id_get**](ResponseApi.md#response_response_id_get) | **GET** /response/{response_id} | Find a Response
[**response_response_id_metadata_get**](ResponseApi.md#response_response_id_metadata_get) | **GET** /response/{response_id}/metadata | Show Response Metadata
[**response_response_id_metadata_post**](ResponseApi.md#response_response_id_metadata_post) | **POST** /response/{response_id}/metadata | Add Response Metadata
[**response_response_id_put**](ResponseApi.md#response_response_id_put) | **PUT** /response/{response_id} | Update a Response


# **response_get**
> list[Response] response_get(skip=skip, limit=limit, where=where, sort=sort)

Find all Responses

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
api_instance = crowdemotion_api_client_python.ResponseApi()
skip = 56 # int | The number of results to skip. (optional)
limit = 56 # int | The maximum number of results to return. (optional)
where = 'where_example' # str | JSON formatted string. (optional)
sort = 'sort_example' # str | Attribute used to sort results. (optional)

try: 
    # Find all Responses
    api_response = api_instance.response_get(skip=skip, limit=limit, where=where, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseApi->response_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| The number of results to skip. | [optional] 
 **limit** | **int**| The maximum number of results to return. | [optional] 
 **where** | **str**| JSON formatted string. | [optional] 
 **sort** | **str**| Attribute used to sort results. | [optional] 

### Return type

[**list[Response]**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **response_post**
> Response response_post(body)

Create a Response

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
api_instance = crowdemotion_api_client_python.ResponseApi()
body = crowdemotion_api_client_python.ResponseCreation() # ResponseCreation | Request body

try: 
    # Create a Response
    api_response = api_instance.response_post(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseApi->response_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResponseCreation**](ResponseCreation.md)| Request body | 

### Return type

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **response_response_id_delete**
> str response_response_id_delete(response_id)

Delete a Response

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
api_instance = crowdemotion_api_client_python.ResponseApi()
response_id = 56 # int | ID of Response to update.

try: 
    # Delete a Response
    api_response = api_instance.response_response_id_delete(response_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseApi->response_response_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of Response to update. | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **response_response_id_get**
> Response response_response_id_get(response_id)

Find a Response

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
api_instance = crowdemotion_api_client_python.ResponseApi()
response_id = 56 # int | ID of the Response

try: 
    # Find a Response
    api_response = api_instance.response_response_id_get(response_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseApi->response_response_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response | 

### Return type

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **response_response_id_metadata_get**
> ResponseMetadataResponse response_response_id_metadata_get(response_id)

Show Response Metadata

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
api_instance = crowdemotion_api_client_python.ResponseApi()
response_id = 56 # int | ID of the Response

try: 
    # Show Response Metadata
    api_response = api_instance.response_response_id_metadata_get(response_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseApi->response_response_id_metadata_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response | 

### Return type

[**ResponseMetadataResponse**](ResponseMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **response_response_id_metadata_post**
> ResponseMetadataResponse response_response_id_metadata_post(response_id, body)

Add Response Metadata

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
api_instance = crowdemotion_api_client_python.ResponseApi()
response_id = 56 # int | ID of the Response.
body = crowdemotion_api_client_python.ResponseMetadata() # ResponseMetadata | Request body

try: 
    # Add Response Metadata
    api_response = api_instance.response_response_id_metadata_post(response_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseApi->response_response_id_metadata_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of the Response. | 
 **body** | [**ResponseMetadata**](ResponseMetadata.md)| Request body | 

### Return type

[**ResponseMetadataResponse**](ResponseMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **response_response_id_put**
> Response response_response_id_put(response_id, body)

Update a Response

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
api_instance = crowdemotion_api_client_python.ResponseApi()
response_id = 56 # int | ID of Response to update.
body = crowdemotion_api_client_python.ResponseCreation() # ResponseCreation | Request body

try: 
    # Update a Response
    api_response = api_instance.response_response_id_put(response_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResponseApi->response_response_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | **int**| ID of Response to update. | 
 **body** | [**ResponseCreation**](ResponseCreation.md)| Request body | 

### Return type

[**Response**](Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

