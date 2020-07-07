# swagger_client.FlinkApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_savepoint**](FlinkApi.md#create_job_savepoint) | **POST** /jobs/{jobid}/savepoints | Triggers a savepoint, and optionally cancels the job afterwards
[**delete_jar**](FlinkApi.md#delete_jar) | **DELETE** /jars/{jarid} | Deletes a jar previously uploaded via &#x27;/jars/upload&#x27;
[**get_job_accumulators**](FlinkApi.md#get_job_accumulators) | **GET** /jobs/{jobid}/accumulators | Returns the accumulators for all tasks of a job, aggregated across the respective subtasks
[**get_job_aggregated_subtask_metrics**](FlinkApi.md#get_job_aggregated_subtask_metrics) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/metrics | Provides access to aggregated subtask metrics
[**get_job_checkpoint_details**](FlinkApi.md#get_job_checkpoint_details) | **GET** /jobs/{jobid}/checkpoints/details/{checkpointid} | Returns details for a checkpoint
[**get_job_checkpoint_statistics**](FlinkApi.md#get_job_checkpoint_statistics) | **GET** /jobs/{jobid}/checkpoints/details/{checkpointid}/subtasks/{vertexid} | Returns checkpoint statistics for a task and its subtasks
[**get_job_checkpoints**](FlinkApi.md#get_job_checkpoints) | **GET** /jobs/{jobid}/checkpoints | Returns checkpointing statistics for a job
[**get_job_checkpoints_config**](FlinkApi.md#get_job_checkpoints_config) | **GET** /jobs/{jobid}/checkpoints/config | Returns the checkpointing configuration
[**get_job_config**](FlinkApi.md#get_job_config) | **GET** /jobs/{jobid}/config | Returns the configuration of a job
[**get_job_details**](FlinkApi.md#get_job_details) | **GET** /jobs/{jobid} | Returns details of a job
[**get_job_exceptions**](FlinkApi.md#get_job_exceptions) | **GET** /jobs/{jobid}/exceptions | Returns the non-recoverable exceptions that have been observed by the job. The truncated flag defines whether more exceptions occurred, but are not listed, because the response would otherwise get too big
[**get_job_manager_metrics**](FlinkApi.md#get_job_manager_metrics) | **GET** /jobmanager/metrics | Provides access to job manager metrics
[**get_job_metrics**](FlinkApi.md#get_job_metrics) | **GET** /jobs/{jobid}/metrics | Provides access to job metrics
[**get_job_plan**](FlinkApi.md#get_job_plan) | **GET** /jobs/{jobid}/plan | Returns the dataflow plan of a job
[**get_job_rescaling_status**](FlinkApi.md#get_job_rescaling_status) | **GET** /jobs/{jobid}/rescaling/{triggerid} | Returns the status of a rescaling operation
[**get_job_result**](FlinkApi.md#get_job_result) | **GET** /jobs/{jobid}/execution-result | Returns the result of a job execution. Gives access to the execution time of the job and to all accumulators created by this job
[**get_job_savepoint_status**](FlinkApi.md#get_job_savepoint_status) | **GET** /jobs/{jobid}/savepoints/{triggerid} | Returns the status of a savepoint operation
[**get_job_subtask_accumulators**](FlinkApi.md#get_job_subtask_accumulators) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/accumulators | Returns all user-defined accumulators for all subtasks of a task
[**get_job_subtask_attempt_accumulators**](FlinkApi.md#get_job_subtask_attempt_accumulators) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex}/attempts/:attempt/accumulators | Returns the accumulators of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery
[**get_job_subtask_attempt_details**](FlinkApi.md#get_job_subtask_attempt_details) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex}/attempts/:attempt | Returns details of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery
[**get_job_subtask_details**](FlinkApi.md#get_job_subtask_details) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex} | Returns details of the current or latest execution attempt of a subtask
[**get_job_subtask_metrics**](FlinkApi.md#get_job_subtask_metrics) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasks/{subtaskindex}/metrics | Provides access to subtask metrics
[**get_job_subtask_times**](FlinkApi.md#get_job_subtask_times) | **GET** /jobs/{jobid}/vertices/{vertexid}/subtasktimes | Returns time-related information for all subtasks of a task
[**get_job_task_accumulators**](FlinkApi.md#get_job_task_accumulators) | **GET** /jobs/{jobid}/vertices/{vertexid}/accumulators | Returns user-defined accumulators of a task, aggregated across all subtasks
[**get_job_task_backpressure**](FlinkApi.md#get_job_task_backpressure) | **GET** /jobs/{jobid}/vertices/{vertexid}/backpressure | Returns back-pressure information for a job, and may initiate back-pressure sampling if necessary
[**get_job_task_details**](FlinkApi.md#get_job_task_details) | **GET** /jobs/{jobid}/vertices/{vertexid} | Returns details for a task, with a summary for each of its subtasks
[**get_job_task_details_by_task_manager**](FlinkApi.md#get_job_task_details_by_task_manager) | **GET** /jobs/{jobid}/vertices/{vertexid}/taskmanagers | Returns task information aggregated by task manager
[**get_job_task_metrics**](FlinkApi.md#get_job_task_metrics) | **GET** /jobs/{jobid}/vertices/{vertexid}/metrics | Provides access to task metrics
[**get_jobs**](FlinkApi.md#get_jobs) | **GET** /jobs | Returns an overview over all jobs and their current state
[**get_jobs_metrics**](FlinkApi.md#get_jobs_metrics) | **GET** /jobs/metrics | Provides access to aggregated job metrics
[**get_jobs_overview**](FlinkApi.md#get_jobs_overview) | **GET** /jobs/overview | Returns an overview over all jobs
[**get_overview**](FlinkApi.md#get_overview) | **GET** /overview | Returns an overview over the Flink cluster
[**get_savepoint_disposal_status**](FlinkApi.md#get_savepoint_disposal_status) | **GET** /savepoint-disposal/{triggerid} | Returns the status of a savepoint disposal operation
[**get_task_manager_aggregated_metrics**](FlinkApi.md#get_task_manager_aggregated_metrics) | **GET** /taskmanagers/metrics | Provides access to aggregated task manager metrics
[**get_task_manager_details**](FlinkApi.md#get_task_manager_details) | **GET** /taskmanagers/{taskmanagerid} | Returns details for a task manager
[**get_task_manager_metrics**](FlinkApi.md#get_task_manager_metrics) | **GET** /taskmanagers/{taskmanagerid}/metrics | Provides access to task manager metrics
[**get_task_managers_overview**](FlinkApi.md#get_task_managers_overview) | **GET** /taskmanagers | Returns an overview over all task managers
[**list_jars**](FlinkApi.md#list_jars) | **GET** /jars | Returns a list of all jars previously uploaded via &#x27;/jars/upload&#x27;
[**run_jar**](FlinkApi.md#run_jar) | **POST** /jars/{jarid}/run | Submits a job by running a jar previously uploaded via &#x27;/jars/upload&#x27;. Program arguments can be passed both via the JSON request (recommended) or query parameters
[**show_config**](FlinkApi.md#show_config) | **GET** /config | Returns the configuration of the WebUI
[**show_job_manager_config**](FlinkApi.md#show_job_manager_config) | **GET** /jobmanager/config | Returns the cluster configuration
[**show_plan**](FlinkApi.md#show_plan) | **GET** /jars/{jarid}/plan | Returns the dataflow plan of a job contained in a jar previously uploaded via &#x27;/jars/upload&#x27;. Program arguments can be passed both via the JSON request (recommended) or query parameters
[**shutdown_cluster**](FlinkApi.md#shutdown_cluster) | **DELETE** /cluster | Shuts-down the cluster
[**submit_job**](FlinkApi.md#submit_job) | **POST** /jobs | Submits a job. This call is primarily intended to be used by the Flink client. This call expects a multipart/form-data request that consists of file uploads for the serialized JobGraph, jars and distributed cache artifacts and an attribute named \&quot;request\&quot; for the JSON payload
[**terminate_job**](FlinkApi.md#terminate_job) | **PATCH** /jobs/{jobid} | Terminates a job
[**trigger_job_rescaling**](FlinkApi.md#trigger_job_rescaling) | **PATCH** /jobs/{jobid}/rescaling | Triggers the rescaling of a job
[**trigger_savepoint_disposal**](FlinkApi.md#trigger_savepoint_disposal) | **POST** /savepoint-disposal | Triggers the desposal of a savepoint
[**upload_jar**](FlinkApi.md#upload_jar) | **POST** /jars/upload | Uploads a jar to the cluster

# **create_job_savepoint**
> TriggerResponse create_job_savepoint(body, jobid)

Triggers a savepoint, and optionally cancels the job afterwards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
body = swagger_client.SavepointTriggerRequestBody() # SavepointTriggerRequestBody | 
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job

try:
    # Triggers a savepoint, and optionally cancels the job afterwards
    api_response = api_instance.create_job_savepoint(body, jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->create_job_savepoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavepointTriggerRequestBody**](SavepointTriggerRequestBody.md)|  | 
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_jar**
> delete_jar(jarid)

Deletes a jar previously uploaded via '/jars/upload'

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jarid = 'jarid_example' # str | String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the `id` field in the list of uploaded jars (/jars)

try:
    # Deletes a jar previously uploaded via '/jars/upload'
    api_instance.delete_jar(jarid)
except ApiException as e:
    print("Exception when calling FlinkApi->delete_jar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jarid** | **str**| String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the &#x60;id&#x60; field in the list of uploaded jars (/jars) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_accumulators**
> JobAccumulatorsInfo get_job_accumulators(jobid, include_serialized_value=include_serialized_value)

Returns the accumulators for all tasks of a job, aggregated across the respective subtasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
include_serialized_value = true # bool | Boolean value that specifies whether serialized user task accumulators should be included in the response (optional)

try:
    # Returns the accumulators for all tasks of a job, aggregated across the respective subtasks
    api_response = api_instance.get_job_accumulators(jobid, include_serialized_value=include_serialized_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_accumulators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **include_serialized_value** | **bool**| Boolean value that specifies whether serialized user task accumulators should be included in the response | [optional] 

### Return type

[**JobAccumulatorsInfo**](JobAccumulatorsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_aggregated_subtask_metrics**
> object get_job_aggregated_subtask_metrics(jobid, vertexid, get=get, agg=agg, subtasks=subtasks)

Provides access to aggregated subtask metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex
get = 'get_example' # str | Comma-separated list of string values to select specific metrics (optional)
agg = 'agg_example' # str | Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \"min, max, sum, avg\" (optional)
subtasks = 'subtasks_example' # str | Comma-separated list of integer ranges (e.g. \"1,3,5-9\") to select specific subtasks (optional)

try:
    # Provides access to aggregated subtask metrics
    api_response = api_instance.get_job_aggregated_subtask_metrics(jobid, vertexid, get=get, agg=agg, subtasks=subtasks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_aggregated_subtask_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 
 **get** | **str**| Comma-separated list of string values to select specific metrics | [optional] 
 **agg** | **str**| Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \&quot;min, max, sum, avg\&quot; | [optional] 
 **subtasks** | **str**| Comma-separated list of integer ranges (e.g. \&quot;1,3,5-9\&quot;) to select specific subtasks | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_checkpoint_details**
> CheckpointStatistics get_job_checkpoint_details(jobid, checkpointid)

Returns details for a checkpoint

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
checkpointid = 56 # int | Long value that identifies a checkpoint

try:
    # Returns details for a checkpoint
    api_response = api_instance.get_job_checkpoint_details(jobid, checkpointid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_checkpoint_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **checkpointid** | **int**| Long value that identifies a checkpoint | 

### Return type

[**CheckpointStatistics**](CheckpointStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_checkpoint_statistics**
> TaskCheckpointStatisticsWithSubtaskDetails get_job_checkpoint_statistics(jobid, checkpointid, vertexid)

Returns checkpoint statistics for a task and its subtasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
checkpointid = 56 # int | Long value that identifies a checkpoint
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex

try:
    # Returns checkpoint statistics for a task and its subtasks
    api_response = api_instance.get_job_checkpoint_statistics(jobid, checkpointid, vertexid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_checkpoint_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **checkpointid** | **int**| Long value that identifies a checkpoint | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 

### Return type

[**TaskCheckpointStatisticsWithSubtaskDetails**](TaskCheckpointStatisticsWithSubtaskDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_checkpoints**
> CheckpointingStatistics get_job_checkpoints(jobid)

Returns checkpointing statistics for a job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job

try:
    # Returns checkpointing statistics for a job
    api_response = api_instance.get_job_checkpoints(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_checkpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 

### Return type

[**CheckpointingStatistics**](CheckpointingStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_checkpoints_config**
> CheckpointConfigInfo get_job_checkpoints_config(jobid)

Returns the checkpointing configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job

try:
    # Returns the checkpointing configuration
    api_response = api_instance.get_job_checkpoints_config(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_checkpoints_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 

### Return type

[**CheckpointConfigInfo**](CheckpointConfigInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_config**
> str get_job_config(jobid)

Returns the configuration of a job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job

try:
    # Returns the configuration of a job
    api_response = api_instance.get_job_config(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_details**
> JobDetailsInfo get_job_details(jobid)

Returns details of a job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job

try:
    # Returns details of a job
    api_response = api_instance.get_job_details(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 

### Return type

[**JobDetailsInfo**](JobDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_exceptions**
> JobExceptionsInfo get_job_exceptions(jobid)

Returns the non-recoverable exceptions that have been observed by the job. The truncated flag defines whether more exceptions occurred, but are not listed, because the response would otherwise get too big

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job

try:
    # Returns the non-recoverable exceptions that have been observed by the job. The truncated flag defines whether more exceptions occurred, but are not listed, because the response would otherwise get too big
    api_response = api_instance.get_job_exceptions(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_exceptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 

### Return type

[**JobExceptionsInfo**](JobExceptionsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_manager_metrics**
> object get_job_manager_metrics(get=get)

Provides access to job manager metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
get = 'get_example' # str | Comma-separated list of string values to select specific metrics (optional)

try:
    # Provides access to job manager metrics
    api_response = api_instance.get_job_manager_metrics(get=get)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_manager_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get** | **str**| Comma-separated list of string values to select specific metrics | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_metrics**
> object get_job_metrics(jobid, get=get)

Provides access to job metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
get = 'get_example' # str | Comma-separated list of string values to select specific metrics (optional)

try:
    # Provides access to job metrics
    api_response = api_instance.get_job_metrics(jobid, get=get)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **get** | **str**| Comma-separated list of string values to select specific metrics | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_plan**
> JobPlanInfo get_job_plan(jobid)

Returns the dataflow plan of a job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job

try:
    # Returns the dataflow plan of a job
    api_response = api_instance.get_job_plan(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 

### Return type

[**JobPlanInfo**](JobPlanInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_rescaling_status**
> AsynchronousOperationResult get_job_rescaling_status(jobid, triggerid)

Returns the status of a rescaling operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
triggerid = 'triggerid_example' # str | 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered

try:
    # Returns the status of a rescaling operation
    api_response = api_instance.get_job_rescaling_status(jobid, triggerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_rescaling_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **triggerid** | **str**| 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered | 

### Return type

[**AsynchronousOperationResult**](AsynchronousOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_result**
> JobExecutionResultResponseBody get_job_result(jobid)

Returns the result of a job execution. Gives access to the execution time of the job and to all accumulators created by this job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job

try:
    # Returns the result of a job execution. Gives access to the execution time of the job and to all accumulators created by this job
    api_response = api_instance.get_job_result(jobid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 

### Return type

[**JobExecutionResultResponseBody**](JobExecutionResultResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_savepoint_status**
> AsynchronousOperationResult get_job_savepoint_status(jobid, triggerid)

Returns the status of a savepoint operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
triggerid = 'triggerid_example' # str | 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered

try:
    # Returns the status of a savepoint operation
    api_response = api_instance.get_job_savepoint_status(jobid, triggerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_savepoint_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **triggerid** | **str**| 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered | 

### Return type

[**AsynchronousOperationResult**](AsynchronousOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_subtask_accumulators**
> SubtasksAllAccumulatorsInfo get_job_subtask_accumulators(jobid, vertexid)

Returns all user-defined accumulators for all subtasks of a task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex

try:
    # Returns all user-defined accumulators for all subtasks of a task
    api_response = api_instance.get_job_subtask_accumulators(jobid, vertexid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_subtask_accumulators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 

### Return type

[**SubtasksAllAccumulatorsInfo**](SubtasksAllAccumulatorsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_subtask_attempt_accumulators**
> SubtaskExecutionAttemptAccumulatorsInfo get_job_subtask_attempt_accumulators(jobid, vertexid, subtaskindex, attempt)

Returns the accumulators of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex
subtaskindex = 56 # int | Positive integer value that identifies a subtask
attempt = 56 # int | Positive integer value that identifies an execution attempt

try:
    # Returns the accumulators of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery
    api_response = api_instance.get_job_subtask_attempt_accumulators(jobid, vertexid, subtaskindex, attempt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_subtask_attempt_accumulators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 
 **subtaskindex** | **int**| Positive integer value that identifies a subtask | 
 **attempt** | **int**| Positive integer value that identifies an execution attempt | 

### Return type

[**SubtaskExecutionAttemptAccumulatorsInfo**](SubtaskExecutionAttemptAccumulatorsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_subtask_attempt_details**
> SubtaskExecutionAttemptDetailsInfo get_job_subtask_attempt_details(jobid, vertexid, subtaskindex, attempt)

Returns details of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex
subtaskindex = 56 # int | Positive integer value that identifies a subtask
attempt = 56 # int | Positive integer value that identifies an execution attempt

try:
    # Returns details of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery
    api_response = api_instance.get_job_subtask_attempt_details(jobid, vertexid, subtaskindex, attempt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_subtask_attempt_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 
 **subtaskindex** | **int**| Positive integer value that identifies a subtask | 
 **attempt** | **int**| Positive integer value that identifies an execution attempt | 

### Return type

[**SubtaskExecutionAttemptDetailsInfo**](SubtaskExecutionAttemptDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_subtask_details**
> SubtaskExecutionAttemptDetailsInfo get_job_subtask_details(jobid, vertexid, subtaskindex)

Returns details of the current or latest execution attempt of a subtask

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex
subtaskindex = 56 # int | Positive integer value that identifies a subtask

try:
    # Returns details of the current or latest execution attempt of a subtask
    api_response = api_instance.get_job_subtask_details(jobid, vertexid, subtaskindex)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_subtask_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 
 **subtaskindex** | **int**| Positive integer value that identifies a subtask | 

### Return type

[**SubtaskExecutionAttemptDetailsInfo**](SubtaskExecutionAttemptDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_subtask_metrics**
> object get_job_subtask_metrics(jobid, vertexid, subtaskindex, get=get)

Provides access to subtask metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex
subtaskindex = 56 # int | Positive integer value that identifies a subtask
get = 'get_example' # str | Comma-separated list of string values to select specific metrics (optional)

try:
    # Provides access to subtask metrics
    api_response = api_instance.get_job_subtask_metrics(jobid, vertexid, subtaskindex, get=get)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_subtask_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 
 **subtaskindex** | **int**| Positive integer value that identifies a subtask | 
 **get** | **str**| Comma-separated list of string values to select specific metrics | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_subtask_times**
> SubtasksTimesInfo get_job_subtask_times(jobid, vertexid)

Returns time-related information for all subtasks of a task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex

try:
    # Returns time-related information for all subtasks of a task
    api_response = api_instance.get_job_subtask_times(jobid, vertexid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_subtask_times: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 

### Return type

[**SubtasksTimesInfo**](SubtasksTimesInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_task_accumulators**
> JobVertexAccumulatorsInfo get_job_task_accumulators(jobid, vertexid)

Returns user-defined accumulators of a task, aggregated across all subtasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex

try:
    # Returns user-defined accumulators of a task, aggregated across all subtasks
    api_response = api_instance.get_job_task_accumulators(jobid, vertexid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_task_accumulators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 

### Return type

[**JobVertexAccumulatorsInfo**](JobVertexAccumulatorsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_task_backpressure**
> JobVertexBackPressureInfo get_job_task_backpressure(jobid, vertexid)

Returns back-pressure information for a job, and may initiate back-pressure sampling if necessary

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex

try:
    # Returns back-pressure information for a job, and may initiate back-pressure sampling if necessary
    api_response = api_instance.get_job_task_backpressure(jobid, vertexid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_task_backpressure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 

### Return type

[**JobVertexBackPressureInfo**](JobVertexBackPressureInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_task_details**
> JobVertexDetailsInfo get_job_task_details(jobid, vertexid)

Returns details for a task, with a summary for each of its subtasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex

try:
    # Returns details for a task, with a summary for each of its subtasks
    api_response = api_instance.get_job_task_details(jobid, vertexid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_task_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 

### Return type

[**JobVertexDetailsInfo**](JobVertexDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_task_details_by_task_manager**
> JobVertexTaskManagersInfo get_job_task_details_by_task_manager(jobid, vertexid)

Returns task information aggregated by task manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex

try:
    # Returns task information aggregated by task manager
    api_response = api_instance.get_job_task_details_by_task_manager(jobid, vertexid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_task_details_by_task_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 

### Return type

[**JobVertexTaskManagersInfo**](JobVertexTaskManagersInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_task_metrics**
> object get_job_task_metrics(jobid, vertexid, get=get)

Provides access to task metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
vertexid = 'vertexid_example' # str | 32-character hexadecimal string value that identifies a job vertex
get = 'get_example' # str | Comma-separated list of string values to select specific metrics (optional)

try:
    # Provides access to task metrics
    api_response = api_instance.get_job_task_metrics(jobid, vertexid, get=get)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_job_task_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **vertexid** | **str**| 32-character hexadecimal string value that identifies a job vertex | 
 **get** | **str**| Comma-separated list of string values to select specific metrics | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> JobIdsWithStatusOverview get_jobs()

Returns an overview over all jobs and their current state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()

try:
    # Returns an overview over all jobs and their current state
    api_response = api_instance.get_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JobIdsWithStatusOverview**](JobIdsWithStatusOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_metrics**
> object get_jobs_metrics(get=get, agg=agg, jobs=jobs)

Provides access to aggregated job metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
get = 'get_example' # str | Comma-separated list of string values to select specific metrics (optional)
agg = 'agg_example' # str | Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \"min, max, sum, avg\" (optional)
jobs = 'jobs_example' # str | Comma-separated list of 32-character hexadecimal strings to select specific jobs (optional)

try:
    # Provides access to aggregated job metrics
    api_response = api_instance.get_jobs_metrics(get=get, agg=agg, jobs=jobs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_jobs_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get** | **str**| Comma-separated list of string values to select specific metrics | [optional] 
 **agg** | **str**| Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \&quot;min, max, sum, avg\&quot; | [optional] 
 **jobs** | **str**| Comma-separated list of 32-character hexadecimal strings to select specific jobs | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_overview**
> MultipleJobsDetails get_jobs_overview()

Returns an overview over all jobs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()

try:
    # Returns an overview over all jobs
    api_response = api_instance.get_jobs_overview()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_jobs_overview: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MultipleJobsDetails**](MultipleJobsDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overview**
> ClusterOverviewWithVersion get_overview()

Returns an overview over the Flink cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()

try:
    # Returns an overview over the Flink cluster
    api_response = api_instance.get_overview()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_overview: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterOverviewWithVersion**](ClusterOverviewWithVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_savepoint_disposal_status**
> AsynchronousOperationResult get_savepoint_disposal_status(triggerid)

Returns the status of a savepoint disposal operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
triggerid = 'triggerid_example' # str | 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered

try:
    # Returns the status of a savepoint disposal operation
    api_response = api_instance.get_savepoint_disposal_status(triggerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_savepoint_disposal_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triggerid** | **str**| 32-character hexadecimal string that identifies an asynchronous operation trigger ID. The ID was returned then the operation was triggered | 

### Return type

[**AsynchronousOperationResult**](AsynchronousOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_manager_aggregated_metrics**
> object get_task_manager_aggregated_metrics(get=get, agg=agg, taskmanagers=taskmanagers)

Provides access to aggregated task manager metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
get = 'get_example' # str | Comma-separated list of string values to select specific metrics (optional)
agg = 'agg_example' # str | Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \"min, max, sum, avg\" (optional)
taskmanagers = 'taskmanagers_example' # str | Comma-separated list of 32-character hexadecimal strings to select specific task managers (optional)

try:
    # Provides access to aggregated task manager metrics
    api_response = api_instance.get_task_manager_aggregated_metrics(get=get, agg=agg, taskmanagers=taskmanagers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_task_manager_aggregated_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get** | **str**| Comma-separated list of string values to select specific metrics | [optional] 
 **agg** | **str**| Comma-separated list of aggregation modes which should be calculated. Available aggregations are: \&quot;min, max, sum, avg\&quot; | [optional] 
 **taskmanagers** | **str**| Comma-separated list of 32-character hexadecimal strings to select specific task managers | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_manager_details**
> TaskManagerDetailsInfo get_task_manager_details(taskmanagerid)

Returns details for a task manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
taskmanagerid = 'taskmanagerid_example' # str | 32-character hexadecimal string that identifies a task manager

try:
    # Returns details for a task manager
    api_response = api_instance.get_task_manager_details(taskmanagerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_task_manager_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskmanagerid** | **str**| 32-character hexadecimal string that identifies a task manager | 

### Return type

[**TaskManagerDetailsInfo**](TaskManagerDetailsInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_manager_metrics**
> object get_task_manager_metrics(taskmanagerid, get=get)

Provides access to task manager metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
taskmanagerid = 'taskmanagerid_example' # str | 32-character hexadecimal string that identifies a task manager
get = 'get_example' # str | Comma-separated list of string values to select specific metrics (optional)

try:
    # Provides access to task manager metrics
    api_response = api_instance.get_task_manager_metrics(taskmanagerid, get=get)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_task_manager_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskmanagerid** | **str**| 32-character hexadecimal string that identifies a task manager | 
 **get** | **str**| Comma-separated list of string values to select specific metrics | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_managers_overview**
> TaskManagersInfo get_task_managers_overview()

Returns an overview over all task managers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()

try:
    # Returns an overview over all task managers
    api_response = api_instance.get_task_managers_overview()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->get_task_managers_overview: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaskManagersInfo**](TaskManagersInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jars**
> JarListInfo list_jars()

Returns a list of all jars previously uploaded via '/jars/upload'

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()

try:
    # Returns a list of all jars previously uploaded via '/jars/upload'
    api_response = api_instance.list_jars()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->list_jars: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JarListInfo**](JarListInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_jar**
> JarRunResponseBody run_jar(jarid, allow_non_restored_state=allow_non_restored_state, savepoint_path=savepoint_path, program_args=program_args, program_arg=program_arg, entry_class=entry_class, parallelism=parallelism)

Submits a job by running a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jarid = 'jarid_example' # str | String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the `id` field in the list of uploaded jars (/jars)
allow_non_restored_state = true # bool | Boolean value that specifies whether the job submission should be rejected if the savepoint contains state that cannot be mapped back to the job (optional)
savepoint_path = 'savepoint_path_example' # str | Comma-separated list of program arguments (optional)
program_args = 'program_args_example' # str | Deprecated, please use 'programArg' instead. String value that specifies the arguments for the program or plan (optional)
program_arg = 'program_arg_example' # str | Comma-separated list of program arguments (optional)
entry_class = 'entry_class_example' # str | String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest (optional)
parallelism = 56 # int | Positive integer value that specifies the desired parallelism for the job (optional)

try:
    # Submits a job by running a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters
    api_response = api_instance.run_jar(jarid, allow_non_restored_state=allow_non_restored_state, savepoint_path=savepoint_path, program_args=program_args, program_arg=program_arg, entry_class=entry_class, parallelism=parallelism)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->run_jar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jarid** | **str**| String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the &#x60;id&#x60; field in the list of uploaded jars (/jars) | 
 **allow_non_restored_state** | **bool**| Boolean value that specifies whether the job submission should be rejected if the savepoint contains state that cannot be mapped back to the job | [optional] 
 **savepoint_path** | **str**| Comma-separated list of program arguments | [optional] 
 **program_args** | **str**| Deprecated, please use &#x27;programArg&#x27; instead. String value that specifies the arguments for the program or plan | [optional] 
 **program_arg** | **str**| Comma-separated list of program arguments | [optional] 
 **entry_class** | **str**| String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest | [optional] 
 **parallelism** | **int**| Positive integer value that specifies the desired parallelism for the job | [optional] 

### Return type

[**JarRunResponseBody**](JarRunResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_config**
> DashboardConfiguration show_config()

Returns the configuration of the WebUI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()

try:
    # Returns the configuration of the WebUI
    api_response = api_instance.show_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->show_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DashboardConfiguration**](DashboardConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_job_manager_config**
> list[ClusterConfigurationInfoEntry] show_job_manager_config()

Returns the cluster configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()

try:
    # Returns the cluster configuration
    api_response = api_instance.show_job_manager_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->show_job_manager_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ClusterConfigurationInfoEntry]**](ClusterConfigurationInfoEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_plan**
> JobPlanInfo show_plan(jarid, program_args=program_args, program_arg=program_arg, entry_class=entry_class, parallelism=parallelism)

Returns the dataflow plan of a job contained in a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jarid = 'jarid_example' # str | String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the `id` field in the list of uploaded jars (/jars)
program_args = 'program_args_example' # str | Deprecated, please use 'programArg' instead. String value that specifies the arguments for the program or plan (optional)
program_arg = 'program_arg_example' # str | Comma-separated list of program arguments (optional)
entry_class = 'entry_class_example' # str | String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest (optional)
parallelism = 56 # int | Positive integer value that specifies the desired parallelism for the job (optional)

try:
    # Returns the dataflow plan of a job contained in a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters
    api_response = api_instance.show_plan(jarid, program_args=program_args, program_arg=program_arg, entry_class=entry_class, parallelism=parallelism)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->show_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jarid** | **str**| String value that identifies a jar. When uploading the jar a path is returned, where the filename is the ID. This value is equivalent to the &#x60;id&#x60; field in the list of uploaded jars (/jars) | 
 **program_args** | **str**| Deprecated, please use &#x27;programArg&#x27; instead. String value that specifies the arguments for the program or plan | [optional] 
 **program_arg** | **str**| Comma-separated list of program arguments | [optional] 
 **entry_class** | **str**| String value that specifies the fully qualified name of the entry point class. Overrides the class defined in the jar file manifest | [optional] 
 **parallelism** | **int**| Positive integer value that specifies the desired parallelism for the job | [optional] 

### Return type

[**JobPlanInfo**](JobPlanInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_cluster**
> shutdown_cluster()

Shuts-down the cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()

try:
    # Shuts-down the cluster
    api_instance.shutdown_cluster()
except ApiException as e:
    print("Exception when calling FlinkApi->shutdown_cluster: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_job**
> JobSubmitResponseBody submit_job(job_graph_file_name, job_jar_file_names, job_artifact_file_names)

Submits a job. This call is primarily intended to be used by the Flink client. This call expects a multipart/form-data request that consists of file uploads for the serialized JobGraph, jars and distributed cache artifacts and an attribute named \"request\" for the JSON payload

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
job_graph_file_name = 'job_graph_file_name_example' # str | 
job_jar_file_names = ['job_jar_file_names_example'] # list[str] | 
job_artifact_file_names = [swagger_client.JobsJobArtifactFileNames()] # list[JobsJobArtifactFileNames] | 

try:
    # Submits a job. This call is primarily intended to be used by the Flink client. This call expects a multipart/form-data request that consists of file uploads for the serialized JobGraph, jars and distributed cache artifacts and an attribute named \"request\" for the JSON payload
    api_response = api_instance.submit_job(job_graph_file_name, job_jar_file_names, job_artifact_file_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->submit_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_graph_file_name** | **str**|  | 
 **job_jar_file_names** | [**list[str]**](str.md)|  | 
 **job_artifact_file_names** | [**list[JobsJobArtifactFileNames]**](JobsJobArtifactFileNames.md)|  | 

### Return type

[**JobSubmitResponseBody**](JobSubmitResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_job**
> terminate_job(jobid, mode=mode)

Terminates a job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
mode = 'mode_example' # str | String value that specifies the termination mode. Supported values are: \"cancel, stop\" (optional)

try:
    # Terminates a job
    api_instance.terminate_job(jobid, mode=mode)
except ApiException as e:
    print("Exception when calling FlinkApi->terminate_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **mode** | **str**| String value that specifies the termination mode. Supported values are: \&quot;cancel, stop\&quot; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_job_rescaling**
> TriggerResponse trigger_job_rescaling(jobid, parallelism)

Triggers the rescaling of a job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jobid = 'jobid_example' # str | 32-character hexadecimal string value that identifies a job
parallelism = 56 # int | Positive integer value that specifies the desired parallelism

try:
    # Triggers the rescaling of a job
    api_response = api_instance.trigger_job_rescaling(jobid, parallelism)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->trigger_job_rescaling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobid** | **str**| 32-character hexadecimal string value that identifies a job | 
 **parallelism** | **int**| Positive integer value that specifies the desired parallelism | 

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_savepoint_disposal**
> TriggerResponse trigger_savepoint_disposal(body)

Triggers the desposal of a savepoint

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
body = swagger_client.SavepointDisposalRequest() # SavepointDisposalRequest | 

try:
    # Triggers the desposal of a savepoint
    api_response = api_instance.trigger_savepoint_disposal(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->trigger_savepoint_disposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavepointDisposalRequest**](SavepointDisposalRequest.md)|  | 

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_jar**
> JarUploadResponseBody upload_jar(jarfile)

Uploads a jar to the cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FlinkApi()
jarfile = 'jarfile_example' # str | 

try:
    # Uploads a jar to the cluster
    api_response = api_instance.upload_jar(jarfile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlinkApi->upload_jar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jarfile** | **str**|  | 

### Return type

[**JarUploadResponseBody**](JarUploadResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

