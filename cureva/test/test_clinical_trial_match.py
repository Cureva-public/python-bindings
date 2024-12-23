# coding: utf-8

"""
    Clinical Match API

    A simple API to match patients to clinical trials.

    The version of the OpenAPI document: 1.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.clinical_trial_match import ClinicalTrialMatch

class TestClinicalTrialMatch(unittest.TestCase):
    """ClinicalTrialMatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClinicalTrialMatch:
        """Test ClinicalTrialMatch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClinicalTrialMatch`
        """
        model = ClinicalTrialMatch()
        if include_optional:
            return ClinicalTrialMatch(
                trial_id = '',
                trial_name = '',
                locations = [
                    openapi_client.models.location.location(
                        facility = 'Tufts Medical Center', 
                        city = 'Boston', 
                        state = 'MA', 
                        zip = '02113', 
                        country = 'United States', )
                    ],
                summary = '',
                status = ''
            )
        else:
            return ClinicalTrialMatch(
                trial_id = '',
                trial_name = '',
                locations = [
                    openapi_client.models.location.location(
                        facility = 'Tufts Medical Center', 
                        city = 'Boston', 
                        state = 'MA', 
                        zip = '02113', 
                        country = 'United States', )
                    ],
                summary = '',
        )
        """

    def testClinicalTrialMatch(self):
        """Test ClinicalTrialMatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
