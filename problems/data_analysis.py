"""
data_analysis.py
Functions for collecting csv data and interpreting it.
Eric O'Neil
Ramana Kondaveeti
Created: 2019-12-01
Updated: 2019-12-15
"""

import csv
import json
import statistics
from collections import Counter


def exercise_by_gender(survey_csv):
    """
    Finds how often each gender exercises based on survey responses and
        adds it to a dictionary.
    Returns: nested dictionary in which the keys are genders and the values
        are a second dictionary with keys of amount of times they exercise
        and values of response numbers
    """
    with open(survey_csv, 'r', encoding='cp1252', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        ex_dict = {}
        gender = 'Gender'
        exercise = 'Exercise'
        for row in reader:
            if row[gender] not in ex_dict:
                ex_dict[row[gender]] = {row[exercise]: 1}
            elif row[exercise] not in ex_dict[row[gender]]:
                ex_dict[row[gender]][row[exercise]] = 1
            else:
                ex_dict[row[gender]][row[exercise]] = ex_dict[row[gender]][row[exercise]] + 1
    return ex_dict


def top_exercisers_by_gender(exercise_dict):
    """
    Accumulates the top three genders that exercise into a string to be
        concatenated with other findings.
    exercise_dict: a dictionary with keys of genders and values of a nested
        dictionary including keys of how often the gender exercises and values
        of the number of respondents
    Returns: string with genders and their associated percent of how many
        exercise at least once per week
    """
    top_exercisers = {}
    top_three = ''
    for gender in exercise_dict:
        exercisers = 0
        total = 0
        for key in exercise_dict[gender]:
            if key == '1 - 2 times per week':
                exercisers = exercisers + exercise_dict[gender][key]
                total = total + exercise_dict[gender][key]
            elif key == '3 - 4 times per week':
                exercisers = exercisers + exercise_dict[gender][key]
                total = total + exercise_dict[gender][key]
            elif key == 'Daily or almost every day':
                exercisers = exercisers + exercise_dict[gender][key]
                total = total + exercise_dict[gender][key]
            else:
                total = total + exercise_dict[gender][key]
            pct_ex = "{0:.1f}".format(((exercisers / total) * 100)) + '%'
            top_exercisers[gender] = pct_ex
    accumulator = Counter(top_exercisers)
    top = accumulator.most_common(3)
    for gender in top:
        top_three = top_three + '{} {}, '.format(gender[0], gender[1])
    return top_three


def median_salary_by_gender(survey_csv):
    """
    Finds the median salary for each gender selected in the survey.
    Returns: dictionary with keys of genders and values of their average
        salary
    """
    with open(survey_csv, 'r', encoding='cp1252', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        median_salary_dict = {}
        gender_salary_dict = {}
        salary = 'ConvertedSalary'
        gender = 'Gender'
        for row in reader:
            if row[salary] != 'NA':
                salary_int = int(float(row[salary]))
                if row[gender] not in gender_salary_dict:
                    gender_salary_dict[row[gender]] = [salary_int]
                else:
                    gender_salary_dict[row[gender]].append(salary_int)
        for gender in gender_salary_dict:
            sorted_list = sorted(gender_salary_dict[gender])
            median_salary = int(statistics.median(sorted_list))
            median_salary_dict[gender] = median_salary
    return median_salary_dict


def top_earners_by_gender(median_salary_dict):
    """
    Accumulates the top three genders that earn the highest salaries into a
        string to be concatenated.
    median_salary_dict: dictionary with keys of genders and values of their
        median salary obtained from the csv
    Returns: string with genders and their associated salaries per year
    """
    three_earners = ''
    accumulator = Counter(median_salary_dict)
    top_earners = accumulator.most_common(3)
    for gender in top_earners:
        three_earners = three_earners + '{} {}, '.format(gender[0], gender[1])
    return three_earners


def job_satisfaction_by_gender(survey_csv):
    """
    Creates a dictionary of job satisfaction responses for each gender.
    Returns: dictionary with keys of genders and values of a nested
        dictionary containing keys of job satisfaction with values of how
        many respondents chose that option
    """
    with open(survey_csv, 'r', encoding='cp1252', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        satis_dict = {}
        gender = 'Gender'
        job = 'JobSatisfaction'
        for row in reader:
            if row[gender] not in satis_dict:
                satis_dict[row[gender]] = {row[job]: 1}
            elif row[job] not in satis_dict[row[gender]]:
                satis_dict[row[gender]][row[job]] = 1
            else:
                satis_dict[row[gender]][row[job]] = satis_dict[row[gender]][row[job]] + 1
    return satis_dict


def happiest_genders_by_job(satisfaction_dict):
    """
    Accumulates the top three genders that are at least slightly satisfied
        with their job into a string to be concatenated.
    satisfaction_dict: dictionary with keys of genders and values of a
        nested dictionary which includes keys of job satisfaction and values of
        response numbers
    Returns: string with genders and the percent of how many of them are at
        least slightly satisfied with their job
    """
    happiest_genders = {}
    three_happiest = ''
    for gender in satisfaction_dict:
        satisfied = 0
        total = 0
        for key in satisfaction_dict[gender]:
            if key == 'Extremely satisfied':
                satisfied = satisfied + satisfaction_dict[gender][key]
                total = total + satisfaction_dict[gender][key]
            elif key == 'Moderately satisfied':
                satisfied = satisfied + satisfaction_dict[gender][key]
                total = total + satisfaction_dict[gender][key]
            elif key == 'Slightly satisfied':
                satisfied = satisfied + satisfaction_dict[gender][key]
                total = total + satisfaction_dict[gender][key]
            else:
                total = total + satisfaction_dict[gender][key]
            pct_happy = "{0:.1f}".format(((satisfied / total) * 100)) + '%'
            happiest_genders[gender] = pct_happy
    accumulator = Counter(happiest_genders)
    top_happiest = accumulator.most_common(3)
    for gender in top_happiest:
        three_happiest = three_happiest + '{} {}, '.format(
                                                        gender[0], gender[1]
                                                    )
    return three_happiest
