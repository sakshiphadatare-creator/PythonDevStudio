"""
Python Sequences
* list
* range
* string
* tuple    """

# List comprehension
num = [1,23,4,5]

new = []
for i in num:
    add = i+1
    new.append(add)
print(new)

#List comprehension
# new_list = [new_item/expression for item in list]
new_list = [n+1 for n in num]
print(new_list)

name = "sakshi"
new_list = [letter for letter in name]
print(new_list)

list_1 = [i*2 for i in range(1,5)]    # [2,4,6,8]
print(list_1)

# Conditional list comprehension
# new_list = [new_item/expression for item in list if test]
names = ['sakshi', 'pranav', 'siddharth', 'prashant']
long_name = [name.upper() for name in names if len(name) > 5]
print(long_name)


"""
Dictionary comprehension
new_dict = {new_key: new_value for item in list}
new_dict = {new_key: new_value for (key, value) in dict_item()}
new_dict = {new_key: new_value for (key, value) in dict.item() if test}   """

# student_score = {
#     "sakshi" : 24,
#     "pranav" : 22,
#     "siddharth" : 19,
#     "prashant" : 17
# }
student = ["sak", "pra", "san", "aks"]
import random
new_student_score = {score:random.randint(20,60) for score in student}
print(new_student_score)
pass_student = {student : score for (student,score) in new_student_score.items() if score > 30}
print(pass_student)

fail_student = {student : marks for (student,marks) in new_student_score.items() if marks <= 25}
print(fail_student)

'''You are going to use Dictionary Comprehension to create a dictionary called result
that takes each word in the given sentence and calculates the number of letters in each word. '''
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {words : len(words) for words in sentence.split()}
print(result)

'''You are going to use Dictionary Comprehension to create a dictionary called weather_f 
that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. 
To convert temp_c into temp_f use this formula: 
(temp_c * 9/5) + 32 = temp_f'''
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day : (temp * 9/5) + 32  for day,temp in weather_c.items() }
print(weather_f)

student_dict = {
    "student":["Sakshi","lily","james"],
    "score":[56,78,34]
}
#Looping through dictionaries:
for(key,value) in student_dict.items():
    print(key,value)

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
for key,value in student_data_frame.items():
    print(value)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)   # return whole student
    print(row.score)     # return whole score
    if row.student == "Sakshi":
        print(row.score)   # Return score




















