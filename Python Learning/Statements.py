print("-------------------- if-elif-else Statements ---------------------")


is_female = False
is_good = False

if is_female and is_good:
    print("female is good")
elif is_female or not is_good:
    print("female is bad")
elif is_female or is_good:
    print("Simple")
elif not is_female or is_good:
    print("not female")
else:
    print("not a human being")


print("-------------------- if-elif-else Statements with function ---------------------")

def max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3
result = max_number(1, 3, 5)
print("Maximum number is : ",result)


def limit_of_vote(name,age):
    if age > 18:
        return f"you are eligible for voting {name}😎."
    else:
        return f"you are not eligible for voting {name}🙁."

voting = limit_of_vote("sakshi",19)
print(voting)

print("-------------------- Grade Calculation ---------------------")

def calculate_grade(marks):
    if marks >= 95:
        return "O+"
    elif 75 <= marks < 95:
        return "A"
    elif 55 <= marks < 75:
        return "B"
    elif 35 <= marks < 55:
        return "C"
    else:
        return "Fail"

result = calculate_grade(37)
print("Grade : "+result)

