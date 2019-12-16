"""
graphs.py
Functions for graphing the csv data.
Eric O'Neil
Ramana Kondaveeti
Created: 2019-12-14
Updated: 2019-12-15
"""

import matplotlib
import matplotlib.pyplot as plt
import data_analysis as analysis
import pandas as pd


def create_graph(type_of_data):
    """
    Creates a graph of data from the Stack Overflow Developer Survey based on
        the option selected by the user. Presents the graph on the user's
        screen.
    """
    if type_of_data == 'exercise':
        working_dict = analysis.exercise_by_gender()
        df = pd.DataFrame(working_dict)
        ax = df.plot(kind="bar",
                     rot=0,
                     title="Exercise Frequency By Gender",
                     colormap='tab20')
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x() + p.get_width() / 2.,
                        p.get_height()), ha='center', va='center',
                        xytext=(0, 10), textcoords='offset points')
        plt.show()
    elif type_of_data == 'salary':
        working_dict = analysis.median_salary_by_gender()
        index = ['Genders']
        df = pd.DataFrame(working_dict, index=index)
        ax = df.plot(kind="bar",
                     rot=0,
                     title="Median Salary By Gender",
                     colormap='tab20')
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x() + p.get_width() / 2.,
                        p.get_height()), ha='center', va='center',
                        xytext=(0, 10), textcoords='offset points')
        plt.show()
    elif type_of_data == 'job satisfaction':
        working_dict = analysis.job_satisfaction_by_gender()
        df = pd.DataFrame(working_dict)
        ax = df.plot(kind="bar",
                     rot=0,
                     title="Job Satisfaction By Gender",
                     colormap='tab20')
        for p in ax.patches:
            ax.annotate(p.get_height(), (p.get_x() + p.get_width() / 2.,
                        p.get_height()), ha='center', va='center',
                        xytext=(0, 10), textcoords='offset points')
        plt.show()
