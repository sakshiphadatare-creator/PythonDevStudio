print(" -------------------         String          ----------------------")

num = 10
name = "sakshi Pranav"
#print(name + 'the number is '+num)   # Gives Error
print(name + 'the number is '+ str(num))

#command "\n"
print("Sakshi\nPhadatare")

#print("Sakshi "Phadatare"")   # Gives Error
print("Sakshi \"Phadatare\"")

print(name.lower())
print(name.isupper())
print(name.upper())
print(len(name))
print(name[0])           #starts
print(name[-1])               #To take the end alphabet
print(name.index('s'))            #what is the index of the s alpha.
print(name.replace("sakshi","Sakshi"))        # replace

print(" -------------------         Number          ----------------------")

print(7+3)
print(7-3)
print(7*3)
print(10.50 / 2)
print(((30+10)-2)*2)
print(15 % 2)           # remainder 1, 2X7=14
print(15 // 2)          # quotient 7
print(abs(-9))          # abs is the function which return the positive value if it's negative
print(pow(3,4))
print(max(2, 3, 4))
print(min(2, 3, 4))
print(round(2.46))
print(round(2.66))

from math import *
print(floor(3.14))    # Return Base of the number
print(ceil(3.14))     # ceil is going to next number
print(sqrt(4))
print(round(sqrt(4)))

print(" -------------------         Input From User          ----------------------")

name = input("Enter the name: ")
age = input("Enter the age:")
print("Welcome " + name +"!")
print("your age is "+str(age))