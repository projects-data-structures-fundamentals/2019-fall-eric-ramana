"""
test_job_satisfaction_by_gender.py
Tests for evaluating csv data.
Eric O'Neil
Ramana Kondaveeti
Created: 2019-12-15
Updated: 2019-12-15
"""
import unittest
from problems import data_analysis


class DictionaryTests(unittest.TestCase):
    """
    Tests data collection from csv files
    """
    def setUp(self):
        self.small_csv = 'test_survey.csv'
        self.medium_csv = 'survey_results_public_medium.csv'
        self.full_csv = 'survey_results_public_modified.csv'


    def test_small_csv(self):
        """
        Csv file with 20 lines
        """
        satisfaction_actual = \
            data_analysis.job_satisfaction_by_gender(self.small_csv)
        satisfaction_expected = {
            'Male': {
                'Extremely satisfied': 1,
                'Moderately dissatisfied': 1,
                'Neither satisfied nor dissatisfied': 2,
                'Slightly satisfied': 2,
                'Moderately satisfied': 3
            },
            'NA': {
                'Moderately satisfied': 1,
                'NA': 4,
                'Moderately dissatisfied': 2,
                'Extremely satisfied': 1
            },
            'Female': {'Slightly satisfied': 2}
         }
        self.assertDictEqual(satisfaction_actual, satisfaction_expected)


    def test_medium_csv(self):
        """
        Csv file with 1,000 lines
        """
        satisfaction_actual = \
            data_analysis.job_satisfaction_by_gender(self.medium_csv)
        satisfaction_expected = {
            'Male': {
                'Extremely satisfied': 103,
                'Moderately dissatisfied': 52,
                'Neither satisfied nor dissatisfied': 46,
                'Slightly satisfied': 90,
                'Moderately satisfied': 222,
                'Slightly dissatisfied': 75,
                'NA': 28,
                'Extremely dissatisfied': 16
            },
            'NA': {
                'Moderately satisfied': 65,
                'NA': 133,
                'Moderately dissatisfied': 20,
                'Extremely satisfied': 23,
                'Neither satisfied nor dissatisfied': 17,
                'Slightly satisfied': 33,
                'Extremely dissatisfied': 2,
                'Slightly dissatisfied': 13
            },
            'Female': {
                'Slightly satisfied': 10,
                'Extremely dissatisfied': 2,
                'Moderately dissatisfied': 5,
                'NA': 1,
                'Moderately satisfied': 20,
                'Neither satisfied nor dissatisfied': 5,
                'Slightly dissatisfied': 5,
                'Extremely satisfied': 5
            },
            'Female;Male;Transgender;Non-binary, '
            'genderqueer, or gender non-conforming': {
                'Slightly dissatisfied': 1
            },
            'Female;Male': {
                'Moderately satisfied': 2
            },
            'Male;Non-binary, genderqueer, or gender '
            'non-conforming': {
                'Moderately satisfied': 1
            },
            'Non-binary, genderqueer, or gender '
            'non-conforming': {
                'Slightly satisfied': 1
            },
            'Transgender': {
                'Slightly dissatisfied': 1,
                'Moderately satisfied': 1
            },
            'Female;Transgender': {
                'Moderately dissatisfied': 1
            }
        }
        self.assertDictEqual(satisfaction_actual, satisfaction_expected)

    def test_full_csv(self):
        """
        Text file with 48,000 lines
        """
        satisfaction_actual = \
            data_analysis.job_satisfaction_by_gender(self.full_csv)
        satisfaction_expected = {
            'Male': {
                'Extremely satisfied': 5360,
                'Moderately dissatisfied': 2873,
                'Neither satisfied nor dissatisfied': 1865,
                'Slightly satisfied': 4393,
                'Moderately satisfied': 11388,
                'Slightly dissatisfied': 3142,
                'NA': 1088,
                'Extremely dissatisfied': 994
            },
            'NA': {
                'Moderately satisfied': 2941,
                'NA': 6320,
                'Moderately dissatisfied': 717,
                'Extremely satisfied': 1243,
                'Neither satisfied nor dissatisfied': 670,
                'Slightly satisfied': 1228,
                'Extremely dissatisfied': 336,
                'Slightly dissatisfied': 838
            },
            'Female': {
                'Slightly satisfied': 263,
                'Extremely dissatisfied': 74,
                'Moderately dissatisfied': 203,
                'NA': 112,
                'Moderately satisfied': 762,
                'Neither satisfied nor dissatisfied': 136,
                'Slightly dissatisfied': 202,
                'Extremely satisfied': 391
            },
            'Female;Male;Transgender;Non-binary, '
            'genderqueer, or gender non-conforming': {
                'Slightly dissatisfied': 1,
                'Moderately satisfied': 5,
                'Neither satisfied nor dissatisfied': 5,
                'Slightly satisfied': 1,
                'Extremely satisfied': 2,
                'Moderately dissatisfied': 1,
                'Extremely dissatisfied': 1
            },
            'Female;Male': {
                'Moderately satisfied': 15,
                'Slightly dissatisfied': 5,
                'Moderately dissatisfied': 10,
                'Slightly satisfied': 7,
                'Extremely dissatisfied': 2,
                'Extremely satisfied': 2,
                'Neither satisfied nor dissatisfied': 5,
                'NA': 2
            },
            'Male;Non-binary, genderqueer, or gender '
            'non-conforming': {
                'Moderately satisfied': 17,
                'Slightly satisfied': 6,
                'Moderately dissatisfied': 13,
                'Extremely satisfied': 14,
                'Extremely dissatisfied': 1,
                'Slightly dissatisfied': 8,
                'Neither satisfied nor dissatisfied': 4,
                'NA': 1
            },
            'Non-binary, genderqueer, or gender '
            'non-conforming': {
                'Slightly satisfied': 16,
                'Extremely dissatisfied': 3,
                'Moderately satisfied': 49,
                'Extremely satisfied': 26,
                'Moderately dissatisfied': 18,
                'Slightly dissatisfied': 15,
                'NA': 12,
                'Neither satisfied nor dissatisfied': 4
            },
            'Transgender': {
                'Slightly dissatisfied': 8,
                'Moderately satisfied': 13,
                'Moderately dissatisfied': 4,
                'Extremely satisfied': 7,
                'Slightly satisfied': 4,
                'Extremely dissatisfied': 4,
                'Neither satisfied nor dissatisfied': 2
            },
            'Female;Transgender': {
                'Moderately dissatisfied': 6,
                'Moderately satisfied': 15,
                'Extremely satisfied': 11,
                'NA': 3,
                'Slightly dissatisfied': 9,
                'Neither satisfied nor dissatisfied': 3,
                'Slightly satisfied': 10,
                'Extremely dissatisfied': 2
            },
            'Transgender;Non-binary, genderqueer, or '
            'gender non-conforming': {
                'Moderately satisfied': 9,
                'Extremely satisfied': 6,
                'Neither satisfied nor dissatisfied': 3,
                'Slightly satisfied': 5,
                'Slightly dissatisfied': 2,
                'Extremely dissatisfied': 1
            },
            'Female;Non-binary, genderqueer, or gender '
            'non-conforming': {
                'Moderately satisfied': 8,
                'Extremely satisfied': 6,
                'Slightly satisfied': 4,
                'Slightly dissatisfied': 2,
                'NA': 2
            },
            'Female;Transgender;Non-binary, genderqueer, '
            'or gender non-conforming': {
                'Moderately dissatisfied': 2,
                'Moderately satisfied': 3,
                'Neither satisfied nor dissatisfied': 3,
                'Slightly satisfied': 2,
                'Slightly dissatisfied': 1,
                'Extremely dissatisfied': 1
            },
            'Male;Transgender': {
                'Moderately satisfied': 6,
                'Slightly satisfied': 3,
                'Extremely satisfied': 3,
                'Slightly dissatisfied': 2,
                'Extremely dissatisfied': 1,
                'NA': 1
            },
            'Female;Male;Transgender': {
                'Slightly satisfied': 1,
                'Slightly dissatisfied': 2,
                'NA': 1,
                'Moderately satisfied': 1,
                'Moderately dissatisfied': 1,
                'Neither satisfied nor dissatisfied': 2
            },
            'Female;Male;Non-binary, genderqueer, or '
            'gender non-conforming': {
                'Moderately satisfied': 1
            },
            'Male;Transgender;Non-binary, genderqueer, or'
            ' gender non-conforming': {
                'Moderately dissatisfied': 1,
                'NA': 1,
                'Extremely satisfied': 1
            }
        }
        self.assertDictEqual(satisfaction_actual, satisfaction_expected)


if __name__ == '__main__':
    unittest.main()
