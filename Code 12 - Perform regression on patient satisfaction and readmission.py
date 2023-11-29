#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np
import os

import matplotlib as plt
from sklearn.linear_model import LogisticRegression
from matplotlib.pyplot import boxplot


#Change working directory
new_directory_path = '/Users/indup'
os.chdir(new_directory_path)

# Read data from the file
file_path = "Week14Assignment.txt"
data = pd.read_csv(file_path)


# In[28]:


print("Patient Data:")
print(data)
print(data.columns)


# In[29]:


readmitted_count = data[' Readmission'].sum()
print("\nNumber of patients readmitted:", readmitted_count)


# In[34]:


avg_stat_sat = data[' StaffSatisfaction'].mean()
print("\nAverage staff satisfaction:", avg_stat_sat)

avg_clean_sat = data[' CleanlinessSatisfaction'].mean()
print("\nAverage cleanliness satisfaction:", avg_clean_sat)

avg_food_sat = data[' FoodSatisfaction'].mean()
print("\nAverage food satisfaction:", avg_food_sat)

avg_comfort_sat = data[' ComfortSatisfaction'].mean()
print("\nAverage comfort satisfaction:", avg_comfort_sat)

avg_communications_sat = data[' CommunicationSatisfaction'].mean()
print("\nAverage communication satisfaction:", avg_communications_sat)

data[' Overall_satisfaction'] = data[[' StaffSatisfaction',' CleanlinessSatisfaction',
                            ' FoodSatisfaction',' ComfortSatisfaction',' CommunicationSatisfaction']].mean(axis=1)


# In[35]:


boxplot(data[' Overall_satisfaction'], showfliers = True)


# In[38]:


# Logistic regression

X = data[' Overall_satisfaction'].values.reshape(-1,1)
Y = data[' Readmission']

log_reg = LogisticRegression().fit(X,Y)


# In[41]:


#correlation results

correlation_coefficient = log_reg.coef_[0][0]

if correlation_coefficient > 0:
    print("Logistic regression results indicated a: ")
    if correlation_coefficient > 0.5:
        print("Moderate Correlation")
    elif correlation_coefficient > 0.7:
        print("Strong Correlation")
    else:
        print("Weak correlation")

print(f"The correlation coefficient was {correlation_coefficient}.")


# In[44]:


#plot the data
plt.pyplot.scatter(X,Y)
plt.pyplot.xlabel('Overall Satisfaction Scores')
plt.pyplot.ylabel('Readmission')
plt.pyplot.title('Logistic Regression - Overall Satisfaction vs Readmission')
plt.pyplot.plot(X, log_reg.predict(X), color = 'blue')
plt.pyplot.xlim(2,5)


# In[ ]:




