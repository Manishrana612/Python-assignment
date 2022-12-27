#!/usr/bin/env python
# coding: utf-8

# Q1 Write a Python program to print "Hello Python"?

# In[3]:


print('Hello Python')


# Q2 Write a Python program to do arithmetical operations addition and division.?

# In[13]:


no1=int(input('Enter first no :'))
no2=int(input('Enter second no :'))
print(no1+no2)
print(no1/no2)


# Q3 Write a Python program to find the area of a triangle?

# In[16]:


base = int(input('Enter the base : '))
height = int(input('Enter the height:'))
p=base*height
print('this is area of triangle')
print(p/2)


# Q4 Write a Python program to swap two variables?

# In[17]:


p=int(input('enter the p value: '))
q=int(input('enter the q value: '))
temp1=p
p=q
q=temp1
print('the value of p',p)
print('the value of q',q)


# Q5 Write a Python program to generate a random number?

# In[22]:


import random
no1=random.randrange(30)
print('random integer',no1)

