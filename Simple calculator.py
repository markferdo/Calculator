#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Operations \n add - a \n substract - s \n multiply - m \n devide - d ")
num1 = float(input("Enter no 1: "))
num2 = float(input("Enter no 2: "))
operation = str(input("Enter operation: "))

def calculator(num1,num2,operation):
    if operation == "a":
        print(f"Total: {num1 + num2}")
    elif operation == "s":
        print(f"Total: {num1 - num2}")
    elif operation == "m":
        print(f"Total: {num1 * num2}")
    elif operation == "d":
        print(f"Total: {num1 / num2}")
    else:
        print("Enter correct operation")
        
calculator(num1,num2,operation)
 

