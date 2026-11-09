# Modifying Global Scope

num = 18

def modify_num():
    global num
    num+=2
    return num
print(modify_num())

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


