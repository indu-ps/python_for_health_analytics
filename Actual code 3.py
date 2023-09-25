#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name = input('Enter your name: ')


# In[4]:


def reverse_slicing(s):
    return s[::-1]

input_str = input('Enter a word.')

if __name__ == "__main__":
    print('Reverse String using slicing =', reverse_slicing(input_str))


# In[ ]:


sentence = input('Enter a sentence. ')
print(len(sentence))


# In[3]:


vowels = input('Enter a word or sentence. ')
number = 0
for a in vowels:
    if a == 'a':
        number += 1
    if a == 'e':
        number += 1
    if a == 'i':
        number += 1
    if a == 'o':
        number += 1
    if a == 'u':
        number += 1

print(number)
        


# In[5]:


word = input('Enter a potential palindrome. ')
if reverse_slicing(word) == word:
    print('This is a palindrome. ')
else:
    print('This is not a palindrome. ')


# In[ ]:


secret = input('Enter a secret message. ')
new = upper(secret)
better = new.replace(' ', '_')

