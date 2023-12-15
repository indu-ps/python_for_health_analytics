#!/usr/bin/env python
# coding: utf-8

# In[23]:


data_list = [('apple', 5), ('banana', 2), ('orange', 8), ('grapes', 3), ('pineapple',1)]


# In[25]:


def convert_to_dictionary(data_list):
    result_dict = {}
    for key, value in data_list:
        result_dict[key] = value
    return result_dict



# Call the function with the sample list
result_dict = convert_to_dictionary(data_list)

# Print the resulting dictionary
print(data_list)
print(result_dict)

