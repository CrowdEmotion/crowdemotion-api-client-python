# crowdemotion_api_client_python.RespondentApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**respondent_get**](RespondentApi.md#respondent_get) | **GET** /respondent | Find all Respondents of a Research
[**respondent_post**](RespondentApi.md#respondent_post) | **POST** /respondent | Create a Respondent
[**respondent_respondent_id_delete**](RespondentApi.md#respondent_respondent_id_delete) | **DELETE** /respondent/{respondent_id} | Delete a Respondent
[**respondent_respondent_id_get**](RespondentApi.md#respondent_respondent_id_get) | **GET** /respondent/{respondent_id} | Find a Respondent
[**respondent_respondent_id_metadata_get**](RespondentApi.md#respondent_respondent_id_metadata_get) | **GET** /respondent/{respondent_id}/metadata | Find Respondent Metadata
[**respondent_respondent_id_metadata_post**](RespondentApi.md#respondent_respondent_id_metadata_post) | **POST** /respondent/{respondent_id}/metadata | Add Respondent Metadata
[**respondent_respondent_id_put**](RespondentApi.md#respondent_respondent_id_put) | **PUT** /respondent/{respondent_id} | Update a Respondent


# **respondent_get**
> list[Respondent] respondent_get(research_id, skip=skip, limit=limit, where=where, sort=sort)

Find all Respondents of a Research

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
api_instance = crowdemotion_api_client_python.RespondentApi()
research_id = 56 # int | Search by research id.
skip = 56 # int | The number of results to skip. (optional)
limit = 56 # int | The maximum number of results to return. (optional)
where = 'where_example' # str | JSON formatted string. (optional)
sort = 'sort_example' # str | Attribute used to sort results. (optional)

try: 
    # Find all Respondents of a Research
    api_response = api_instance.respondent_get(research_id, skip=skip, limit=limit, where=where, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RespondentApi->respondent_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **int**| Search by research id. | 
 **skip** | **int**| The number of results to skip. | [optional] 
 **limit** | **int**| The maximum number of results to return. | [optional] 
 **where** | **str**| JSON formatted string. | [optional] 
 **sort** | **str**| Attribute used to sort results. | [optional] 

### Return type

[**list[Respondent]**](Respondent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respondent_post**
> Respondent respondent_post(body)

Create a Respondent

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
api_instance = crowdemotion_api_client_python.RespondentApi()
body = crowdemotion_api_client_python.Respondent() # Respondent | Request body

try: 
    # Create a Respondent
    api_response = api_instance.respondent_post(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RespondentApi->respondent_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Respondent**](Respondent.md)| Request body | 

### Return type

[**Respondent**](Respondent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respondent_respondent_id_delete**
> str respondent_respondent_id_delete(respondent_id)

Delete a Respondent

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
api_instance = crowdemotion_api_client_python.RespondentApi()
respondent_id = 56 # int | 

try: 
    # Delete a Respondent
    api_response = api_instance.respondent_respondent_id_delete(respondent_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RespondentApi->respondent_respondent_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**|  | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respondent_respondent_id_get**
> Respondent respondent_respondent_id_get(respondent_id)

Find a Respondent

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
api_instance = crowdemotion_api_client_python.RespondentApi()
respondent_id = 56 # int | Search by research id.

try: 
    # Find a Respondent
    api_response = api_instance.respondent_respondent_id_get(respondent_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RespondentApi->respondent_respondent_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**| Search by research id. | 

### Return type

[**Respondent**](Respondent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respondent_respondent_id_metadata_get**
> RespondentMetadataResponse respondent_respondent_id_metadata_get(respondent_id)

Find Respondent Metadata

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
api_instance = crowdemotion_api_client_python.RespondentApi()
respondent_id = 56 # int | ID of the Respondent

try: 
    # Find Respondent Metadata
    api_response = api_instance.respondent_respondent_id_metadata_get(respondent_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RespondentApi->respondent_respondent_id_metadata_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**| ID of the Respondent | 

### Return type

[**RespondentMetadataResponse**](RespondentMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respondent_respondent_id_metadata_post**
> RespondentMetadataResponse respondent_respondent_id_metadata_post(respondent_id, body)

Add Respondent Metadata

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
api_instance = crowdemotion_api_client_python.RespondentApi()
respondent_id = 56 # int | 
body = crowdemotion_api_client_python.RespondentMetadata() # RespondentMetadata | Request body

try: 
    # Add Respondent Metadata
    api_response = api_instance.respondent_respondent_id_metadata_post(respondent_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RespondentApi->respondent_respondent_id_metadata_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**|  | 
 **body** | [**RespondentMetadata**](RespondentMetadata.md)| Request body | 

### Return type

[**RespondentMetadataResponse**](RespondentMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respondent_respondent_id_put**
> Respondent respondent_respondent_id_put(respondent_id, body)

Update a Respondent

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
api_instance = crowdemotion_api_client_python.RespondentApi()
respondent_id = 56 # int | 
body = crowdemotion_api_client_python.Respondent() # Respondent | Request body

try: 
    # Update a Respondent
    api_response = api_instance.respondent_respondent_id_put(respondent_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RespondentApi->respondent_respondent_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **respondent_id** | **int**|  | 
 **body** | [**Respondent**](Respondent.md)| Request body | 

### Return type

[**Respondent**](Respondent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

