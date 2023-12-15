#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[32]:


prevalence_1 = float(80/1780000)*100000
incidence_1 = float(19/(1780000*120))
mortality_rate_1 = float(2/1780000)*1000

age_1_at_death_1 = (input('At what age did patient 1 die? '))
age_2_at_death_1 = int(input('At what age did patient 2 die? '))
years_of_life_lost_1 = (77-int(age_1_at_death)) + (77-int(age_2_at_death))


# In[33]:


print('The prevalence of HepA in Hillsborough County in 2022 is '+ str(prevalence_1) + ' per 100000 people')
print('The incidence of HepA from Jan 1, 2023 - May 1, 2023 ' + str(incidence_1))
print('The mortality rate during that time frame is '+ str(mortality_rate_1) + ' per 1000 people')
print('The years of potential life lost is ' + str(years_of_life_lost_1))


# # Question 2

# In[34]:


prevalence_2 = float(1211/2660000)*100000
new_cases_2 = int(input('What is the number of new cases? '))
incidence_2 = float(new_cases_2/(2660000))
mortality_rate_2 = float(1/(2660000)*1000)


# In[35]:


print('The prevalence of Salmonella in Miami-Dade in 2022 is '+ str(prevalence_2) + ' per 100000 people')
print('The incidence of Salmonella from Jan 1, 2023 - May 1, 2023 ' + str(incidence_2))
print('The mortality rate during that time frame is '+ str(mortality_rate_2) + ' per 1000 people')


# # Question 3

# In[36]:


prevalence_3 = float(500/100000)*100000
new_cases_3 = int(input('What is the number of new cases? '))
incidence_3 = float(new_cases_3/(100000*90))
mortality_rate_3 = float((40/1780000)*1000)


# In[37]:


print('The prevalence of influenza in 2021 is '+ str(prevalence_3) + ' per 100000 people')
print('The incidence of influenza from Dec 1, 2023 - Feb 1, 2023 ' + str(incidence_3))
print('The mortality rate during that time frame is '+ str(mortality_rate_3) + ' per 1000 people')


# # Question 4

# In[38]:


prevalence_4 = float((12000/1780000)*100000)
new_cases_4 = int(input('How many new cases occured?'))
incidence_4 = float(new_cases_4/(1780000*92))
mortality_rate_4 = float((5/1780000)*1000)
years_of_life_lost_4 = (77-32)+(77-45)+(77-28)+(77-37)+(77-52)


# In[39]:


print('The prevalence of Chlamydia in Hillsborough County in 2022 is '+ str(prevalence_4) + ' per 100000 people')
print('The incidence of Chlamydia from Jan 1, 2023 - May 1, 2023 ' + str(incidence_4))
print('The mortality rate during that time frame is '+ str(mortality_rate_4) + ' per 1000 people')
print('The years of potential life lost is ' + str(years_of_life_lost_4))


# In[ ]:





# In[ ]:




