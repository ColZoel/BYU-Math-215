# -*- coding: utf-8 -*-
"""Lab 5 -  LU_decompositions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hUqd25J-jVkm4ZAixbkVFu9U0lKqjTmN

#**Lab 5 - LU decompositions and Gaussian elimination**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab5"

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

BYUNetID="czoeller"

"""**Import NumPy**"""

import numpy as np

"""**Problem 1**"""

def augment(A,b): 
  Ab = np.column_stack((A,b))
  return Ab

"""**Problem 2**"""

def first_column_zeros(A):
  B=np.copy(A)
  for i in range(1, len(A)):
    B[i]=B[i] - (B[i,0]/B[0,0])*B[0]
  return B

"""**Problem 3**"""

def row_echelon(A,b):
  Ab = np.column_stack((A,b))
  B=np.copy(Ab)
  for j in range(len(B)):
    for i in range(j+1, len(B)):
      B[i]=B[i] - (B[i,j]/B[j,j])*B[j,:]
  return B

"""**Problem 4**"""

def LU_decomposition(A):
  U=np.copy(A)
  L=np.identity(len(A))
  v = np.array(np.shape(A))
  m = v[0]
  n = v[1]
  for j in range(0, n):
    for i in range(j+1, m):
      L[i,j] = U[i,j]/U[j,j]
      U[i,:] = U[i,:]-L[i,j]*U[j,:]
  # Put your code here.
  return L,U

"""**Problem 5**"""

def forward_substitution(L,b):
  n = len(b)
  y = np.zeros(n)
  for i in range(0,n):
    y[i] = (b[i] - np.dot(y,L[i,:]))/L[i,i]
  return y

"""**Problem 6**"""

def back_substitution(U,y):
  n = len(y)
  x = np.zeros(n)
  for i in range(n-1,-1,-1):
    x[i] = (y[i] - np.dot(x,U[i,:]))/U[i,i]
  return x

"""**Problem 7**"""

def LU_solver(A,b):
  U=np.copy(A)
  L=np.identity(len(A))
  v = np.array(np.shape(A))
  m = v[0]
  n = v[1]
  for j in range(0, n):
    for i in range(j+1, m):
      L[i,j] = U[i,j]/U[j,j]
      U[i,:] = U[i,:]-L[i,j]*U[j,:]
  n = len(b)
  y = np.zeros(n)
  for i in range(0,n):
    y[i] = (b[i] - np.dot(y,L[i,:]))/L[i,i]            
  a = len(y)
  x = np.zeros(a)
  for i in range(a-1,-1,-1):
    x[i] = (y[i] - np.dot(x,U[i,:]))/U[i,i]
  return x

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""