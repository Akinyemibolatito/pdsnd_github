#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[8]:


df1 = pd.read_csv('chicago.csv')
df2 = pd.read_csv('new_york_city.csv')
df3 = pd.read_csv('washington.csv')


# In[9]:


df3.head()


# In[91]:


df = pd.concat([df1,df2,df3]).reset_index()


# In[93]:


#most common year of birth
    df['Year_Of_Birth'] = pd.to_datetime(df['Birth Year']).dt.year
    popular_year = df['year_of_Birth'].mode()[0] 
     print (popular_year) 


# In[32]:


print(dfnew)


# In[34]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


# In[42]:


# TO DO: display the most common month
   
df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract hour from the Start Time column to create an hour column
df['month'] = pd.to_datetime(df['Start Time']).dt.month
# find the most common month 
common_month = df['month'].mode()[0]
   
print('Most Frequent Start month:', common_month)


# In[44]:


# TO DO: display the most common day of week
   
df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.day
common_day_of_week = df['day_of_week'].mode()[0]
   
print('Most Frequent Start day:', common_day_of_week)


# In[47]:


# TO DO: display the most common start hour
df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
most_common_hour = df['hour'].mode()[0]
   
print('Most Frequent Start hour:', most_common_hour)


# In[57]:


# TO DO: display most commonly used start station
    
common_start_station = df['Start Station'].mode()[0]
print ('Most Popular Start station:', common_start_station)


# In[62]:


# TO DO: display most commonly used end station
common_end_station = df['End Station'].mode()[0]
print ('Most Popular end station:', common_end_station)


# In[108]:


df ['start end station'] = df ['Start Station'] + df ['End Station']
common_start_end_station = df['start end station'].mode()[0]
print ('Most Popular sta rt end station:', common_start_end_station)


# In[73]:
# TO DO: display total travel time
#change the start time to hours and rename and change the end time to hours and rename then do a difference btw d 2 columns
total_travel_time = df['Trip Duration'].sum()
print ('total travel time:',total_travel_time)


# In[75]:


# TO DO: display mean travel time
mean_travel_time = df['Trip Duration'].mean()
print('mean_travel_time:', mean_travel_time)


# In[78]:


# TO DO: Display counts of user types
user_types = df['User Type'].value_counts()

print(user_types)


# In[80]:


# TO DO: Display counts of gender
Gender = df['Gender'].value_counts()
print(Gender)


# In[99]:


#filter output first by column ID and then get min and max
 # Earliest year of birth
Earliest = df['Birth Year'].min()
print(Earliest)


# In[106]:


#Most recent year of birth
Most_recent = df['Birth Year'].max()
print(Most_recent)


# In[101]:


#most common year of birth
popular_year = df['Birth Year'].mode()[0] 
print (popular_year) 

#change for github
#change for github 2
#change for github 3
