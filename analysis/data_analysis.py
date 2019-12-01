"""
data_analysis.py
Functions for collecting csv data and interpreting it.
Eric O'Neil
Ramana Kondaveeti
Created: 2019-12-01
Updated:
"""
import csv

class Analysis(object):
    """
    Contains functions for working with survey_results_public.csv
    """

    def exercise_by_gender(self, filename):
        """
        Finds how often each gender exercises based on survey responses and
            adds it to a dictionary.
        filename: string that has the name of the CSV file
        Returns: nested dictionary in which the keys are genders and the values
            are a second dictionary with keys of amount of times they exercise
            and values of response numbers
        """
