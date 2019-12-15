"""
menu.py
Text-driven menus for navigation of the project.
Eric O'Neil
Ramana Kondaveeti
Created: 2019-12-14
Updated: 2019-12-15
"""

import graphs as graph
import data_analysis as analysis


def intro_menu():
    """
    Creates an introductory text GUI for the project.
    """
    print('+----------------------------------------------------------------+')
    print('|                                                                |')
    print('|                                                                |')
    print('|            Stack Overflow Developer Survey Project             |')
    print('|                                                                |')
    print('|                                                                |')
    print('|                       Eric O\'Neil                              |')
    print('|                                                                |')
    print('|                            &                                   |')
    print('|                                                                |')
    print('|                     Ramana Kondaveeti                          |')
    print('|                                                                |')
    print('|                   Press enter to continue                      |')
    print('|                                                                |')
    print('+----------------------------------------------------------------+')


def selection_menu():
    """
    Creates a text GUI for selection of program modules.
    """
    print('+----------------------------------------------------------------+')
    print('|                                                                |')
    print('|                                                                |')
    print('|   Please select a question by typing its corresponding number  |')
    print('|                                                                |')
    print('|            1. How often does each gender exercise?             |')
    print('|                                                                |')
    print('|            2. What is the median salary by gender?             |')
    print('|                                                                |')
    print('|    3. How satisfied is each gender with its career choice?     |')
    print('|                                                                |')
    print('|                                                                |')
    print('|                                                                |')
    print('|                                                                |')
    print('+----------------------------------------------------------------+')


def program_run():
    """
    Executes the program in a text-driven manner from the console allowing
        user selection to drive data analysis.
    """
    intro_menu()
    proceed = input()
    continue_running = True
    while continue_running:
        selection_menu()
        print('Accumulating data for graphs and interpreting it may take up '
              'to 10 seconds. Please be patient!')
        selection = input('Selection: ')
        if selection == '1':
            graph.create_graph('exercise')
            print('Based on these findings, we found that the top three '
                  ' genders that exercise at least once a week are: '
                  + analysis.top_exercisers_by_gender(
                        analysis.exercise_by_gender()
                    )
                  + 'based on the csv data.\n')
        elif selection == '2':
            graph.create_graph('salary')
            print('Based on these findings, we found that the top three '
                  'genders with the highest salaries are: '
                  + analysis.top_earners_by_gender(
                    analysis.median_salary_by_gender()
                    )
                  + 'based on the csv data.\n')
        elif selection == '3':
            graph.create_graph('job satisfaction')
            print('Based on these findings, we found that the top three '
                  'genders that are at least slightly satisfied with their '
                  'jobs are: '
                  + analysis.happiest_genders_by_job(
                        analysis.job_satisfaction_by_gender()
                    )
                  + 'based on the csv data.\n')
        else:
            proceed = input('Sorry, that is not a valid selection. '
                            'Press any key to return to the selection screen.')
        back_to_start = input('Would you like to see another graph? Please '
                              'answer \'yes\' or \'no\': ')
        if back_to_start == 'no':
            print('Thank you for using this program.')
            break
