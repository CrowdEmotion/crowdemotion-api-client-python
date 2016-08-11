# crowdemotion_api_client_python
CrowdEmotion API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.0.0
- Build date: 2016-08-11T15:53:19.605+01:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import crowdemotion_api_client_python 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import crowdemotion_api_client_python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = crowdemotion_api_client_python.FaceVideoApi
facevideo_id = 56 # int | ID of FaceVideo to be deleted.

try:
    # Delete a FaceVideo
    api_response = api_instance.facevideo_facevideo_id_delete(facevideo_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FaceVideoApi->facevideo_facevideo_id_delete: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.crowdemotion.co.uk/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FaceVideoApi* | [**facevideo_facevideo_id_delete**](docs/FaceVideoApi.md#facevideo_facevideo_id_delete) | **DELETE** /facevideo/{facevideo_id} | Delete a FaceVideo
*FaceVideoApi* | [**facevideo_get**](docs/FaceVideoApi.md#facevideo_get) | **GET** /facevideo | Find a FaceVideo
*FaceVideoApi* | [**facevideo_post**](docs/FaceVideoApi.md#facevideo_post) | **POST** /facevideo | Analyse FaceVideo
*FaceVideoApi* | [**facevideo_put**](docs/FaceVideoApi.md#facevideo_put) | **PUT** /facevideo | Analyse FaceVideo
*MediaApi* | [**media_get**](docs/MediaApi.md#media_get) | **GET** /media | Find all registered Media
*MediaApi* | [**media_media_id_delete**](docs/MediaApi.md#media_media_id_delete) | **DELETE** /media/{media_id} | Delete Media
*MediaApi* | [**media_media_id_get**](docs/MediaApi.md#media_media_id_get) | **GET** /media/{media_id} | Find a Media
*MediaApi* | [**media_media_id_put**](docs/MediaApi.md#media_media_id_put) | **PUT** /media/{media_id} | Update a Media
*MediaApi* | [**media_post**](docs/MediaApi.md#media_post) | **POST** /media | Create new Media
*MetricApi* | [**metric_get**](docs/MetricApi.md#metric_get) | **GET** /metric | List all registered metrics
*MetricApi* | [**metric_metric_id_delete**](docs/MetricApi.md#metric_metric_id_delete) | **DELETE** /metric/{metric_id} | Delete a Metric
*MetricApi* | [**metric_metric_id_get**](docs/MetricApi.md#metric_metric_id_get) | **GET** /metric/{metric_id} | Find a Metric
*MetricApi* | [**metric_post**](docs/MetricApi.md#metric_post) | **POST** /metric | Create Metric
*ResearchApi* | [**research_get**](docs/ResearchApi.md#research_get) | **GET** /research | Find all Research
*ResearchApi* | [**research_post**](docs/ResearchApi.md#research_post) | **POST** /research | Create a Research Project
*ResearchApi* | [**research_research_id_delete**](docs/ResearchApi.md#research_research_id_delete) | **DELETE** /research/{research_id} | Delete Research Project
*ResearchApi* | [**research_research_id_get**](docs/ResearchApi.md#research_research_id_get) | **GET** /research/{research_id} | Find a Research Project
*ResearchApi* | [**research_research_id_put**](docs/ResearchApi.md#research_research_id_put) | **PUT** /research/{research_id} | Edit Research Project details
*RespondentApi* | [**respondent_get**](docs/RespondentApi.md#respondent_get) | **GET** /respondent | Find all Respondents of a Research
*RespondentApi* | [**respondent_post**](docs/RespondentApi.md#respondent_post) | **POST** /respondent | Create a Respondent
*RespondentApi* | [**respondent_respondent_id_delete**](docs/RespondentApi.md#respondent_respondent_id_delete) | **DELETE** /respondent/{respondent_id} | Delete a Respondent
*RespondentApi* | [**respondent_respondent_id_get**](docs/RespondentApi.md#respondent_respondent_id_get) | **GET** /respondent/{respondent_id} | Find a Respondent
*RespondentApi* | [**respondent_respondent_id_metadata_get**](docs/RespondentApi.md#respondent_respondent_id_metadata_get) | **GET** /respondent/{respondent_id}/metadata | Find Respondent Metadata
*RespondentApi* | [**respondent_respondent_id_metadata_post**](docs/RespondentApi.md#respondent_respondent_id_metadata_post) | **POST** /respondent/{respondent_id}/metadata | Add Respondent Metadata
*RespondentApi* | [**respondent_respondent_id_put**](docs/RespondentApi.md#respondent_respondent_id_put) | **PUT** /respondent/{respondent_id} | Update a Respondent
*ResponseApi* | [**response_get**](docs/ResponseApi.md#response_get) | **GET** /response | Find all Responses
*ResponseApi* | [**response_post**](docs/ResponseApi.md#response_post) | **POST** /response | Create a Response
*ResponseApi* | [**response_response_id_delete**](docs/ResponseApi.md#response_response_id_delete) | **DELETE** /response/{response_id} | Delete a Response
*ResponseApi* | [**response_response_id_get**](docs/ResponseApi.md#response_response_id_get) | **GET** /response/{response_id} | Find a Response
*ResponseApi* | [**response_response_id_metadata_get**](docs/ResponseApi.md#response_response_id_metadata_get) | **GET** /response/{response_id}/metadata | Show Response Metadata
*ResponseApi* | [**response_response_id_metadata_post**](docs/ResponseApi.md#response_response_id_metadata_post) | **POST** /response/{response_id}/metadata | Add Response Metadata
*ResponseApi* | [**response_response_id_put**](docs/ResponseApi.md#response_response_id_put) | **PUT** /response/{response_id} | Update a Response
*TimeseriesApi* | [**timeseries_delete**](docs/TimeseriesApi.md#timeseries_delete) | **DELETE** /timeseries | Delete a Timeseries
*TimeseriesApi* | [**timeseries_get**](docs/TimeseriesApi.md#timeseries_get) | **GET** /timeseries | Get all recorded timeseries for a Response
*UserApi* | [**user_id_get**](docs/UserApi.md#user_id_get) | **GET** /user/{id} | Get User information
*UserApi* | [**user_id_put**](docs/UserApi.md#user_id_put) | **PUT** /user/{id} | Edit User information
*UserApi* | [**user_login_post**](docs/UserApi.md#user_login_post) | **POST** /user/login | User Login
*UserApi* | [**user_user_id_metadata_get**](docs/UserApi.md#user_user_id_metadata_get) | **GET** /user/{user_id}/metadata | Find User metadata
*UserApi* | [**user_user_id_metadata_post**](docs/UserApi.md#user_user_id_metadata_post) | **POST** /user/{user_id}/metadata | Add user metadata


## Documentation For Models

 - [ContentDetails](docs/ContentDetails.md)
 - [Data](docs/Data.md)
 - [FaceVideo](docs/FaceVideo.md)
 - [FaceVideoUpload](docs/FaceVideoUpload.md)
 - [Login](docs/Login.md)
 - [LoginResponse](docs/LoginResponse.md)
 - [Media](docs/Media.md)
 - [MediaCreation](docs/MediaCreation.md)
 - [Metric](docs/Metric.md)
 - [MetricCreation](docs/MetricCreation.md)
 - [Research](docs/Research.md)
 - [ResearchCreation](docs/ResearchCreation.md)
 - [Respondent](docs/Respondent.md)
 - [RespondentMetadata](docs/RespondentMetadata.md)
 - [RespondentMetadataResponse](docs/RespondentMetadataResponse.md)
 - [Response](docs/Response.md)
 - [ResponseCreation](docs/ResponseCreation.md)
 - [ResponseMetadata](docs/ResponseMetadata.md)
 - [ResponseMetadataResponse](docs/ResponseMetadataResponse.md)
 - [Statistics](docs/Statistics.md)
 - [Stats](docs/Stats.md)
 - [Status](docs/Status.md)
 - [Tags](docs/Tags.md)
 - [Timeseries](docs/Timeseries.md)
 - [User](docs/User.md)
 - [UserMetadata](docs/UserMetadata.md)
 - [UserMetadataResponse](docs/UserMetadataResponse.md)
 - [UserUpdateBody](docs/UserUpdateBody.md)
 - [Videodetails](docs/Videodetails.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



