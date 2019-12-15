"""
graphs.py
Functions for graphing the csv data.
Eric O'Neil
Ramana Kondaveeti
Created: 2019-12-14
Updated:
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import data_analysis as analysis
import pandas as pd

def create_graph(type_of_data):
    if type_of_data == 'exercise':
        exercise_dict = analysis.exercise_by_gender()

    df = pd.DataFrame(exercise_dict)

    ax = df.plot(kind="bar", rot=0, title="Exercise Frequency")
    for p in ax.patches:
        ax.annotate(p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    plt.show()
