# coding: utf-8

"""
    CloudEmotion API v1

    CrowdEmotion API

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import crowdemotion_api_client_python
from crowdemotion_api_client_python.rest import ApiException
from crowdemotion_api_client_python.apis.metric_api import MetricApi


class TestMetricApi(unittest.TestCase):
    """ MetricApi unit test stubs """

    def setUp(self):
        self.api = crowdemotion_api_client_python.apis.metric_api.MetricApi()

    def tearDown(self):
        pass

    def test_metric_get(self):
        """
        Test case for metric_get

        List all registered metrics
        """
        pass

    def test_metric_metric_id_delete(self):
        """
        Test case for metric_metric_id_delete

        Delete a Metric
        """
        pass

    def test_metric_metric_id_get(self):
        """
        Test case for metric_metric_id_get

        Find a Metric
        """
        pass

    def test_metric_post(self):
        """
        Test case for metric_post

        Create Metric
        """
        pass


if __name__ == '__main__':
    unittest.main()