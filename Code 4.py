#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def celcius_to_fahrenheit(celsius):
    return ((celsius * 9/5 + 32))

def fahrenheit_to_celcius(fahrenheit):
    return ((fahrenheit-32) * 5/9)

conversion_features = {
    'c': celcius_to_fahrenheit,
    'f': fahrenheit_to_celcius
}

print('Choose the conversion direction. Type c for celcius to fahrenheit or f for fahrenheit to celcius. ')

choice = input('Enter your choice: ').strip().lower()
            
if choice in conversion_features:
            temperature = float(input('Enter the temperature: '))
            converted_temperature = conversion_features[choice](temperature)
            print(f"{temperature} degrees {'Celcius' if choice == 'c' else 'Fahrenheit'} is {converted_temperature} degrees {'Fahrenheit' if choice == 'c' else 'Celcius'}")

else:
    print('This was not a valid input. Please enter a C or a F. ')



# In[ ]:





# In[ ]:





# In[ ]:




