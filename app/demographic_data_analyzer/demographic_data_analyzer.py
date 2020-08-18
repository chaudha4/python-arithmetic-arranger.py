import pandas as pd
import pathlib

def calculate_demographic_data(print_data=True):

    #print(pathlib.Path().absolute())

    # Read data from file
    #df = None

    #df = pd.read_csv("/home/chaudha4/Projects/pyprojects/python-projects/app/demographic_data_analyzer/adult.data.csv")
    df = pd.read_csv("./app/demographic_data_analyzer/adult.data.csv")
    #print(df)
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()
    race_count = df.race.value_counts()        # another way

    # What is the average age of men?

    df_males = df[ (df["sex"] == "Male") ]
    average_age_men = df_males["age"].mean()

    average_age_men =  df[df.sex == "Male"].age.mean()   # another way

    average_age_men = average_age_men.item()    # Convert from numpy dtype to python dtype

    average_age_men = round(average_age_men, 1) # Round to make test pass

    # What is the percentage of people who have a Bachelor's degree?

    percentage_bachelors =  (df[df.education == "Bachelors"].education.count()) / df.education.count() * 100 

    percentage_bachelors = round(percentage_bachelors.item(), 1)  # Convert from numpy dtype to python dtype and round it to 1 decimal


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[ df.education.isin(["Bachelors", "Masters", "Doctorate"]) ]
    lower_education = df[ ~ df.education.isin(["Bachelors", "Masters", "Doctorate"]) ]         # Not is ~ , I thought it will be !

    # percentage with salary >50K
    higher_education_rich = higher_education[higher_education.salary == ">50K"].salary.count() / higher_education.salary.count() * 100
    lower_education_rich = lower_education[lower_education.salary == ">50K"].salary.count() / lower_education.salary.count() * 100

    higher_education_rich = round(higher_education_rich.item(), 1)  # Convert from numpy dtype to python dtype and round it to 1 decimal
    lower_education_rich = round(lower_education_rich.item(), 1)  # Convert from numpy dtype to python dtype and round it to 1 decimal

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[ (df["hours-per-week"] == min_work_hours) & (df.salary == ">50K")]

    rich_percentage = num_min_workers.salary.count() /  df[ (df["hours-per-week"] == min_work_hours) ].salary.count() * 100

    rich_percentage = round(rich_percentage.item(), 1)  # Convert from numpy dtype to python dtype and round it to 1 decimal

    # What country has the highest percentage of people that earn >50K?

    df1 = df.groupby(by="native-country").size()
    df2 = df[(df.salary == ">50K")].groupby(by="native-country").size()
    df3 = (df2 / df1) * 100

    highest_earning_country = df3.idxmax()
    highest_earning_country_percentage = df3.max()

    highest_earning_country_percentage = round(highest_earning_country_percentage.item(), 1)  # Convert from numpy dtype to python dtype and round it to 1 decimal

    # Identify the most popular occupation for those who earn >50K in India.

    df1 = df[(df.salary == ">50K") & (df["native-country"] == "India")]
  
    top_IN_occupation = df1.groupby(by="occupation").size().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


if __name__ == "__main__":
    ret = calculate_demographic_data(True)
    print(ret)
    print(type(ret["average_age_men"]))