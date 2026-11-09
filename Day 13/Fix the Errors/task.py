try:
    age = int(input("How old are you?"))

except ValueError:
    print("You have typed in an invalid number, please try again with the numerical response such as 10.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

          # FizzBuzz Game Logic
# def fizz_buzz(target):
#
#     for number in range(1, target+1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
#
# fizz_buzz(int(input("Enter a target: ")))
