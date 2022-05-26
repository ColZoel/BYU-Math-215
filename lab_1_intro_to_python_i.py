# -*- coding: utf-8 -*-
"""Lab 1 - Intro_to_Python_I.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WrcFE7z3lvXQ1SODp1vAdHDBRxtLpnYl

# **Lab 1 - Introduction to Python programming I**

Enter your code in the spaces provided.  Do not change any of the variable names or function names that are already provided for you.  In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab1"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Collin"

last_name="Zoeller"

# Enter your Math 215 section number in between the quotation marks. 

section_number="Your Math 215 section number goes here"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID=" "

"""**Problem 1**"""

my_first_var=(118+(11*2))/(9-2)   # Replace the value of 0 with the required expression from Problem 1.

"""**Problem 2**"""

def arithmetic2(i):
  return ((i+2)*3)-5 # Put your return value here.  Your shouldn't need to add any more lines of code to this function.

"""**Problem 3**"""

def triple(y):
  return y*3 # Put your return value here.

def avg(x,y):
  return (x+y)/2 # Put your return value here.

def combine(x,y):
  # Put your code here.  Remember that this function should call both of the functions triple(y) and avg(x,y) from above.
  return avg(x,triple(y)) # Put your return value here.

"""**Problem 4**"""

def first(c):
  # Put your code here.
  return c[0] # Put your return value here.

def first_last(c):
  # Put your code here.
  return c[0], c[-1] # Put your return values here.  Remember a function can return two values (you will format your return statement as "return value1, value2").

def middle(c):
  del c[0]
  del c[-1] # Put your code here.
  return c # Put your return value here.

"""**Problem 5**"""

def swap(c):
  new_list=c.copy()
  a = c[0]
  b = c[-1]
  new_list[0] = b
  new_list[-1] = a   # This creates a copy of the list c, which is called new_list.  Your function should work with this list instead of the list c which is passed to the function.
  # Put your code here.
  return new_list # Put your return value here.

"""**Problem 6**"""

def absolute_value(x):
  if x<0:# Put your code here.
    return -1*x
  else:
    return x # Put your return value here.

"""**Problem 7**"""

def indicator(lower,upper,n):
  if lower <= n and n<= upper:
    return 1 # Put your code here.
  else:
    return 0 # Put your return value here.

"""**Problem 8**"""

def trunc_max(x,y):
  if (x>0) or (y>0): # Put your code here. 
    if (x>y):
      return x
    else:
      return y
  else:
    return 0 # Put your return value here.

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""
