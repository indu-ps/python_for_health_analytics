#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import numpy as np
import os

import matplotlib as plt
from sklearn.linear_model import LogisticRegression
from matplotlib.pyplot import boxplot


# In[84]:


#Change working directory
new_directory_path = '/Users/indup'
os.chdir(new_directory_path)

# Read data from the file
file_path = "Hospital1.txt"
hospy1 = pd.read_csv(file_path)

# Read data from the file
file_path = "Hospital2.txt"
hospy2 = pd.read_csv(file_path)


# In[85]:


#Determine Column Names
print(hospy1.columns)
print(hospy2.columns)


# In[86]:


#Function to Count Readmission
def count_readmission(hospital_name, hospital_num):
    readmitted_count = hospital_name[' Readmission'].sum()
    print(f"\nNumber of patients readmitted in hospital {hospital_num}:", readmitted_count)


# In[87]:


def find_averages(hospital_name, hospital_num):
    
    avg_stat_sat = hospital_name[' StaffSatisfaction'].mean()
    print(f"\n Hospital {hospital_num}- Average staff satisfaction:", avg_stat_sat)

    avg_clean_sat = hospital_name[' CleanlinessSatisfaction'].mean()
    print(f"\n Hospital {hospital_num}- Average cleanliness satisfaction:", avg_clean_sat)

    avg_food_sat = hospital_name[' FoodSatisfaction'].mean()
    print(f"\n Hospital {hospital_num}- Average food satisfaction:", avg_food_sat)

    avg_comfort_sat = hospital_name[' ComfortSatisfaction'].mean()
    print(f"\n Hospital {hospital_num}- Average comfort satisfaction:", avg_comfort_sat)

    avg_communications_sat = hospital_name[' CommunicationSatisfaction'].mean()
    print(f"\n Hospital {hospital_num}- Average communication satisfaction:", avg_communications_sat)


    hospital_name[' Overall_satisfaction'] = hospital_name[[' StaffSatisfaction',' CleanlinessSatisfaction',
                            ' FoodSatisfaction',' ComfortSatisfaction',' CommunicationSatisfaction']].mean(axis=1)


# In[88]:


def logistic_regression_results(correlation_coefficient, hospital_num):

    if correlation_coefficient > 0:
        print("Logistic regression results indicated a: ")
        if correlation_coefficient > 0.5:
            print("Moderate Correlation")
        elif correlation_coefficient > 0.7:
            print("Strong Correlation")
        else:
            print("Weak correlation")

    print(f"The correlation coefficient was {correlation_coefficient}.")

    #plot the data
    plt.pyplot.scatter(X,Y)
    plt.pyplot.xlabel('Overall Satisfaction Scores')
    plt.pyplot.ylabel('Readmission')
    plt.pyplot.title(f"Hospital {hospital_num}: Logistic Regression - Overall Satisfaction vs Readmission")
    plt.pyplot.plot(X, log_reg.predict(X), color = 'blue')
    plt.pyplot.xlim(2,5)


# In[89]:


#Counting the number of readmits
count_readmission(hospy1,1)
count_readmission(hospy2,2)


# In[90]:


#Find Averages Hospital 1
find_averages(hospy1,1)


# In[91]:


#Find Averages Hospital 2
find_averages(hospy2,2)


# In[95]:


# Logistic regression Transformation Hospital 1

X = hospy1[' Overall_satisfaction'].values.reshape(-1,1)
Y = hospy1[' Readmission']

log_reg1 = LogisticRegression().fit(X,Y)

#Logistic Regression Hospital 1
logistic_regression_results(log_reg1.coef_[0][0],1)


# In[96]:


# Logistic regression Transformation Hospital 2

X = hospy2[' Overall_satisfaction'].values.reshape(-1,1)
Y = hospy2[' Readmission']

#Logistic Regression Hospital 2

log_reg2 = LogisticRegression().fit(X,Y)
logistic_regression_results(log_reg2.coef_[0][0],2)

