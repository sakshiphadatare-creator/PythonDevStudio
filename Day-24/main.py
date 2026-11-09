""". refers to the current directory
.. refers to one level up
../.. goes two levels up, and so on
import os
print(os.getcwd())  # Tells you the current working directory"""

file = open("/Users/sakshi/Desktop/my_file.txt","r")
print(file.read())
file.close()

with open("new_file.txt", "a+") as file:
    file.write("\nHello World\n")
    file.write("I am student of Indira college")

with open("new_file.txt","r") as file:
    print(file.read())