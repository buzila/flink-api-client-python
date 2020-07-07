# coding: utf-8

"""
    Flink Client

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.flink_api import FlinkApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFlinkApi(unittest.TestCase):
    """FlinkApi unit test stubs"""

    def setUp(self):
        self.api = api.flink_api.FlinkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_job_savepoint(self):
        """Test case for create_job_savepoint

        Triggers a savepoint, and optionally cancels the job afterwards  # noqa: E501
        """
        pass

    def test_delete_jar(self):
        """Test case for delete_jar

        Deletes a jar previously uploaded via '/jars/upload'  # noqa: E501
        """
        pass

    def test_get_job_accumulators(self):
        """Test case for get_job_accumulators

        Returns the accumulators for all tasks of a job, aggregated across the respective subtasks  # noqa: E501
        """
        pass

    def test_get_job_aggregated_subtask_metrics(self):
        """Test case for get_job_aggregated_subtask_metrics

        Provides access to aggregated subtask metrics  # noqa: E501
        """
        pass

    def test_get_job_checkpoint_details(self):
        """Test case for get_job_checkpoint_details

        Returns details for a checkpoint  # noqa: E501
        """
        pass

    def test_get_job_checkpoint_statistics(self):
        """Test case for get_job_checkpoint_statistics

        Returns checkpoint statistics for a task and its subtasks  # noqa: E501
        """
        pass

    def test_get_job_checkpoints(self):
        """Test case for get_job_checkpoints

        Returns checkpointing statistics for a job  # noqa: E501
        """
        pass

    def test_get_job_checkpoints_config(self):
        """Test case for get_job_checkpoints_config

        Returns the checkpointing configuration  # noqa: E501
        """
        pass

    def test_get_job_config(self):
        """Test case for get_job_config

        Returns the configuration of a job  # noqa: E501
        """
        pass

    def test_get_job_details(self):
        """Test case for get_job_details

        Returns details of a job  # noqa: E501
        """
        pass

    def test_get_job_exceptions(self):
        """Test case for get_job_exceptions

        Returns the non-recoverable exceptions that have been observed by the job. The truncated flag defines whether more exceptions occurred, but are not listed, because the response would otherwise get too big  # noqa: E501
        """
        pass

    def test_get_job_manager_metrics(self):
        """Test case for get_job_manager_metrics

        Provides access to job manager metrics  # noqa: E501
        """
        pass

    def test_get_job_metrics(self):
        """Test case for get_job_metrics

        Provides access to job metrics  # noqa: E501
        """
        pass

    def test_get_job_plan(self):
        """Test case for get_job_plan

        Returns the dataflow plan of a job  # noqa: E501
        """
        pass

    def test_get_job_rescaling_status(self):
        """Test case for get_job_rescaling_status

        Returns the status of a rescaling operation  # noqa: E501
        """
        pass

    def test_get_job_result(self):
        """Test case for get_job_result

        Returns the result of a job execution. Gives access to the execution time of the job and to all accumulators created by this job  # noqa: E501
        """
        pass

    def test_get_job_savepoint_status(self):
        """Test case for get_job_savepoint_status

        Returns the status of a savepoint operation  # noqa: E501
        """
        pass

    def test_get_job_subtask_accumulators(self):
        """Test case for get_job_subtask_accumulators

        Returns all user-defined accumulators for all subtasks of a task  # noqa: E501
        """
        pass

    def test_get_job_subtask_attempt_accumulators(self):
        """Test case for get_job_subtask_attempt_accumulators

        Returns the accumulators of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery  # noqa: E501
        """
        pass

    def test_get_job_subtask_attempt_details(self):
        """Test case for get_job_subtask_attempt_details

        Returns details of an execution attempt of a subtask. Multiple execution attempts happen in case of failure/recovery  # noqa: E501
        """
        pass

    def test_get_job_subtask_details(self):
        """Test case for get_job_subtask_details

        Returns details of the current or latest execution attempt of a subtask  # noqa: E501
        """
        pass

    def test_get_job_subtask_metrics(self):
        """Test case for get_job_subtask_metrics

        Provides access to subtask metrics  # noqa: E501
        """
        pass

    def test_get_job_subtask_times(self):
        """Test case for get_job_subtask_times

        Returns time-related information for all subtasks of a task  # noqa: E501
        """
        pass

    def test_get_job_task_accumulators(self):
        """Test case for get_job_task_accumulators

        Returns user-defined accumulators of a task, aggregated across all subtasks  # noqa: E501
        """
        pass

    def test_get_job_task_backpressure(self):
        """Test case for get_job_task_backpressure

        Returns back-pressure information for a job, and may initiate back-pressure sampling if necessary  # noqa: E501
        """
        pass

    def test_get_job_task_details(self):
        """Test case for get_job_task_details

        Returns details for a task, with a summary for each of its subtasks  # noqa: E501
        """
        pass

    def test_get_job_task_details_by_task_manager(self):
        """Test case for get_job_task_details_by_task_manager

        Returns task information aggregated by task manager  # noqa: E501
        """
        pass

    def test_get_job_task_metrics(self):
        """Test case for get_job_task_metrics

        Provides access to task metrics  # noqa: E501
        """
        pass

    def test_get_jobs(self):
        """Test case for get_jobs

        Returns an overview over all jobs and their current state  # noqa: E501
        """
        pass

    def test_get_jobs_metrics(self):
        """Test case for get_jobs_metrics

        Provides access to aggregated job metrics  # noqa: E501
        """
        pass

    def test_get_jobs_overview(self):
        """Test case for get_jobs_overview

        Returns an overview over all jobs  # noqa: E501
        """
        pass

    def test_get_overview(self):
        """Test case for get_overview

        Returns an overview over the Flink cluster  # noqa: E501
        """
        pass

    def test_get_savepoint_disposal_status(self):
        """Test case for get_savepoint_disposal_status

        Returns the status of a savepoint disposal operation  # noqa: E501
        """
        pass

    def test_get_task_manager_aggregated_metrics(self):
        """Test case for get_task_manager_aggregated_metrics

        Provides access to aggregated task manager metrics  # noqa: E501
        """
        pass

    def test_get_task_manager_details(self):
        """Test case for get_task_manager_details

        Returns details for a task manager  # noqa: E501
        """
        pass

    def test_get_task_manager_metrics(self):
        """Test case for get_task_manager_metrics

        Provides access to task manager metrics  # noqa: E501
        """
        pass

    def test_get_task_managers_overview(self):
        """Test case for get_task_managers_overview

        Returns an overview over all task managers  # noqa: E501
        """
        pass

    def test_list_jars(self):
        """Test case for list_jars

        Returns a list of all jars previously uploaded via '/jars/upload'  # noqa: E501
        """
        pass

    def test_run_jar(self):
        """Test case for run_jar

        Submits a job by running a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters  # noqa: E501
        """
        pass

    def test_show_config(self):
        """Test case for show_config

        Returns the configuration of the WebUI  # noqa: E501
        """
        pass

    def test_show_job_manager_config(self):
        """Test case for show_job_manager_config

        Returns the cluster configuration  # noqa: E501
        """
        pass

    def test_show_plan(self):
        """Test case for show_plan

        Returns the dataflow plan of a job contained in a jar previously uploaded via '/jars/upload'. Program arguments can be passed both via the JSON request (recommended) or query parameters  # noqa: E501
        """
        pass

    def test_shutdown_cluster(self):
        """Test case for shutdown_cluster

        Shuts-down the cluster  # noqa: E501
        """
        pass

    def test_submit_job(self):
        """Test case for submit_job

        Submits a job. This call is primarily intended to be used by the Flink client. This call expects a multipart/form-data request that consists of file uploads for the serialized JobGraph, jars and distributed cache artifacts and an attribute named \"request\" for the JSON payload  # noqa: E501
        """
        pass

    def test_terminate_job(self):
        """Test case for terminate_job

        Terminates a job  # noqa: E501
        """
        pass

    def test_trigger_job_rescaling(self):
        """Test case for trigger_job_rescaling

        Triggers the rescaling of a job  # noqa: E501
        """
        pass

    def test_trigger_savepoint_disposal(self):
        """Test case for trigger_savepoint_disposal

        Triggers the desposal of a savepoint  # noqa: E501
        """
        pass

    def test_upload_jar(self):
        """Test case for upload_jar

        Uploads a jar to the cluster  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
