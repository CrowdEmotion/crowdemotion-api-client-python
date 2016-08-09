# crowdemotion_api_client_python.UserApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_id_get**](UserApi.md#user_id_get) | **GET** /user/{id} | Get User information
[**user_id_put**](UserApi.md#user_id_put) | **PUT** /user/{id} | Edit User information
[**user_login_post**](UserApi.md#user_login_post) | **POST** /user/login | User Login
[**user_user_id_metadata_get**](UserApi.md#user_user_id_metadata_get) | **GET** /user/{user_id}/metadata | Find User metadata
[**user_user_id_metadata_post**](UserApi.md#user_user_id_metadata_post) | **POST** /user/{user_id}/metadata | Add user metadata


# **user_id_get**
> User user_id_get(id)

Get User information

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
api_instance = crowdemotion_api_client_python.UserApi()
id = 56 # int | User unique ID

try: 
    # Get User information
    api_response = api_instance.user_id_get(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_id_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User unique ID | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_id_put**
> User user_id_put(id, body)

Edit User information

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
api_instance = crowdemotion_api_client_python.UserApi()
id = 'id_example' # str | ID of User to update.
body = crowdemotion_api_client_python.UserUpdateBody() # UserUpdateBody | Request body

try: 
    # Edit User information
    api_response = api_instance.user_id_put(id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_id_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of User to update. | 
 **body** | [**UserUpdateBody**](UserUpdateBody.md)| Request body | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_login_post**
> LoginResponse user_login_post(body)

User Login

<p><strong>Permissions:</strong> No authorization is required</p>

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
api_instance = crowdemotion_api_client_python.UserApi()
body = crowdemotion_api_client_python.Login() # Login | Request body

try: 
    # User Login
    api_response = api_instance.user_login_post(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_login_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Login**](Login.md)| Request body | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_metadata_get**
> UserMetadataResponse user_user_id_metadata_get(user_id)

Find User metadata

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
api_instance = crowdemotion_api_client_python.UserApi()
user_id = 56 # int | ID of User.

try: 
    # Find User metadata
    api_response = api_instance.user_user_id_metadata_get(user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_user_id_metadata_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of User. | 

### Return type

[**UserMetadataResponse**](UserMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_id_metadata_post**
> UserMetadataResponse user_user_id_metadata_post(user_id, body)

Add user metadata

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
api_instance = crowdemotion_api_client_python.UserApi()
user_id = 56 # int | ID of User.
body = crowdemotion_api_client_python.UserMetadata() # UserMetadata | Request body

try: 
    # Add user metadata
    api_response = api_instance.user_user_id_metadata_post(user_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->user_user_id_metadata_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of User. | 
 **body** | [**UserMetadata**](UserMetadata.md)| Request body | 

### Return type

[**UserMetadataResponse**](UserMetadataResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

