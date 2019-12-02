"""
data_analysis.py
Functions for collecting csv data and interpreting it.
Eric O'Neil
Ramana Kondaveeti
Created: 2019-12-01
Updated:
"""

import csv
import json
import statistics

class Analysis(object):
    """
    Contains functions for working with survey_results_public.csv
    """

    survey_csv = 'C:\\Users\\ecoun\\OneDrive\\Desktop\\survey_results_public.csv'
    # survey_csv = 'test_survey.csv'

    def exercise_by_gender(self):
        """
        Finds how often each gender exercises based on survey responses and
            adds it to a dictionary.
        Returns: nested dictionary in which the keys are genders and the values
            are a second dictionary with keys of amount of times they exercise
            and values of response numbers
        """
        with open(Analysis.survey_csv, 'r', encoding='cp1252', errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            exercise_dict = {}
            for row in reader:
                if row['Gender'] not in exercise_dict:
                    exercise_dict[row['Gender']] = {row['Exercise']: 1}
                elif row['Exercise'] not in exercise_dict[row['Gender']]:
                    exercise_dict[row['Gender']][row['Exercise']] = 1
                else:
                    exercise_dict[row['Gender']][row['Exercise']] = exercise_dict[row['Gender']][row['Exercise']] + 1
        return exercise_dict

    def median_salary_by_gender(self):
        """
        Finds the median salary for each gender selected in the survey.
        Returns: dictionary with keys of genders and values of their average
            salary
        """
        with open(Analysis.survey_csv, 'r', encoding='cp1252', errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            median_salary_dict = {}
            gender_salary_dict = {}
            for row in reader:
                if row['ConvertedSalary'] != 'NA':
                    salary_int = int(float(row['ConvertedSalary']))
                    if row['Gender'] not in gender_salary_dict:
                        gender_salary_dict[row['Gender']] = [salary_int]
                    else:
                        gender_salary_dict[row['Gender']].append(salary_int)
            for gender in gender_salary_dict:
                sorted_list = sorted(gender_salary_dict[gender])
                median_salary = int(statistics.median(sorted_list))
                median_salary_dict[gender] = median_salary
        return median_salary_dict

    def job_satisfaction_by_gender(self):
        """
        Creates a dictionary of job satisfaction responses for each gender.
        Returns: dictionary with keys of genders and values of a nested
            dictionary containing keys of job satisfaction with values of how
            many respondents chose that option
        """
        with open(Analysis.survey_csv, 'r', encoding='cp1252', errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            job_satisfaction_dict = {}
            for row in reader:
                if row['Gender'] not in job_satisfaction_dict:
                    job_satisfaction_dict[row['Gender']] = {row['JobSatisfaction']: 1}
                elif row['JobSatisfaction'] not in job_satisfaction_dict[row['Gender']]:
                    job_satisfaction_dict[row['Gender']][row['JobSatisfaction']] = 1
                else:
                    job_satisfaction_dict[row['Gender']][row['JobSatisfaction']] = job_satisfaction_dict[row['Gender']][row['JobSatisfaction']] + 1
        return job_satisfaction_dict


if __name__ == '__main__':
    analysis = Analysis()
    # print(json.dumps(analysis.exercise_by_gender(), indent=1))
    # print(json.dumps(analysis.median_salary_by_gender(), indent=1))
    print(json.dumps(analysis.job_satisfaction_by_gender(), indent=1))
