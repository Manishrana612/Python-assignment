#!/usr/bin/env python
# coding: utf-8

#  Q1 Write a Python Program to Find the Factorial of a Number?

# In[5]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)

num=int(input("enter the no : "))
print("the factorial of ",num,"is",factorial(num))


# Q2 Write a Python Program to Print the Fibonacci sequence?

# In[21]:


def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
num=int(input("enter the no : "))
if num <=0:
    print("please enter postive no ")
else:
    print("fibonacci series:")
    for i in range(num):
        print(fibonacci(i))


# Q3 Write a Python Program to Check Armstrong Number?

# In[1]:


def is_armstrong(num):
    num_digits = len(str(num))
    sum = 0
    for digit in str(num):
        sum += int(digit)**num_digits
    return sum == num


# In[2]:


print(is_armstrong(153))


# Q4 Write a Python Program to Display the multiplication Table?

# In[4]:


def display_multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")


# In[6]:


display_multiplication_table(5)


# Q5 Write a Python Program to Find the Sum of Natural Numbers?

# In[8]:


def sum_natural_numbers(n):
    total = 0
    for i in range(1, n+1):   
        total += i
    return total


# In[9]:


sum_natural_numbers(5)

