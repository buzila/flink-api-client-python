# CompletedCheckpointStatistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**is_savepoint** | **bool** |  | [optional] 
**trigger_timestamp** | **int** |  | [optional] 
**latest_ack_timestamp** | **int** |  | [optional] 
**state_size** | **int** |  | [optional] 
**end_to_end_duration** | **int** |  | [optional] 
**alignment_buffered** | **int** |  | [optional] 
**num_subtasks** | **int** |  | [optional] 
**num_acknowledged_subtasks** | **int** |  | [optional] 
**tasks** | [**dict(str, TaskCheckpointStatistics)**](TaskCheckpointStatistics.md) |  | [optional] 
**external_path** | **str** |  | [optional] 
**discarded** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

