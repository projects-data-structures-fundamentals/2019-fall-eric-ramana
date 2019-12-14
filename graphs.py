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

labels = ['3-4x', '4-5x', '6x', '7x', '5x', '2x']
men_means = [20, 34, 30, 35, 27, 28]
women_means = [25, 32, 34, 20, 25, 15]
trans_male_means = [1, 2, 3, 4, 5, 19]
trans_female_means = [1, 2, 3, 4, 5, 26]
trans_female_means2 = [1, 2, 3, 4, 5, 26]

x = np.arange(len(labels))  # the label locations
width = 0.18  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width*2, men_means, width, label='Men')
rects2 = ax.bar(x - width, women_means, width, label='Female')
rects3 = ax.bar(x, trans_male_means, width, label='Trans Male')
rects4 = ax.bar(x + width, trans_female_means, width, label='Trans Female')
rects5 = ax.bar(x + width*2, trans_female_means2, width, label='Trans Female222')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

if __name__ == '__main__':
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    autolabel(rects4)
    autolabel(rects5)

    plt.show()
