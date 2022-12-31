#!/usr/bin/env python
# coding: utf-8

# Q 1 Write a Python program to convert kilometers to miles?

# In[1]:


def km_to_miles(km):
 return km*0.621371
print(km_to_miles(5))


# Q2 Write a Python program to convert Celsius to Fahrenheit?

# In[2]:


def celsius_to_fahrenheit(celsius):
  return celsius * 1.8 + 32
print(celsius_to_fahrenheit(100))


# Q3 Write a Python program to display calendar?

# In[3]:


import calendar
yy=int(input("Enter Year: " ))
mm=int(input("Enter Month: " ))
print(calendar.month(yy,mm))


# Q4 Write a Python program to solve quadratic equation?

# In[4]:


import cmath
def solve_quadratic_equation(a,b,c):
    d=b**2-4*a*c
    X1 = (-b+cmath.sqrt(d))/2*a
    X2 = (-b-cmath.sqrt(d))/2*a
    return X1,X2
    


# In[8]:


a=1
b=5
c=6
solution = solve_quadratic_equation(a,b,c)
print(f"The solutions to the quadratic equation {a}x^2 + {b}x + {c} = 0 are x = {solution[0]} and x = {solution[1]}")


# Q5 Write a Python program to swap two variables without temp variable?

# In[9]:


x = 10
y = 20

x, y = y, x

print(f"x = {x}, y = {y}")


# In[ ]:





# In[ ]:




