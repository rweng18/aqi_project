import requests
import json
import pandas as pd

## WEATHER DATA
nyc_lat = 40.7128
nyc_long = -74.0060
years = list(range(2013, 2019))
months = ['07', '12']
days = list(range(1, 32))

all_dates = []
for year in years:
    for month in months:
        for day in days:
            if day < 10:
                str_day = '0' + str(day)
            else:
                str_day = str(day)
            all_dates.append(str(year) + '-' + month + '-' + str_day + 'T23:59:59')

nyc_data = []
for date in all_dates:
    url = f'https://api.darksky.net/forecast/{darksky_api_key}/{nyc_lat},{nyc_long},{date}?exclude=currently,hourly'
    response = requests.request('GET', url, allow_redirects=False)
    
    # turns each response into a dataframe
    date_info = pd.DataFrame(json.loads(response.text)['daily']['data'])
    
    # adds date and location to each dataframe
    date_info['DATE'] = date
    date_info['CITY'] = 'NEW YORK'
    
    # appends each dataframe to a list
    nyc_data.append(date_info)
    
# concats list of dataframes into one dataframe    
nyc_data = pd.concat(nyc_data)

# saves dataframe as .csv
nyc_data.to_csv('nyc_weather_2013_2018.csv')

## FLIGHT DATA
# filter Bureau of Transport data for flights to LA and Miami
NYC_LA_MIA_201812 = pd.read_csv('nyc_2018_12.csv')
NYC_LA_MIA_201812 = NYC_LA_MIA_201812[(NYC_LA_MIA_201812['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201812['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201812['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201807 = pd.read_csv('nyc_2018_07.csv')
NYC_LA_MIA_201807 = NYC_LA_MIA_201807[(NYC_LA_MIA_201807['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201807['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201807['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201712 = pd.read_csv('nyc_2017_12.csv')
NYC_LA_MIA_201712 = NYC_LA_MIA_201712[(NYC_LA_MIA_201712['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201712['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201712['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201707 = pd.read_csv('nyc_2017_07.csv')
NYC_LA_MIA_201707 = NYC_LA_MIA_201707[(NYC_LA_MIA_201707['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201707['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201707['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201612 = pd.read_csv('nyc_2016_12.csv')
NYC_LA_MIA_201612 = NYC_LA_MIA_201612[(NYC_LA_MIA_201612['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201612['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201612['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201607 = pd.read_csv('nyc_2016_07.csv')
NYC_LA_MIA_201607 = NYC_LA_MIA_201607[(NYC_LA_MIA_201607['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201607['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201607['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201512 = pd.read_csv('nyc_2015_12.csv')
NYC_LA_MIA_201512 = NYC_LA_MIA_201512[(NYC_LA_MIA_201512['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201512['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201512['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201507 = pd.read_csv('nyc_2015_07.csv')
NYC_LA_MIA_201507 = NYC_LA_MIA_201507[(NYC_LA_MIA_201507['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201507['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201507['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201412 = pd.read_csv('nyc_2014_12.csv')
NYC_LA_MIA_201412 = NYC_LA_MIA_201412[(NYC_LA_MIA_201412['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201412['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201412['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201407 = pd.read_csv('nyc_2014_07.csv')
NYC_LA_MIA_201407 = NYC_LA_MIA_201407[(NYC_LA_MIA_201407['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201407['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201407['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201312 = pd.read_csv('nyc_2013_12.csv')
NYC_LA_MIA_201312 = NYC_LA_MIA_201312[(NYC_LA_MIA_201312['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201312['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201312['DEST_CITY_NAME'] == 'Miami, FL')]
NYC_LA_MIA_201307 = pd.read_csv('nyc_2013_07.csv')
NYC_LA_MIA_201307 = NYC_LA_MIA_201307[(NYC_LA_MIA_201307['ORIGIN_CITY_NAME'] == 'New York, NY') &
                                      (NYC_LA_MIA_201307['DEST_CITY_NAME'] == 'Los Angeles, CA') | 
                                      (NYC_LA_MIA_201307['DEST_CITY_NAME'] == 'Miami, FL')]

# combine December dfs
nyc_12flights = pd.concat([NYC_LA_MIA_201812, NYC_LA_MIA_201712, NYC_LA_MIA_201612,
                           NYC_LA_MIA_201512, NYC_LA_MIA_201412, NYC_LA_MIA_201312])
# combine July ddfs
nyc_07flights = pd.concat([NYC_LA_MIA_201807, NYC_LA_MIA_201707, NYC_LA_MIA_201607, 
                           NYC_LA_MIA_201507, NYC_LA_MIA_201407, NYC_LA_MIA_201307])

# save both dfs as .csv files
nyc_12flights.to_csv('nyc_12flights.csv')
nyc_07flights.to_csv('nyc_07flights.csv')