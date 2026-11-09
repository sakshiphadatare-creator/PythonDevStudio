import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
#choice function used by the randomly print the item from the list.
print(random.choice(friends))

# 2nd Option
print(friends[random.randint(0,4)])

# Simple way
random_int = random.randint(0,4)
rand_print = friends[random_int]
print(rand_print)

