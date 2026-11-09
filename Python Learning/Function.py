print("-------------------- Function ---------------------")
''' So basically, function is a block of reusable code that performs of specific task.
    Functions, basically help in organising code, making it more readable, reusable and modular in Python
    In python function is defined using the def keyword followed by the function name and parentheses inside the variable'''

#let's see, how to execute function.
def sayhi():
    print("hello world")
print("Top")
top = sayhi()
print("Hii! Sakshi")

#Here we saw only right function and inside value in many times, instead of writing, whole code again and again.
def greeting(name,age):
    print("hello!"+ name +", you're " + str(age))

greeting("sakshi",12)
greeting("sanka",23)
greeting("Akash", 24)

#Here We will see how to take input from user in function.
def greeting(coustomer_name):
    print("Have a good day,",coustomer_name)
name = input("Enter the name: ")
greeting = greeting(name)

print("-------------------- Return Function ---------------------")

def cube(no):
    return no*no*no
result = cube(5)
print(result)

print("-------------------- Exponent Function ---------------------")

result= 2**3
print(result)

def power(no, po_num):
    res = 1
    for index in range(po_num):
        res = res * no
    return res
print(power(2,3))

import math
print(math.pow(2,3))





















