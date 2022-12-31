#!/usr/bin/env python
# coding: utf-8

# Q1 Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[1]:


def check_no(num):
    if num > 0:
        print("no is positive")
    elif num < 0:
        print("no is negative")
    else:
        print(" no is zero")
        


# In[4]:


check_no(5)
check_no(-5)
check_no(0)


# Q2 Write a Python Program to Check if a Number is Odd or Even?

# In[5]:


def check_odd_even(num):
    if num % 2 ==0:
        print(" no is even ")
    else :
        print("no is odd")
    


# In[9]:


check_odd_even(20)
check_odd_even(19)
check_odd_even(-2)


#  Q3 Write a Python Program to Check Leap Year?

# In[11]:


def check_leap_year(year):
    if year % 4 ==0:
        print("this is leap year")
    else:
        print("this is not leap year")


# In[14]:


check_leap_year(2000)
check_leap_year(2004)
check_leap_year(2005)


# Q4 Write a Python Program to Check Prime Number?

# In[19]:


def check_prime_no(num):
    if num<2:
        print("no is not prime no")
        return
    for i in range(2,num):
        if num%i==0:
            print("no is not prime no ")
            return
        
    print("no is prime no ")
        


# In[21]:


check_prime_no(2)
check_prime_no(4)


# Q5 Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[24]:


def check_prime(num):
    if num<2:
        return False
    
    for i in range(2,num):
        if num%i==0:
            return False
    
    return True

for i in range(1,100001):
    if check_prime(i):
        print(i)


# In[ ]:





# In[ ]:




