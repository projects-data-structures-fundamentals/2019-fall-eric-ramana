"""
test_exercise_by_gender.py
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
        exercise_expected = {
            'Male': {
                '3 - 4 times per week': 3,
                'Daily or almost every day': 2,
                "I don't typically exercise": 3,
                '1 - 2 times per week': 1
            },
            'NA': {
                'NA': 5,
                "I don't typically exercise": 1,
                '3 - 4 times per week': 2
            },
            'Female': {
                '1 - 2 times per week': 1,
                'Daily or almost every day': 1
            }
        }
        self.assertDictEqual(exercise_actual, exercise_expected)

    def test_medium_csv(self):
        """
        Csv file with 1,000 lines
        """
        exercise_actual = data_analysis.exercise_by_gender(self.medium_csv)
        exercise_expected = {
            'Male': {
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
        self.assertDictEqual(exercise_actual, exercise_expected)

    def test_full_csv(self):
        """
        Text file with 48,000 lines
        """
        exercise_actual = data_analysis.exercise_by_gender(self.full_csv)
        exercise_expected = {
            'Male': {
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
        self.assertDictEqual(exercise_actual, exercise_expected)


if __name__ == '__main__':
    unittest.main()
