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
from collections import Counter


survey_csv = 'C:\\Users\\ecoun\\OneDrive\\Desktop\\survey_results_public.csv'
# survey_csv = 'test_survey.csv'


def exercise_by_gender():
    """
    Finds how often each gender exercises based on survey responses and
        adds it to a dictionary.
    Returns: nested dictionary in which the keys are genders and the values
        are a second dictionary with keys of amount of times they exercise
        and values of response numbers
    """
    with open(survey_csv, 'r', encoding='cp1252', errors='ignore') as csvfile:
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


def top_exercisers_by_gender(exercise_dict):
    """
    Accumulates the top three genders that exercise into a string to be
        concatenated with other findings.
    Returns: string with genders and their associated percent of how many
        exercise at least once per week
    """
    top_exercisers = {}
    top_three_exercisers = ''
    for gender in exercise_dict:
        exercisers = 0
        total_respondents = 0
        for key in exercise_dict[gender]:
            if key == '1 - 2 times per week':
                exercisers = exercisers + exercise_dict[gender][key]
                total_respondents = total_respondents + exercise_dict[gender][key]
            elif key == '3 - 4 times per week':
                exercisers = exercisers + exercise_dict[gender][key]
                total_respondents = total_respondents + exercise_dict[gender][key]
            elif key == 'Daily or almost every day':
                exercisers = exercisers + exercise_dict[gender][key]
                total_respondents = total_respondents + exercise_dict[gender][key]
            else:
                total_respondents = total_respondents + exercise_dict[gender][key]
            percent_exercised_each_week = "{0:.1f}".format(((exercisers / total_respondents) * 100)) + '%'
            top_exercisers[gender] = percent_exercised_each_week
    accumulator = Counter(top_exercisers)
    top = accumulator.most_common(3)
    for gender in top:
        top_three_exercisers = top_three_exercisers + '{} {}, '.format(gender[0], gender[1])
    return top_three_exercisers


def median_salary_by_gender():
    """
    Finds the median salary for each gender selected in the survey.
    Returns: dictionary with keys of genders and values of their average
        salary
    """
    with open(survey_csv, 'r', encoding='cp1252', errors='ignore') as csvfile:
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


def top_earners_by_gender(median_salary_dict):
    """
    Accumulates the top three genders that earn the highest salaries into a
        string to be concatenated.
    Returns: string with genders and their associated salaries per year
    """
    top_three_earners = ''
    accumulator = Counter(median_salary_dict)
    top_earners = accumulator.most_common(3)
    for gender in top_earners:
        top_three_earners = top_three_earners + '{} {}, '.format(gender[0], gender[1])
    return top_three_earners


def job_satisfaction_by_gender():
    """
    Creates a dictionary of job satisfaction responses for each gender.
    Returns: dictionary with keys of genders and values of a nested
        dictionary containing keys of job satisfaction with values of how
        many respondents chose that option
    """
    with open(survey_csv, 'r', encoding='cp1252', errors='ignore') as csvfile:
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


def happiest_genders_by_job(job_satisfaction_dict):
    """
    Accumulates the top three genders that are at least slightly satisfied
        with their job into a string to be concatenated.
    Returns: string with genders and the percent of how many of them are at
        least slightly satisfied with their job
    """
    happiest_genders = {}
    top_three_happiest = ''
    for gender in job_satisfaction_dict:
        satisfied = 0
        total_respondents = 0
        for key in job_satisfaction_dict[gender]:
            if key == 'Extremely satisfied':
                satisfied = satisfied + job_satisfaction_dict[gender][key]
                total_respondents = total_respondents + job_satisfaction_dict[gender][key]
            elif key == 'Moderately satisfied':
                satisfied = satisfied + job_satisfaction_dict[gender][key]
                total_respondents = total_respondents + job_satisfaction_dict[gender][key]
            elif key == 'Slightly satisfied':
                satisfied = satisfied + job_satisfaction_dict[gender][key]
                total_respondents = total_respondents + job_satisfaction_dict[gender][key]
            else:
                total_respondents = total_respondents + job_satisfaction_dict[gender][key]
            percent_happiest = "{0:.1f}".format(((satisfied / total_respondents) * 100)) + '%'
            happiest_genders[gender] = percent_happiest
    accumulator = Counter(happiest_genders)
    top_happiest = accumulator.most_common(3)
    for gender in top_happiest:
        top_three_happiest = top_three_happiest + '{} {}, '.format(gender[0], gender[1])
    return top_three_happiest
