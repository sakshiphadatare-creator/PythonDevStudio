# len() function is usually use for string, list, set, frozen set, tuple, dictionary data types.
print(len("hello"))

# How to identify data types
print(type("abc"))
print(type(123))
print(type(123.45))
print(type(True))   # True the first char is always capital.

# Type Conversion
print("123" + "456")
print(int("123") + int("456"))

print(str(123))
print(int("125"))
print(float(125))
print(bool("True"))

print("Number of letters in your name: " + str(len(input("Enter your name : "))))

name = input("Enter your name : ")
length = len(name)
print("Number of letters in your name: " + str(length) )