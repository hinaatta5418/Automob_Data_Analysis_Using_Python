#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


# In[3]:


df=pd.read_csv('C:\\Users\\hinaa\\Documents\\Data Analyst\\DataAnalysisUsingPythonproject\\Data-Preprocessing_Lab1\\Automobile_data.csv')
print(df)


# In[5]:


# List columns containing '???'
columns_with_question_marks = ['normalized-losses', 'bore', 'stroke','horsepower','peak-rpm','price']
# Replace '???' with NaN in specified columns
df[columns_with_question_marks] = df[columns_with_question_marks].replace('???', np.nan)
# Convert columns to numeric type
df[columns_with_question_marks] = df[columns_with_question_marks].apply(pd.to_numeric, errors='coerce')
print([columns_with_question_marks])


# In[6]:


# Filling missing value with mean of column
mean_normalized_losses = df['normalized-losses'].mean()
df['normalized-losses'].fillna(mean_normalized_losses, inplace=True)
print(df['normalized-losses'])


# In[7]:


df['num-of-doors'] = df['num-of-doors'].replace({'two': 2, 'four': 4})
df['num-of-doors'].replace('???', np.nan, inplace=True)
df['num-of-doors'] = pd.to_numeric(df['num-of-doors'], errors='coerce')
mean_num_of_doors = df['num-of-doors'].mean()
df['num-of-doors'].fillna(mean_num_of_doors, inplace=True)
print(df['num-of-doors'])


# In[10]:


# Filling missing value with mean of column
df['num-of-cylinders'] = df['num-of-cylinders'].replace({'two': 2, 'three': 3, 'four':4, 'five':5, 'six':6, 'eight':8, 'twelve':12})
print(df['num-of-cylinders'])
df['num-of-cylinders'].replace('???', np.nan, inplace=True)
df['num-of-cylinders'] = pd.to_numeric(df['num-of-cylinders'], errors='coerce')
mean_num_of_cylinders = df['num-of-cylinders'].mean()
df['num-of-cylinders'].fillna(mean_num_of_cylinders, inplace=True)
print(df['num-of-cylinders'])


# In[11]:



mean_bore = df['bore'].mean()
df['bore'].fillna(mean_bore, inplace=True)
print(df['bore'])


# In[12]:


mean_stroke = df['stroke'].mean()
df['stroke'].fillna(mean_stroke, inplace=True)
print(df['stroke'])


# In[13]:


mean_horsepower = df['horsepower'].mean()
df['horsepower'].fillna(mean_horsepower, inplace=True)
print(df['horsepower'])


# In[14]:


mean_peak_rpm = df['peak-rpm'].mean()
df['peak-rpm'].fillna(mean_peak_rpm, inplace=True)
print(df['peak-rpm'])


# In[21]:


mean_price = df['price'].mean()
df['price'].fillna(mean_price, inplace=True)
print(df['price'])


# In[23]:


print(df.isnull().sum())


# In[16]:


df['highway-mpg']=235.214/df['highway-mpg']
print(df['highway-mpg'])
df.rename(columns={'highway-mpg':'highway-L/100km'}, inplace=True)
print(df)


# In[25]:


#Normalize the columns 'length', 'width', and 'height'
columns_to_normalize = ['length', 'width', 'height']
# Min-Max Scaling
df[columns_to_normalize] = (df[columns_to_normalize] - df[columns_to_normalize].min()) / (df[columns_to_normalize].max() - df[columns_to_normalize].min())


# In[26]:


print(df['length'])


# In[27]:


print(df['width'])


# In[28]:


print(df["height"])


# In[29]:


print(df)


# In[ ]:




