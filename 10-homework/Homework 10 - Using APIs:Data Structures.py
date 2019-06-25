#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.getenv("DARKSKY_API_KEY")


# In[3]:


response = requests.get(f'https://api.darksky.net/forecast/{API_KEY}/40.7128,-74.0060')
data = response.json()


# In[4]:


temperature = data['currently']['temperature']
summary = data['currently']['summary']


# In[5]:


temp_feeling = ""
high_temp = data['daily']['data'][0]["temperatureHigh"]
low_temp = data['daily']['data'][0]["temperatureLow"]
if high_temp <= 59:
    temp_feeling = "cold"
elif high_temp >= 82:
    temp_feeling = "hot"
else:
    temp_feeling = "warm"


# In[6]:


forecast = []
for hour in data['hourly']['data'][:17]:
    forecast.append(hour['icon'])
if 'rain' in forecast:
    rain_warning = 'Bring your umbrella!'
else:
    rain_warning = 'You may save the trouble of taking an umbrella.'


# In[7]:


print(f"Right now it is {temperature} degrees out and {summary}. Today will be {temp_feeling} with a high of {high_temp} and a low of {low_temp}. {rain_warning}")

