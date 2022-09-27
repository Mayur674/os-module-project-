#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os 


# In[14]:


while True:
    
    choice=int(input("1:create a file\n2:print a file\n3:delete a file\nchoose your option:-"))

    if choice==1:
        folder=input("Create a file name:-")
        os.mkdir(folder)
    
    if choice==2:
        folder=input("Enter a file name that you want to print:-")
        os.listdir(folder)
        
    if choice==3:
        folder=input("enter a file name that you want to delete:-")
        os.rmdir(folder)
    
    break


# In[ ]:





# In[ ]:




