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


f"Right now it is {temperature} degrees out and {summary}. Today will be {temp_feeling} with a high of {high_temp} and a low of {low_temp}. {rain_warning}"


# In[8]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%B %-d, %Y")
date_string


# In[9]:


response = requests.post(
        "https://api.mailgun.net/v3/sandbox3bb56ce803ac4abaa01be7deebbf8b9b.mailgun.org/messages",
        auth=("api", "4a2f6fafc0380e2c2ac0ec89adbd3d9d-39bc661a-3a837b66"),
        data={"from": "Excited User <mailgun@sandbox3bb56ce803ac4abaa01be7deebbf8b9b.mailgun.org>",
              "to": ["grace.129@hotmail.com", "nl2687@columbia.edu"],
              "subject": f"8AM Weather forecast: {date_string}.",
              "text": f"Right now it is {temperature} degrees out and {summary}. Today will be {temp_feeling} with a high of {high_temp} and a low of {low_temp}. {rain_warning}"}) 
response.text

