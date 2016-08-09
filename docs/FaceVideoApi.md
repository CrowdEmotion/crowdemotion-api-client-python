# crowdemotion_api_client_python.FaceVideoApi

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facevideo_facevideo_id_delete**](FaceVideoApi.md#facevideo_facevideo_id_delete) | **DELETE** /facevideo/{facevideo_id} | Delete a FaceVideo
[**facevideo_get**](FaceVideoApi.md#facevideo_get) | **GET** /facevideo | Find a FaceVideo
[**facevideo_post**](FaceVideoApi.md#facevideo_post) | **POST** /facevideo | Analyse FaceVideo
[**facevideo_put**](FaceVideoApi.md#facevideo_put) | **PUT** /facevideo | Analyse FaceVideo


# **facevideo_facevideo_id_delete**
> str facevideo_facevideo_id_delete(facevideo_id)

Delete a FaceVideo

<p>Use this operation to delete a FaceVideo.</p> <p><strong>Permissions:</strong> ✗ Respondent ✗ Customer ✓ Manager</p>

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
api_instance = crowdemotion_api_client_python.FaceVideoApi()
facevideo_id = 56 # int | ID of FaceVideo to be deleted.

try: 
    # Delete a FaceVideo
    api_response = api_instance.facevideo_facevideo_id_delete(facevideo_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FaceVideoApi->facevideo_facevideo_id_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facevideo_id** | **int**| ID of FaceVideo to be deleted. | 

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facevideo_get**
> FaceVideo facevideo_get(facevideo_id=facevideo_id, response_id=response_id)

Find a FaceVideo

<p>Use this operation to access information about the FaceVideo analysis.</p> <p><i>Any one of the two parameters must be specified.</i></p> <p>To discover if the video has been analyzed, check the meaning of status field in the following table:</p> <table>   <tr><td>Value</td> <td>Description</td></tr>   <tr><td>0</td> <td>Not started</td></tr>   <tr><td>1</td> <td>Processing started</td></tr>   <tr><td>2</td> <td>Processing completed</td></tr>   <tr><td>-1</td> <td>Error</td></tr> </table> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

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
api_instance = crowdemotion_api_client_python.FaceVideoApi()
facevideo_id = 56 # int | FaceVideo ID. NOTE: Only this parameter is considered if both are specified. (optional)
response_id = 56 # int | Response ID corresponding to the FaceVideo. (optional)

try: 
    # Find a FaceVideo
    api_response = api_instance.facevideo_get(facevideo_id=facevideo_id, response_id=response_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FaceVideoApi->facevideo_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facevideo_id** | **int**| FaceVideo ID. NOTE: Only this parameter is considered if both are specified. | [optional] 
 **response_id** | **int**| Response ID corresponding to the FaceVideo. | [optional] 

### Return type

[**FaceVideo**](FaceVideo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facevideo_post**
> FaceVideo facevideo_post(filename=filename, sandbox=sandbox, response_id=response_id, research_id=research_id, media_id=media_id, respondent_id=respondent_id, process_video=process_video)

Analyse FaceVideo

<p>Starts the analysis of a single FaceVideo (in the supported formats) through either:</p> <ol>   <li>a video URL pointing to a resource accessible through the Internet without authentication</li>   <li>the binary contents of the video in the request's body, encoded as <code>multipart/form-data</code> content type</li> </ol> <p>The third option is a <code>PUT</code> call to <code>/v1/facevideo/{filename}</code> (<code>filename</code> required string e.g. <code>facevideo1.mp4</code>) which supports all the URL parameters as above with a body encoding <code>application/octet-stream</code> and the file contents as plain binary: this call makes uploads more efficient but it does not respect HTTP/RESTful standards so it may be not supported in future.</p> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

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
api_instance = crowdemotion_api_client_python.FaceVideoApi()
filename = '/path/to/file.txt' # file | FaceVideo to be analysed. (optional)
sandbox = true # bool | Generates random data for testing, at no cost. Default: false. (optional)
response_id = 56 # int | Associates this Facevideo to a previously generated Response. (optional)
research_id = 56 # int | Associates this Facevideo to a previously generated Research. (optional)
media_id = 56 # int | Associates this Facevideo to a previously generated Media. (optional)
respondent_id = 56 # int | Associates this Facevideo to a previously generated Respondent. (optional)
process_video = true # bool | Actually processes the video. Default: true. (optional)

try: 
    # Analyse FaceVideo
    api_response = api_instance.facevideo_post(filename=filename, sandbox=sandbox, response_id=response_id, research_id=research_id, media_id=media_id, respondent_id=respondent_id, process_video=process_video)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FaceVideoApi->facevideo_post: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **file**| FaceVideo to be analysed. | [optional] 
 **sandbox** | **bool**| Generates random data for testing, at no cost. Default: false. | [optional] 
 **response_id** | **int**| Associates this Facevideo to a previously generated Response. | [optional] 
 **research_id** | **int**| Associates this Facevideo to a previously generated Research. | [optional] 
 **media_id** | **int**| Associates this Facevideo to a previously generated Media. | [optional] 
 **respondent_id** | **int**| Associates this Facevideo to a previously generated Respondent. | [optional] 
 **process_video** | **bool**| Actually processes the video. Default: true. | [optional] 

### Return type

[**FaceVideo**](FaceVideo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facevideo_put**
> FaceVideo facevideo_put(sandbox=sandbox, response_id=response_id, research_id=research_id, media_id=media_id, respondent_id=respondent_id, process_video=process_video, body=body)

Analyse FaceVideo

<p>Starts the analysis of a single FaceVideo (in the supported formats) through either:</p> <ol>   <li>a video URL pointing to a resource accessible through the Internet without authentication</li>   <li>the binary contents of the video in the request's body, encoded as <code>multipart/form-data</code> content type</li> </ol> <p>The third option is a <code>PUT</code> call to <code>/v1/facevideo/{filename}</code> (<code>filename</code> required string e.g. <code>facevideo1.mp4</code>) which supports all the URL parameters as above with a body encoding <code>application/octet-stream</code> and the file contents as plain binary: this call makes uploads more efficient but it does not respect HTTP/RESTful standards so it may be not supported in future.</p> <p><strong>Permissions:</strong> ✓ Respondent ✓ Customer ✓ Manager</p>

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
api_instance = crowdemotion_api_client_python.FaceVideoApi()
sandbox = true # bool | Generates random data for testing, at no cost. Default: false. (optional)
response_id = 56 # int | Associates this Facevideo to a previously generated Response. (optional)
research_id = 56 # int | Associates this Facevideo to a previously generated Research. (optional)
media_id = 56 # int | Associates this Facevideo to a previously generated Media. (optional)
respondent_id = 56 # int | Associates this Facevideo to a previously generated Respondent. (optional)
process_video = true # bool | Actually processes the video. Default: true. (optional)
body = crowdemotion_api_client_python.FaceVideoUpload() # FaceVideoUpload | Request body (optional)

try: 
    # Analyse FaceVideo
    api_response = api_instance.facevideo_put(sandbox=sandbox, response_id=response_id, research_id=research_id, media_id=media_id, respondent_id=respondent_id, process_video=process_video, body=body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FaceVideoApi->facevideo_put: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox** | **bool**| Generates random data for testing, at no cost. Default: false. | [optional] 
 **response_id** | **int**| Associates this Facevideo to a previously generated Response. | [optional] 
 **research_id** | **int**| Associates this Facevideo to a previously generated Research. | [optional] 
 **media_id** | **int**| Associates this Facevideo to a previously generated Media. | [optional] 
 **respondent_id** | **int**| Associates this Facevideo to a previously generated Respondent. | [optional] 
 **process_video** | **bool**| Actually processes the video. Default: true. | [optional] 
 **body** | [**FaceVideoUpload**](FaceVideoUpload.md)| Request body | [optional] 

### Return type

[**FaceVideo**](FaceVideo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

