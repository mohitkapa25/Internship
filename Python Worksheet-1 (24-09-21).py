#!/usr/bin/env python
# coding: utf-8

# In[1]:


#11) How to find factorial of a number
a=int(input("The number is,"))
def factorial(a):
    if a==1 or a==0:
        return 1
    else:
        return a*factorial(a-1)

print(factorial(a))


# In[48]:


#12) Code to find if the number is prime or composite

def number(x):
    if x>1:
        for i in range(2,x+1):
            if x%i==0:
                print("the number is composite")
                break
            else:
                print("The number is prime")
                break   
    if x==1 or x==0:
        for i in range(1,2):
            if x%i==0:
                print("The number is neither prime nor composite")
x=int(input("The number is,"))
print(number(x))


# In[49]:


#13) code to check if the string is a palindrome or not

string=input("The string is,")

if string==string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


# In[5]:


# 14) write a program to find the third side of the right angled triangle with two sides give
a=float(input("Length of the triangle is",))
b=float(input("Height of the triangle is",))
import math

from math import sqrt
def hypo():
    return sqrt(a**2+b**2)
     
print(hypo())


# In[6]:


#15) code to write frequency of each character present in given string

S= "Welcome to Python"

print(len(S))

print(S.count("W"))
print(S.count("e"))
print(S.count("l"))
print(S.count("c"))
print(S.count("o"))
print(S.count("m"))
print(S.count("e"))
print(S.count("t"))
print(S.count("p"))
print(S.count("y"))
print(S.count("h"))
print(S.count("n"))


# In[ ]:





# In[ ]:




