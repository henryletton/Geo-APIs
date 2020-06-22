# -*- coding: utf-8 -*-
"""
Title: Test Code

Author: Henry Letton

Date: 2020/06/17
"""

#%% Import any required modules 

import requests
import pandas as pd
import numpy as np

#%% Test opennotify API

# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)
# Print the status code of the response.
print(response.status_code)
print(response.content)

#%% get lat long for postcode, https://postcodes.io/

response = requests.get("http://api.postcodes.io/postcodes/ CO3 3ND")

print(response.status_code)
print(response.content)

location_details = pd.read_json(response.text)

print(location_details)

#%% get police data at long lat

parameters = {"date": "2020-02", "lat": 51.886685, "lng": 0.886988}

response = requests.post("https://data.police.uk/api/crimes-street/all-crime", params=parameters)
#response = requests.post("https://data.police.uk/api/crimes-street/all-crime?lat=53.414226&lng=-2.923026&date=2019-08")

print(response.status_code)
#print(response.content)

data = response.text

#%% convert json to dataframe

crime_df = pd.read_json(data)

crime_df.columns

print(crime_df['location'][0]['latitude'])
print(crime_df['location'][0]['longitude'])

print(crime_df.groupby('category')['category'].count())


#%% data manipulation
lonlat = crime_df.location.apply(pd.Series)
geo_data = pd.concat([crime_df['category'], lonlat[['latitude','longitude']]], axis=1)

#%% Food Standards Agency

parameters = {"latitude": 51.886685, "longitude": 0.886988, "maxDistanceLimit": 10, "pageSize": 1}
hdrs = {'x-api-version': '2'}

response = requests.get("https://api.ratings.food.gov.uk/Establishments", params=parameters, headers=hdrs)

print(response.status_code)
print(response.content)

#%% Public heatlht england - fingertips API

response = requests.get("http://fingertips.phe.org.uk/api/profiles")

print(response.status_code)

profiles = pd.read_json(response.text)

profiles['Key'].head(5)

profiles2 = profiles[profiles.Key == "general-practice"]

profiles3 = pd.DataFrame(profiles2['GroupMetadata'].values[0])






#%% Air Quality

parameters = {"coordinates": "51.886685, 0.886988", "radius": 100000, "limit": 3}

response = requests.get("https://api.openaq.org/v1/measurements", params=parameters)

print(response.status_code)

print(response.content)







