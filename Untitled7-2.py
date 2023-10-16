#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as st


# In[2]:


def calculate_sample_size(population_size, confidence_level, margin_of_error):
    
    P = 0.5
    
    sample_size = float(((Z**2) * P * (1-P)) / (c**2))
    
    return sample_size


# In[3]:


a = float(input('Enter the population size. '))
b = float(input('Enter the confidence level. '))
c = float(input('Enter the desired margin of error. '))
                        
Z = float(st.norm.ppf(b))

calculate_sample_size(a,b,c)


# In[ ]:


ideal = float(input('Enter the sample size you want to draw. '))

list = []
x = 0

if ideal < sample_size:
    print('Sorry, the requested sample size is not feasible with the given population size, confidence level, and margin of error. The minimum sample size possible is 384. Please enter a lower value.')
else:
    while x < ideal:
        range = int(a/ideal)
        y = 0 + range
        list.append(y)
        x = x+1
    print(list)
        
        
        
        


# In[ ]:





# In[ ]:




