#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
import random
from flask import request

def return_pass():

# In[2]:

    test = request.form['test']
    #secure password should contain a mix of uppercase, lowercase, symbols,numbers
    case1 = string.ascii_uppercase
    case2 = string.ascii_lowercase
    case3 = string.punctuation
    case4 = string.digits


    # In[4]:


    get_len = test


    # In[5]:


    #put each case into a list and puts them all together
    l = []
    l.extend(list(case1))
    l.extend(list(case2))
    l.extend(list(case3))
    l.extend(list(case4))


    # In[7]:


    print("Your password is: ",end="")
    #we join a null string with ramdomized string from above and give it a length based on users input
    print("".join(random.sample(l,get_len)))


# In[ ]:




