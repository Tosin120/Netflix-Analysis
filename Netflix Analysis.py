#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#importing the dataset


# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv(r'C:\Users\USER\Videos\New folder (8)\New folder\New folder\python files\8. Netflix Dataset.csv')


# In[4]:


data


# In[5]:


#Getting some basic data information


# In[6]:


# 5 top record of the dataset
data.head()


# In[7]:


# Bottom 5 record of the dataset
data.tail()


# In[8]:


# no of rows and column
data.shape


# In[9]:


# Total no of value(element) in a dataset
data.size


# In[10]:


# Each column name
data.columns


# In[11]:


# The datatype of each column
data.dtypes


# In[12]:


# Indexes, column, datatypes of each column, memory at once
data.info()


# In[13]:


# Task 1 : Is there any duplicate record in this dataset? if yes, then remove the duplicate records


# In[14]:


# Top 5 rows of the dataset
data.head()


# In[15]:


# row & column of the dataset 
data.shape


# In[16]:


# duplicate value(s) in the datset
data[data.duplicated()]


# In[17]:


# Removing the duplicates()
# using inplace to make the changes permanent
data.drop_duplicates(inplace = True)


# In[18]:


# verifying the duplicates has been removed
data[data.duplicated()]


# In[19]:


# verifying the duplicates has been removed
data.shape


# In[20]:


# Task2: Is their any null values present in any columns? show with heat map


# In[21]:


data.head()


# In[22]:


# To show where the null values is present
data.isnull()


# In[23]:


# To show the null values in each columns
data.isnull().sum()


# In[24]:


#seaborn library
#importing seaborn
import seaborn as sns


# In[25]:


# Using heatmap to show the nullvalues in count
sns.heatmap(data.isnull())


# In[26]:


# Q1. For 'House Cards', What is the Show id and who is the Director of this Show?


# There are two methods of solving this problem: isin() & str.contains()


# In[27]:


# isin()


# In[28]:


data.head()


# In[29]:


# Record of particular item in any column using isin()
data[data['Title'].isin(['House of Cards'])]


# In[30]:


#str.contains()


# In[31]:


data.head(2)


# In[32]:


# Record of particular item in any column using str.contains()
data[data['Title'].str.contains('House of Cards')]


# In[33]:


# Q2. In which year highest number of the TV shows & Movies were released ? Show the Bar Graph.


# In[34]:


data.dtypes


# In[35]:


# Creating new column ('Date_N') in the dataset
# Converting 'Release_Date' in a datetime format & putting it in a new column
data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[36]:


data.head()


# In[37]:


data.dtypes


# In[38]:


# Number of tv shows released per year
# The occurence of all individual years in Date column
data['Date_N'].dt.year.value_counts()


# In[39]:


# Plotting using barchart, the occurence of all individual years in Date column
data['Date_N'].dt.year.value_counts().plot(kind = 'bar')


# In[40]:


# Q3.  How many Movies & TV shows are in the dataset? Show with Bar Graph.


# In[41]:


#groupby()


# In[42]:


data.head(2)


# In[43]:


# All the unique values in the dataset and show their count
data.groupby('Category').Category.count()


# In[44]:


# Showing the count of all unique values of any column in form of bar graph
sns.countplot(data['Category'])


# In[45]:


# Q4 Show all the movies that were release in year 2000


# In[46]:


data.head(2)


# In[47]:


# Creating a new column 'Yaer', it will only consider year
data['Year'] = data['Date_N'].dt.year


# In[48]:


data.head(2)


# In[49]:


# Filtering
data[(data['Category'] == 'Movie') & (data['Year'] == 2000)]


# In[50]:


# Q5. Show only the Titles of all TV Shows that were released in India only


# In[51]:


data.head(2)


# In[52]:


# filtering


# In[53]:


# The Titles of all TV Shows that were released in India only
data[(data['Category'] == 'TV Show') & (data['Country'] =='India')]['Title']


