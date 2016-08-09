# crowdemotion_api_client_python.ResearchApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**research_get**](ResearchApi.md#research_get) | **GET** /research | Find all Research
[**research_post**](ResearchApi.md#research_post) | **POST** /research | Create a Research Project
[**research_research_id_delete**](ResearchApi.md#research_research_id_delete) | **DELETE** /research/{research_id} | Delete Research Project
[**research_research_id_get**](ResearchApi.md#research_research_id_get) | **GET** /research/{research_id} | Find a Research Project
[**research_research_id_put**](ResearchApi.md#research_research_id_put) | **PUT** /research/{research_id} | Edit Research Project details


# **research_get**
> list[Research] research_get(skip=skip, limit=limit, where=where, sort=sort)

Find all Research

<p>Returns all the Research created by an admin user.</p> <p><strong>Permissions:</strong> ✓ Respondent ✗ Customer ✓ Manager</p>

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
api_instance = crowdemotion_api_client_python.ResearchApi()
skip = 56 # int | The number of results to skip. (optional)
limit = 56 # int | The maximum number of results to return. (optional)
where = 'where_example' # str | JSON formatted string condition. (optional)
sort = 'sort_example' # str | Attribute used to sort results. (optional)

try: 
    # Find all Research
    api_response = api_instance.research_get(skip=skip, limit=limit, where=where, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResearchApi->research_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| The number of results to skip. | [optional] 
 **limit** | **int**| The maximum number of results to return. | [optional] 
 **where** | **str**| JSON formatted string condition. | [optional] 
 **sort** | **str**| Attribute used to sort results. | [optional] 

### Return type

[**list[Research]**](Research.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_post**
> Research research_post(body)

Create a Research Project

<p>New research projects can only be created with an admin account.</p> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

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
api_instance = crowdemotion_api_client_python.ResearchApi()
body = crowdemotion_api_client_python.ResearchCreation() # ResearchCreation | Request body

try: 
    # Create a Research Project
    api_response = api_instance.research_post(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResearchApi->research_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResearchCreation**](ResearchCreation.md)| Request body | 

### Return type

[**Research**](Research.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_research_id_delete**
> str research_research_id_delete(research_id)

Delete Research Project

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
api_instance = crowdemotion_api_client_python.ResearchApi()
research_id = 56 # int | 

try: 
    # Delete Research Project
    api_response = api_instance.research_research_id_delete(research_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResearchApi->research_research_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **int**|  | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_research_id_get**
> Research research_research_id_get(research_id)

Find a Research Project

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
api_instance = crowdemotion_api_client_python.ResearchApi()
research_id = 56 # int | ID of Research Project to be found.

try: 
    # Find a Research Project
    api_response = api_instance.research_research_id_get(research_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResearchApi->research_research_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **int**| ID of Research Project to be found. | 

### Return type

[**Research**](Research.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **research_research_id_put**
> Research research_research_id_put(research_id, body)

Edit Research Project details

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
api_instance = crowdemotion_api_client_python.ResearchApi()
research_id = 56 # int | 
body = crowdemotion_api_client_python.ResearchCreation() # ResearchCreation | Request body

try: 
    # Edit Research Project details
    api_response = api_instance.research_research_id_put(research_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ResearchApi->research_research_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **research_id** | **int**|  | 
 **body** | [**ResearchCreation**](ResearchCreation.md)| Request body | 

### Return type

[**Research**](Research.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

