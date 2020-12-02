"""
test_median_salary_by_gender.py
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
        salary_actual = data_analysis.median_salary_by_gender(self.small_csv)
        salary_expected = {'Male': 47904}
        self.assertDictEqual(salary_actual, salary_expected)

    def test_medium_csv(self):
        """
        Csv file with 1,000 lines
        """
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
        self.assertDictEqual(salary_actual, salary_expected)

    def test_full_csv(self):
        """
        Text file with 48,000 lines
        """
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
        self.assertDictEqual(salary_actual, salary_expected)


if __name__ == '__main__':
    unittest.main()
