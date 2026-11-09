import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}
#print(operations["*"](4,8))
#print(operations["-"](8,4))

def calculator():

    print(art.logo)

    continue_ = True
    num1 = float(input("Enter the first number: "))
    while continue_:
        for symbols in operations:
            print(symbols)

        operators = input("pick the operators: ")

        num2 = float(input("Enter the second number: "))

        result = operations[operators](num1,num2)
        print(f"{num1} {operators} {num2} = {result}")

        choice = input("Do you want to continue? (y/n): ").lower()
        if choice == "y":
            num1 = result
            continue_ = True
        else:
            continue_ = False
            print("\n" * 20)
            calculator()

calculator()


