#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import pandas as pd

current_directory = os.getcwd()
print(current_directory)


# In[14]:


#Change working directory
new_directory_path = '/Users/indup'
os.chdir(new_directory_path)


# In[15]:


updated_dir = os.getcwd()
print(updated_dir)


# In[16]:


file_path = 'Week13Assignment.txt'

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print('An error occurred while reading the file.')


# In[17]:


#Avg age of patients
df = pd.read_csv(file_path)


# In[18]:


print(df)


# In[19]:


print(df.columns)


# In[21]:


#Avg age
average_age = df[' Age'].mean()
print(average_age)


# In[22]:


male = (df[' Gender'] == ' Male').sum()
female = (df[' Gender'] == ' Female').sum()
print(f"The number of male patients is {male} and the number of female patients is {female}. ")


# In[25]:


# Get the highest blood pressure
max_bp = max(df[' BloodPressure'])
print(f"The highest blood pressure is {max_bp}.")


# In[26]:


#Low BP
low_bp = min(df[' BloodPressure'])
print(f"The lowest blood pressure is {low_bp}.")


# In[27]:


#Avg Temp

average_temp = df[' Temperature'].mean()
print(f"The average temperature is {average_temp}.")


# In[ ]:




