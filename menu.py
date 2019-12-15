"""
menu.py
Text-driven menus for navigation of the project.
Eric O'Neil
Ramana Kondaveeti
Created: 2019-12-14
Updated:
"""

import graphs as graph

def intro_menu():
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
    intro_menu()
    proceed = input()
    continue_running = True
    while continue_running:
        selection_menu()
        selection = input('Selection: ')
        if selection == '1':
            graph.create_graph('exercise')
            print('Based on these findings, we can conclude...')
        elif selection == '2':
            break
        elif selection == '3':
            break
        else:
            proceed = input('Sorry, that is not a valid selection. '
                            'Press any key to return to the selection screen.')
        back_to_start = input('Would you like to see another graph? Please answer \'yes\' or \'no\': ')
        if back_to_start == 'no':
            print('Thank you for using this program.')
            break
