"""
tests.py
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
        exercise_actual = data_analysis.exercise_by_gender(self.small_csv)
        exercise_expected = {'Male':
                                {'3 - 4 times per week': 3,
                                'Daily or almost every day': 2,
                                "I don't typically exercise": 3,
                                '1 - 2 times per week': 1},
                           'NA':
                                {'NA': 5,
                                "I don't typically exercise": 1,
                                '3 - 4 times per week': 2},
                           'Female':
                                {'1 - 2 times per week': 1,
                                 'Daily or almost every day': 1}
                                }
        salary_actual = data_analysis.median_salary_by_gender(self.small_csv)
        salary_expected = {'Male': 47904}
        satisfaction_actual = data_analysis.job_satisfaction_by_gender(self.small_csv)
        satisfaction_expected = {'Male':
                                    {'Extremely satisfied': 1,
                                     'Moderately dissatisfied': 1,
                                     'Neither satisfied nor dissatisfied': 2,
                                     'Slightly satisfied': 2,
                                     'Moderately satisfied': 3},
                                 'NA':
                                    {'Moderately satisfied': 1,
                                     'NA': 4,
                                     'Moderately dissatisfied': 2,
                                     'Extremely satisfied': 1},
                                'Female':
                                    {'Slightly satisfied': 2}}
        self.assertEqual(exercise_actual, exercise_expected)
        self.assertEqual(salary_actual, salary_expected)
        self.assertEqual(satisfaction_actual, satisfaction_expected)

    def test_medium_csv(self):
        """
        Csv file with 1,000 lines
        """
        exercise_actual = data_analysis.exercise_by_gender(self.medium_csv)
        exercise_expected = {'Male': {
                                '3 - 4 times per week': 139,
                                'Daily or almost every day': 90,
                                "I don't typically exercise": 237,
                                '1 - 2 times per week': 163,
                                'NA': 3
                                },
                             'NA': {
                                'NA': 234,
                                "I don't typically exercise": 28,
                                '3 - 4 times per week': 13,
                                '1 - 2 times per week': 22,
                                'Daily or almost every day': 9
                                },
                             'Female': {
                                '1 - 2 times per week': 18,
                                'Daily or almost every day': 12,
                                "I don't typically exercise": 16,
                                '3 - 4 times per week': 7
                                },
                             'Female;Male;Transgender;Non-binary, genderqueer,'
                             ' or gender non-conforming': {
                                "I don't typically exercise": 1
                                },
                             'Female;Male': {
                                'Daily or almost every day': 1,
                                "I don't typically exercise": 1
                                },
                             'Male;Non-binary, genderqueer, or gender '
                             'non-conforming': {
                                'Daily or almost every day': 1
                                },
                             'Non-binary, genderqueer, or gender '
                             'non-conforming': {
                                "I don't typically exercise": 1
                                },
                             'Transgender': {
                                "I don't typically exercise": 1,
                                'Daily or almost every day': 1
                                },
                             'Female;Transgender': {
                                '1 - 2 times per week': 1
                                }
                            }
        salary_actual = data_analysis.median_salary_by_gender(self.medium_csv)
        salary_expected = {'Male': 53000,
                           'Female;Male;Transgender;Non-binary, genderqueer, '
                           'or gender non-conforming': 75000,
                           'Female;Male': 10958,
                           'Female': 53346,
                           'Male;Non-binary, genderqueer, or gender '
                           'non-conforming': 90000,
                           'NA': 36005,
                           'Non-binary, genderqueer, or gender '
                           'non-conforming': 684000,
                           'Transgender': 56224,
                           'Female;Transgender': 85000
                           }
        satisfaction_actual = data_analysis.job_satisfaction_by_gender(self.medium_csv)
        satisfaction_expected = {'Male': {
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
        self.assertEqual(exercise_actual, exercise_expected)
        self.assertEqual(salary_actual, salary_expected)
        self.assertEqual(satisfaction_actual, satisfaction_expected)

    def test_full_csv(self):
        """
        Text file with 48,000 lines
        """
        exercise_actual = data_analysis.exercise_by_gender(self.full_csv)
        exercise_expected = {'Male': {
                                '3 - 4 times per week': 6356,
                                'Daily or almost every day': 3952,
                                "I don't typically exercise": 11567,
                                '1 - 2 times per week': 9021,
                                'NA': 207
                                },
                             'NA': {
                                'NA': 10429,
                                "I don't typically exercise": 1493,
                                '3 - 4 times per week': 713,
                                '1 - 2 times per week': 1117,
                                'Daily or almost every day': 541
                                },
                             'Female': {
                                '1 - 2 times per week': 697,
                                'Daily or almost every day': 262,
                                "I don't typically exercise": 706,
                                '3 - 4 times per week': 462, 'NA': 16
                                },
                             'Female;Male;Transgender;Non-binary, genderqueer,'
                             ' or gender non-conforming': {
                                "I don't typically exercise": 8,
                                '3 - 4 times per week': 2,
                                '1 - 2 times per week': 4,
                                'Daily or almost every day': 2
                                },
                             'Female;Male': {
                                'Daily or almost every day': 13,
                                "I don't typically exercise": 13,
                                '3 - 4 times per week': 10,
                                '1 - 2 times per week': 12
                                },
                             'Male;Non-binary, genderqueer, or gender '
                             'non-conforming': {
                                'Daily or almost every day': 10,
                                '1 - 2 times per week': 20,
                                "I don't typically exercise": 21,
                                '3 - 4 times per week': 13
                                },
                             'Non-binary, genderqueer, or gender '
                             'non-conforming': {
                                "I don't typically exercise": 60,
                                '3 - 4 times per week': 24,
                                '1 - 2 times per week': 45,
                                'Daily or almost every day': 14
                                },
                             'Transgender': {
                                "I don't typically exercise": 17,
                                'Daily or almost every day': 8,
                                '3 - 4 times per week': 5,
                                '1 - 2 times per week': 12
                                },
                             'Female;Transgender': {
                                '1 - 2 times per week': 12,
                                "I don't typically exercise": 32,
                                '3 - 4 times per week': 8,
                                'Daily or almost every day': 7
                                },
                             'Transgender;Non-binary, genderqueer, or gender '
                             'non-conforming': {
                                "I don't typically exercise": 10,
                                '3 - 4 times per week': 6,
                                '1 - 2 times per week': 6,
                                'Daily or almost every day': 4
                                },
                             'Female;Non-binary, genderqueer, or gender '
                             'non-conforming': {
                                '1 - 2 times per week': 6,
                                "I don't typically exercise": 6,
                                'Daily or almost every day': 7,
                                '3 - 4 times per week': 3
                                },
                             'Female;Transgender;Non-binary, genderqueer, or '
                             'gender non-conforming': {
                                "I don't typically exercise": 5,
                                '1 - 2 times per week': 4,
                                'Daily or almost every day': 3
                                },
                             'Male;Transgender': {
                                '3 - 4 times per week': 4,
                                '1 - 2 times per week': 7,
                                'Daily or almost every day': 2,
                                "I don't typically exercise": 3
                                },
                             'Female;Male;Transgender': {
                                'Daily or almost every day': 1,
                                '3 - 4 times per week': 1,
                                '1 - 2 times per week': 4,
                                "I don't typically exercise": 2
                                },
                             'Female;Male;Non-binary, genderqueer, or gender '
                             'non-conforming': {
                                '1 - 2 times per week': 1
                                },
                             'Male;Transgender;Non-binary, genderqueer, or '
                             'gender non-conforming': {
                                '3 - 4 times per week': 1,
                                "I don't typically exercise": 2
                                }
                            }
        salary_actual = data_analysis.median_salary_by_gender(self.full_csv)
        salary_expected = {'Male': 58340,
                           'Female;Male;Transgender;Non-binary, genderqueer, '
                           'or gender non-conforming': 29664,
                           'Female;Male': 23220,
                           'Female': 57276,
                           'Male;Non-binary, genderqueer, or gender '
                           'non-conforming': 45283,
                           'NA': 44064,
                           'Non-binary, genderqueer, or gender '
                           'non-conforming': 66117,
                           'Transgender': 57500,
                           'Female;Transgender': 75747,
                           'Transgender;Non-binary, genderqueer, or gender '
                           'non-conforming': 75000,
                           'Female;Non-binary, genderqueer, or gender '
                           'non-conforming': 85000,
                           'Female;Transgender;Non-binary, genderqueer, or '
                           'gender non-conforming': 77500,
                           'Male;Transgender': 75000,
                           'Female;Male;Non-binary, genderqueer, or gender '
                           'non-conforming': 47984,
                           'Male;Transgender;Non-binary, genderqueer, or '
                           'gender non-conforming': 115000,
                           'Female;Male;Transgender': 6387
                           }
        satisfaction_actual = data_analysis.job_satisfaction_by_gender(self.full_csv)
        satisfaction_expected = {'Male': {
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
        self.assertEqual(exercise_actual, exercise_expected)
        self.assertEqual(salary_actual, salary_expected)
        self.assertEqual(satisfaction_actual, satisfaction_expected)


if __name__ == '__main__':
    unittest.main()
