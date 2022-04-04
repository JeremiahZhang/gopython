import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', delimiter=',')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df_race = df.groupby('race')['age'].count().reset_index()
    df_race = df_race.set_index('race')
    race_count = df_race['age'].squeeze().sort_values(ascending=False)

    # What is the average age of men?
    df_male= df[df['sex'] == 'Male']
    average_age_men = round(df_male.age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    caseload = df.shape[0] # total
    percentage_bachelors = round(df.education.value_counts().Bachelors / caseload * 100.0, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    # people with adv education & make more than 50k
    mask = ((df['education'] == 'Bachelors') | 
            (df['education'] == 'Masters') | 
            (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')
    higher_education = df[mask].shape[0] 
    # people with adv education
    mask = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    num_higher = df[mask].shape[0] 

    # people without adv edu & make more than 50k
    mask = df['salary'] == '>50K' 
    lower_education = df[mask].shape[0] - higher_education 
    # people without adv edu
    num_lower = caseload - num_higher

    # percentage with salary >50K
    higher_education_rich = round(higher_education / num_higher * 100.0, 1)
    lower_education_rich = round(lower_education / num_lower * 100.0, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask = (df['salary'] == '>50K') & (df['hours-per-week'] == min_work_hours)
    num_min_worker_50K = int(df[mask].shape[0])
    mask = df['hours-per-week'] == min_work_hours
    total_min_worker = df[mask].shape[0]
    rich_percentage = round(num_min_worker_50K / total_min_worker * 100.0, 1)

    # What country has the highest percentage of people that earn >50K?
    # how many people of each country
    df_country_total = df.groupby(['native-country'])['age'].count().reset_index()
    df_salary = df.groupby(['native-country', 'salary'])['age'].count().reset_index()
    df_50k = df_salary[df_salary['salary'] != '>50K'].reset_index()
    df_country_total['<=50K'] = df_50k['age']
    df_country_total['per'] = (df_country_total['age'] - df_country_total['<=50K']) / df_country_total['age'] * 100.0
    mask = df_country_total['per'] == df_country_total['per'].max()
    
    highest_earning_country = df_country_total[mask]['native-country'].iloc[0]
    highest_earning_country_percentage = round(df_country_total['per'].max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask = df['salary'] == '>50K'
    df2 = df[mask].groupby(['native-country', 'occupation'])['salary'].count().reset_index()
    df3 = df2[df2['native-country'] == 'India']
    india_occ_max = df3['salary'].max()
    top_IN_occupation = df3[df3['salary'] == india_occ_max].iloc[0]['occupation']

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
