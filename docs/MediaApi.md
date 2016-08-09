# crowdemotion_api_client_python.MediaApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**media_get**](MediaApi.md#media_get) | **GET** /media | Find all registered Media
[**media_media_id_delete**](MediaApi.md#media_media_id_delete) | **DELETE** /media/{media_id} | Delete Media
[**media_media_id_get**](MediaApi.md#media_media_id_get) | **GET** /media/{media_id} | Find a Media
[**media_media_id_put**](MediaApi.md#media_media_id_put) | **PUT** /media/{media_id} | Update a Media
[**media_post**](MediaApi.md#media_post) | **POST** /media | Create new Media


# **media_get**
> Media media_get(skip=skip, limit=limit, where=where, sort=sort)

Find all registered Media

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
api_instance = crowdemotion_api_client_python.MediaApi()
skip = 56 # int | The number of results to skip. (optional)
limit = 56 # int | The maximum number of results to return. (optional)
where = 'where_example' # str | JSON formatted string condition. (optional)
sort = 'sort_example' # str | Attribute used to sort results. (optional)

try: 
    # Find all registered Media
    api_response = api_instance.media_get(skip=skip, limit=limit, where=where, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MediaApi->media_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| The number of results to skip. | [optional] 
 **limit** | **int**| The maximum number of results to return. | [optional] 
 **where** | **str**| JSON formatted string condition. | [optional] 
 **sort** | **str**| Attribute used to sort results. | [optional] 

### Return type

[**Media**](Media.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_media_id_delete**
> str media_media_id_delete(media_id)

Delete Media

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
api_instance = crowdemotion_api_client_python.MediaApi()
media_id = 56 # int | 

try: 
    # Delete Media
    api_response = api_instance.media_media_id_delete(media_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MediaApi->media_media_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**|  | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_media_id_get**
> list[Media] media_media_id_get(media_id, presigned_url=presigned_url)

Find a Media

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
api_instance = crowdemotion_api_client_python.MediaApi()
media_id = 56 # int | ID of Media to search.
presigned_url = true # bool | Returns the presignedUrl whose value is a signed (protected) URL to hosted video on our premises. (optional)

try: 
    # Find a Media
    api_response = api_instance.media_media_id_get(media_id, presigned_url=presigned_url)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MediaApi->media_media_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**| ID of Media to search. | 
 **presigned_url** | **bool**| Returns the presignedUrl whose value is a signed (protected) URL to hosted video on our premises. | [optional] 

### Return type

[**list[Media]**](Media.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_media_id_put**
> Media media_media_id_put(media_id, body)

Update a Media

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
api_instance = crowdemotion_api_client_python.MediaApi()
media_id = 56 # int | 
body = crowdemotion_api_client_python.MediaCreation() # MediaCreation | Request body

try: 
    # Update a Media
    api_response = api_instance.media_media_id_put(media_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MediaApi->media_media_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **int**|  | 
 **body** | [**MediaCreation**](MediaCreation.md)| Request body | 

### Return type

[**Media**](Media.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media_post**
> Media media_post(body)

Create new Media

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
api_instance = crowdemotion_api_client_python.MediaApi()
body = crowdemotion_api_client_python.MediaCreation() # MediaCreation | Request body

try: 
    # Create new Media
    api_response = api_instance.media_post(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MediaApi->media_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaCreation**](MediaCreation.md)| Request body | 

### Return type

[**Media**](Media.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

