#!/usr/bin/env python
# coding: utf-8

# In[1]:


# US ACCIDENTS EXPLORATORY DATA ANALYSIS


# In[2]:


#Downloading the Data and #reading csv #almost 7.7 million records


# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[4]:


df = pd.read_csv('US_Accidents_March23.csv')


# In[5]:


df


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


# Questions in mind 
# Are there more accidents in warmer or colder areas?
# Which 5 states in USA have the highest number of accidents 
# what about the per capita as well?


# In[10]:


df.isna() #gives false if the value is present , gives true if value is absent or null


# In[11]:


df.isna().sum() #gives per column count if missing values


# In[12]:


missing_percentages = df.isna().sum().sort_values(ascending=False) / len(df)
missing_percentages


# In[13]:


missing_percentages[missing_percentages != 0].plot(kind='barh') 
#gives us only the columns which have missing values


# In[14]:


#now we can remove the columns which are missing more than 40 percent of the times


# In[15]:


df.columns


# In[16]:


df.City


# In[17]:


cities = df.City.unique() #checking unique cities
len(cities)


# In[18]:


# now will look at the top cities with max accidents number


# In[19]:


cities_by_accident = df.City.value_counts()
cities_by_accident


# In[20]:


cities_by_accident[:20]


# In[21]:


#Why does New York count so much lower if it is the most populated city in USA?


# In[22]:


df[df['City'] == 'New York']


# In[23]:


'NY' in df.State


# In[24]:


cities_by_accident[:30].plot(kind='barh')


# In[25]:


sns.set_style("darkgrid")


# In[26]:


sns.distplot(cities_by_accident)


# In[27]:


#here we can see that most of the cities have less than 2000 accidents, bcos it shows the frequency of accidents by city


# In[28]:


high_accident_cities = cities_by_accident[cities_by_accident>=1000]
low_accident_cities = cities_by_accident[cities_by_accident<1000]


# In[29]:


len(high_accident_cities)


# In[30]:


len(high_accident_cities)/len(cities)


# In[31]:


#insights 
#less than 9 percent of the cities have accidents more than 1000
#no of accidents per city decreases exponentially 
#


# In[32]:


sns.displot(high_accident_cities)


# In[33]:


sns.histplot(low_accident_cities, log_scale=True) 
#bcos the graph is exponential we use log scale


# In[34]:


# Exploring start time column now


# In[38]:


df.columns


# In[40]:


df.Start_Time


# In[41]:


pd.to_datetime(df.Start_Time)


# In[43]:


df.Start_Time = pd.to_datetime(df.Start_Time)


# In[45]:


df.Start_Time.dt.hour #to get the hours from the timestamps


# In[51]:


sns.displot(df.Start_Time.dt.hour, bins=24, kde = False ) #norm hist used to get the percentages


# In[52]:


# As we can see from the graph, a high percentage of accidents occur between 6 to 10 am ( maybe due to work)
# Next highest is 3 pm to 6 pm


# In[53]:


sns.displot(df.Start_Time.dt.dayofweek, bins=24, kde = False ) #norm hist used to get the percentages


# In[54]:


# as we can see on weekends as people travel less so , is accident lower

# Now we can check is the dsitribution of accidents by hour the same on weekends the same on weekdays?


# In[63]:


sundays_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 6]


# In[64]:


sns.displot(sundays_start_time.dt.hour, bins=24, kde = False )


# In[65]:


#in the above graph as we can see the accidents are spread out throughout the day


# In[66]:


monday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 0]


# In[67]:


sns.displot(monday_start_time.dt.hour, bins=24, kde = False )


# In[68]:


#whereas in moonday as we can see the chart is peaking towards morning and evening 


# In[69]:


# Now lets check for months as well


# In[74]:


sns.displot(df.Start_Time.dt.month, bins=12, kde = False )


# In[73]:


# throughout the year, we can see that during the summers the accidents are lower, but in winter months they are higher
# this maybe due to snow in winters and slipping of vehicles, during summers people like to stay indoors mainly


# In[ ]:




