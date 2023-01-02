#!/usr/bin/env python
# coding: utf-8

# Q1 Write a Python Program to Find LCM?

# In[1]:


def find_lcm(x, y):
    maximum = max(x, y)
    lcm = maximum
    while True:
        if lcm % x == 0 and lcm % y == 0:
            return lcm
        lcm += maximum


# In[2]:


find_lcm(3,4)


# Q2 Write a Python Program to Find HCF?

# In[4]:


def find_hcf(x, y):
    minimum = min(x, y)
    hcf = 1   
    for i in range(minimum, 0, -1):
           if x % i == 0 and y % i == 0:
            hcf = i
            return hcf


print(find_hcf(3, 4))


# Q3 Write a Python Program To Find ASCII value of a character?

# In[5]:


def find_ascii_value(char):
    return ord(char)
print(find_ascii_value('a')) 
print(find_ascii_value('A')) 


# Q4 Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[9]:


def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"


# In[10]:


print(calculator(2, 3, '+'))

