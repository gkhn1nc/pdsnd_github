import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['All','January', 'February', 'March', 'April', 'May', 'June']
weekdays = ['All','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=str(input('Please enter city name: '))
        if (city.lower()=='chicago' or city.lower()=='new york city' or city.lower()=='washington'):
            break
        else:
            print('\nPlease enter one of the 3 cities below:\n\n*chicago\n*new york city\n*washington\n')  


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=str(input('Please enter month: '))
        if (month.title() in months):
            break
        else:
            print('\nPlease try again.Enter a month\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=str(input('Please enter week day: '))
        if (day.title() in weekdays):
            break
        else:
            print('\nPlease try again.Enter a week day\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month.lower() != 'all':
        df = df[df['month'] == month.title()]
        
    if day.lower() != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('The most popular month: {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day_week=df['day_of_week'].mode()[0]
    print('The most popular week : {}'.format(popular_day_week))

    # TO DO: display the most common start hour
    popular_hour=df['Start Time'].dt.hour.mode()[0]
    print('The most popular hour : {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print("The most popular start station: ",popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print("The most popular end station: ",popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    combination= df['Start Station'].str.cat(df['End Station'], sep ="->") 
    p_comb_station=combination.mode()[0]
    print("The most popular route: ",p_comb_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration= df['Trip Duration'].fillna(0).sum()
    print("Total travel time: ",total_duration)

    # TO DO: display mean travel time
    mean_duration= df['Trip Duration'].fillna(0).mean()
    print("Mean travel time: ",mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        count_user_type = df.groupby(['User Type'])['User Type'].count()
        print("Counts of user types:\n",count_user_type)
    else:
        print("no User Type column information for this city!")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df.groupby(['Gender'])['Gender'].count()
        print("\nCounts of gender:\n",count_gender)
    else:
        print("\nno Gender column information for this city!\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth=df['Birth Year'].min()
        recent_birth=df['Birth Year'].max()
        common_birth=df['Birth Year'].mean()
        print("\nThe earliest date of birth: ",earliest_birth)
        print("\nThe newest date of birth: ",recent_birth)
        print("\nThe most common date of birth: ",common_birth)
    else:
        print("\nThe earliest date of birth: 0")
        print("\nThe newest date of birth: 0")
        print("\nThe most common date of birth: 0")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        data_req = input('\nWould you like to see the first 5 data? Enter yes or no.\n')
        if data_req.lower() =='yes':
            start=0
            end=5
            more_data='yes'
            while more_data.lower()=='yes':
                print(df[start:end])
                more_data = input('\nWould you like to see 5 more data? Enter yes or no.\n')
                start+=5
                end+=5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
