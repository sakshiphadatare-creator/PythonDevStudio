level = 8
enemies = ["Skeleton", "Zombie", "Alies"]
def my_function():
    new_enemies = ""
    if level < 5:
        new_enemies = enemies[0]
    print(f"New_enemies: {new_enemies}")
my_function()