# In[ ]:


# Q6. Show Top 10 Directors, who gave the highest number of TV shows & Movies to Netflix?


# In[54]:


data.head(2)


# In[56]:


data['Director'].value_counts().head(10)


# In[ ]:


# Q7. Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".


# In[58]:


data.head(2)


# In[57]:


# filtering (And, Or Operators)


# In[59]:


# All the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".
data[(data['Category'] == 'Movie') & (data['Type'] == 'Comedies') | (data['Country'] == 'United Kingdom')]


# In[60]:


# Q8. In how many movies/shows, Tom Cruise was cast?


# In[61]:


data.head(2)


# In[62]:


# Filtering
data[data['Cast'] == 'Tom Cruise']


# In[66]:


# str.contains()
data[data['Cast'].str.contains('Tom Cruise')]
# Result showing error because str.contain can't operate on null values
# i'll have to remove all values from the dataset


# In[68]:


# Creating new dataframe and dropping all rows which has any missing value rows 
data_new = data.dropna()


# In[69]:


data_new.head(2)


# In[ ]:


# Now, we can apply (str.contains) function in the missing value


# In[71]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# In[72]:


# Q9. What are the different ratings defined by netflix?


# In[75]:


# Total count of rating 
# nunique()
data['Rating'].nunique()


# In[76]:


# different rating in each column
# unique()
data['Rating'].unique()


# In[77]:


# Q10. How many movies got the 'TV-14' rating, in canada? 


# In[78]:


data.head(2)


# In[79]:


# Movies that got 'TV-14' rating in Canada
data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada')]


# In[80]:


# Number of movies that got 'TV-14' rating in Canada 
data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada')].shape

# the number of movies is 11


# In[81]:


# Q11. How many TV shows got the 'R' rating after year 2018?


# In[82]:


data.head(2)


# In[85]:


# TV shows got the 'R' rating after year 2018
data[(data['Category'] == 'TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018)]


# In[86]:


# Q12. What is the maximum duration of a movie/show on netflix?


# In[87]:


data.head(2)


# In[88]:


data['Duration'].unique()


# In[89]:


data['Duration'].dtypes


# In[92]:


# i'll have to split the string from the integer
# i'll use the str.split() function
data[['Minutes', 'Unit']] =  data['Duration'].str.split(' ', expand=True)


# In[93]:


data.head(2)


# In[94]:


data['Minutes'].max()


# In[95]:


# Q13  Which individual country has the highest number of TV Shows?


# In[96]:


data.head(2)


# In[97]:


# i'll create a new dataframe for tvshows
data_tvshow = data[data['Category'] == 'TV Show']


# In[98]:


data_tvshow.head(2)


# In[99]:


#  number of TV Shows in each countries
data_tvshow.Country.value_counts()


# In[100]:


#  country that has the highest number of TVShows
data_tvshow.Country.value_counts().head(1)


# In[101]:


# Q14 How can we solve the dataset by years


# In[103]:


data.head(2)


# In[104]:


data.sort_values(by='Year').head(2)


# In[105]:


data.sort_values(by='Year').head(2).ascending = False


# In[106]:


data.head(2)


# In[107]:


# Q15. Find all the instances where:
#        category is 'Movie' and type is 'Drama'
#        Category is 'TV Show' and type is "Kids' TV"


# In[108]:


data.head(2)


# In[110]:


# Instance where category is 'Movie' and type is 'Drama'
data[(data['Category'] == 'Movie') & (data['Type'] == 'Dramas')]


# In[111]:


# Category is 'TV Show' and type is "Kids' TV"
data[(data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV")]


# In[112]:


# All the instances where:
#        category is 'Movie' and type is 'Drama'
#        Category is 'TV Show' and type is "Kids' TV"
data[(data['Category'] == 'Movie') & (data['Type'] == 'Dramas') | (data['Category'] == 'TV Show') & (data['Type'] == "Kids' TV")]


# In[ ]:




