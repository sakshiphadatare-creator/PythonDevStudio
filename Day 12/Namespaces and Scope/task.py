enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

my_local_var2 = "Sakshi"  # Glocal variable/scope
def my_function():
    my_local_var = 2  # Local variable/scope
    print(f"my_local_var inside function: {my_local_var}")
my_function()
print(my_local_var2)


my_glocal_var3 = "Sakshi"  # Glocal variable/scope
""" Global variable is accessible anywhere in the code file. """
def my_function():
    print(f"my_glocal_var inside function: {my_glocal_var3}")
my_function()