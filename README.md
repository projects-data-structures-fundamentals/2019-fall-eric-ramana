# Stack Overflow Developer Survey Analysis Project
The Stack Overflow Developer Survey collected survey responses from thousands of developers who frequent the Stack Overflow website. In this analysis project, we seek to find out how gender has played a role in the industry today. Do wage disparities exist between genders? Does one gender report higher satisfaction ratings with their job? By visualizing and interpreting the data collected from the survey, we hope to answer these questions.

## Packages
- csv module
- matplotlib
- json module
- pandas
- statistics module
- collections module

## Driver Functions
##### average_salary_by_gender()
##### job_satisfaction_by_gender()
##### exercise_by_gender()

## Credits
- Stack Overflow 2018 Developer Survey
- Eric O'Neil
- Ramana Kondaveeti


### exercise_by_gender()
```
def exercise_by_gender(survey_csv):
    """
    Finds how often each gender exercises based on survey responses and
        adds it to a dictionary.
    Returns: nested dictionary in which the keys are genders and the values
        are a second dictionary with keys of amount of times they exercise
        and values of response numbers
    """
```
* Use `with ... as` statement to open and read from the CSV file named
  `survey_csv` as csvfile
* read the csv file as a Dictionary and store it in `reader` using class
  `DictReader`
* **accumulator**:
  * of type dictionary
  * initialized with {}
  * named `ex_dict`
  * keys are genders
  * values are dictionary with keys as amount of times they exercise and value
    as response numbers
* Assign String `Gender` to `gender`
* Assign String `Exercise` to `ex`
* **iteration** : use a for loop
  * with loop variable named `row` to iterate over reader
    * check if dictionary row keyed with `gender` is not in `ex_dict`
      * if true, add key: value pair with key as `row[gender]` and value as a dictionary
        with key as `row[ex]` and value as 1
    * else check if `row[ex]` is not in `ex_dict[row[gender]]`
      * if true, assign value `1` to dictionary ex_dict with key as `row[gender]`
        and value as dictionary with key `row[ex]`
        ```
        ex_dict[row[gender]][row[ex]] = 1
        ```
    * else, increment with 1 to dictionary ex_dict with key as `row[gender]`
      and value as dictionary with key `row[ex]`
      ```
      ex_dict[row[gender]][row[ex]] = ex_dict[row[gender]][row[ex]] + 1
      ```
* return `ex_dict`


### median_salary_by_gender()
```
def median_salary_by_gender(survey_csv):
    """
    Finds the median salary for each gender selected in the survey.
    Returns: dictionary with keys of genders and values of their average
        salary
    """
```
* Use `with ... as` statement to open and read from the CSV file named
  `survey_csv` as csvfile
* read the csv file as a Dictionary and store it in `reader` using class
  `DictReader`
* **accumulator**
  * of type dictionary
  * initialized with {}
  * named `median_salary_dict`
  * keys are genders
  * values are median of salaries corresponding to the gender
* assign and empty dictionary to `gender_salary_dict`
* assign string `ConvertedSalary` to `salary`
* assign string `Gender` to `gender`
* use a for loop with loop variable `row` to iterate over `reader`
  * check if `row[salary]` is not equal to `NA`
    * if true, convert `row[salary]` to int and store it in `salary_int`
    * check if `row[gender]` not in `gender_salary_dict`
      * if true, add key:value pair where key is `row[gender]` and value is `salary_int`
        to dictionary gender_salary_dict
      * else, add salary_int, to gender_salary_dict dictionary keyed by row[gender]
        using list method append()
* use a for loop with loop variable `gender` to iterate over `gender_salary_dict`
  * sort the dictionary gender_salary_dict with key as gender using method
    sorted() and store it in `sorted_list`
  * We use Python module statistics and its method median() applied to
    `sorted_list` and store it in a local variable `median_salary`
  * assign value `median_salary` to dictionary `median_salary_dict` with key as
    `gender`
