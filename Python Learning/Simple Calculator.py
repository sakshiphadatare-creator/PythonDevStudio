def calculator(num1, num2,choose):
    if choose == "add":
        result = num1 + num2
        return result
    elif choose == "sub":
        result = num1 - num2
        return result
    elif choose == "mul":
        result = num1 * num2
        return  result
    elif choose == "div":
        result = num1 / num2
        return  result
    else:
        return "Invalid option"

chose = input("Choose the option \n 1) Add\n 2) Sub\n 3) Mul\n 4) Div\nEnter here: ").lower()
no1 = int(input("Enter the first number: "))
no2 = int(input("Enter the second number: "))
total = calculator(no1, no2,chose)
print("Result : ",total)

# Without Function
num1 = int(input("Enter the first number:"))
oper = input("Enter the operator: ")
num2 = int(input("Enter the second number: "))

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
else:
    print("Invalid option")
