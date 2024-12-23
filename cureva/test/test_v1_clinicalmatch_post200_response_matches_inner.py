# coding: utf-8

"""
    Clinical Match API

    A simple API to match patients to clinical trials.

    The version of the OpenAPI document: 1.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v1_clinicalmatch_post200_response_matches_inner import V1ClinicalmatchPost200ResponseMatchesInner

class TestV1ClinicalmatchPost200ResponseMatchesInner(unittest.TestCase):
    """V1ClinicalmatchPost200ResponseMatchesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ClinicalmatchPost200ResponseMatchesInner:
        """Test V1ClinicalmatchPost200ResponseMatchesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ClinicalmatchPost200ResponseMatchesInner`
        """
        model = V1ClinicalmatchPost200ResponseMatchesInner()
        if include_optional:
            return V1ClinicalmatchPost200ResponseMatchesInner(
                trial_id = 'NCT00344331',
                trial_name = 'Evaluation of Biochemical Markers and Clinical Investigation of Niemann-Pick Disease, Type C',
                locations = [
                    openapi_client.models.location.location(
                        facility = 'Tufts Medical Center', 
                        city = 'Boston', 
                        state = 'MA', 
                        zip = '02113', 
                        country = 'United States', )
                    ],
                summary = 'Niemann-Pick type C disease (NPC) is an autosomal recessive, lysosomal storage disorder characterized by accumulation of cholesterol and gangliosides. NPC is a rare (estimated prevalence of 1:120,000-150,000) neurodegenerative disorder with a wide clinical spectrum and a variable age of onset. Classically, children with NPC demonstrate neurological dysfunction with cerebellar ataxia, dysarthria, seizures, vertical gaze palsy, motor impairment, dysphagia, psychotic episodes, and progressive dementia. In general, adolescent and adult onset forms have a more insidious onset and slower progression.

There is no effective treatment for NPC and it is a lethal disorder. A major impediment to the testing of therapeutic interventions is the lack of well-defined outcome measures. The purpose of this protocol is to obtain both baseline and rate of progression data on clinical and biochemical markers that may later be used as an outcome measure in a clinical trial.',
                status = 'Actively Recruiting'
            )
        else:
            return V1ClinicalmatchPost200ResponseMatchesInner(
        )
        """

    def testV1ClinicalmatchPost200ResponseMatchesInner(self):
        """Test V1ClinicalmatchPost200ResponseMatchesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
