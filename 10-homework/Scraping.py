#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


response = requests.get('https://www.reuters.com/')
doc = BeautifulSoup(response.text)


# In[3]:


articles = []
titles = doc.find_all('h3')
for title in titles:
    article = {}
    article['title'] = title.text.strip()
    try:
        article['URL'] = title.find('a')['href']
    except:
        pass
    articles.append(article)


# In[4]:


top_title = doc.find(class_="story-title").text.strip()
top_url = doc.find(class_="story-title").a['href']


# In[5]:


articles.insert(0, {'title': top_title, 'URL': top_url})


# In[6]:


import pandas as pd

df = pd.DataFrame(articles)
df = df[['title', 'URL']]
df = df.dropna(subset=['title', 'URL'])



# In[7]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%Y-%m-%d-%-IPM")
date_string


# In[8]:


filename = f"briefing-{date_string}.csv"


# In[9]:


df.to_csv(filename, index=False)


# In[10]:


response = requests.post(
        "https://api.mailgun.net/v3/sandbox3bb56ce803ac4abaa01be7deebbf8b9b.mailgun.org/messages",
        auth=("api", "4a2f6fafc0380e2c2ac0ec89adbd3d9d-39bc661a-3a837b66"),
        files=[("attachment", open(filename))],
        data={"from": "Excited User <mailgun@sandbox3bb56ce803ac4abaa01be7deebbf8b9b.mailgun.org>",
              "to": ["grace.129@hotmail.com", "nl2687@columbia.edu"],
              "subject": "Here is your 6PM briefing.",
              "text": 'filename'}) 

