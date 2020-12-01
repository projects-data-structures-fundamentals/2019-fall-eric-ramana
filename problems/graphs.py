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
    survey_csv = 'survey_results_public_modified.csv'
    if type_of_data == 'exercise':
        working_dict = analysis.exercise_by_gender(survey_csv)
        data_frame = pd.DataFrame(working_dict)
        ax_plot = data_frame.plot(
            kind="bar",
            rot=0,
            title="Exercise Frequency By Gender",
            colormap='tab20'
        )
        for patch in ax_plot.patches:
            ax_plot.annotate(
                patch.get_height(),
                (patch.get_x() + patch.get_width() / 2.,
                    patch.get_height()),
                ha='center', va='center',
                xytext=(0, 10), textcoords='offset points'
            )
        plt.show()
    elif type_of_data == 'salary':
        working_dict = analysis.median_salary_by_gender(survey_csv)
        index = ['Genders']
        data_frame = pd.DataFrame(working_dict, index=index)
        ax_plot = data_frame.plot(
            kind="bar",
            rot=0,
            title="Median Salary By Gender",
            colormap='tab20'
        )
        for patch in ax_plot.patches:
            ax_plot.annotate(
                patch.get_height(),
                (patch.get_x() + patch.get_width() / 2.,
                    patch.get_height()),
                ha='center', va='center',
                xytext=(0, 10), textcoords='offset points'
            )
        plt.show()
    elif type_of_data == 'job satisfaction':
        working_dict = analysis.job_satisfaction_by_gender(survey_csv)
        data_frame = pd.DataFrame(working_dict)
        ax_plot = data_frame.plot(
            kind="bar",
            rot=0,
            title="Job Satisfaction By Gender",
            colormap='tab20'
        )
        for patch in ax_plot.patches:
            ax_plot.annotate(
                patch.get_height(),
                (patch.get_x() + patch.get_width() / 2.,
                    patch.get_height()),
                ha='center', va='center',
                xytext=(0, 10), textcoords='offset points'
            )
        plt.show()
