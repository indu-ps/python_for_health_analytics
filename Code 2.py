#!/usr/bin/env python
# coding: utf-8

# # Patient Temperature Check

# In[7]:


temperature = input('Enter the patient temperature in Fahrenheit: ')


# In[8]:


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# In[9]:


if isfloat(temperature): 
    if float(temperature) >= 99.5:
        print('The patient has high temperature.')
    elif float(temperature) <=99.5:
        print('The patient does not have a high temperature.')
else: 
    print('Invalid input. ')
    
    


# In[ ]:





# In[ ]:




