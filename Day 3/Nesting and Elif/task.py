# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("Enter the age: "))
#     if age <= 12 :
#         print("please pay the $5.")
#     elif age >= 12 and age <= 18 :
#         print("please pay the $7.")
#     else:
#         print("please pay the $12.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi >= 25 :
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else :
    print("under weight")
