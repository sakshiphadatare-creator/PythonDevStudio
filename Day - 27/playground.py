#Unlimited positional Argument
# *args instead of this we can write *numbers, *names....so on.
def add(*numbers):
    print(numbers[0])   #It's a tuple so we can also access indexing through
    result = 0
    for n in numbers:
        result += n
    return result
print(add(1,2,3,4,5,6,7))  #We can add more values to it. basically it can take any number of values


def add(*args):
    print(args)   # return tuple type (3,6,4)
    sum = 0
    for n in args:
       sum += n
    return sum

print(add(3, 6, 4))

#keyword Argument
def calculate(n,**kwargs):
    print(kwargs)
    # for key,word in kwargs.items():
    #     print(key)
    #     print(word)
    #     print(f"{key}: {word}")
    #     print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2,add=3, multiply=5)

# Example of keyword Argument how it's create a kw class
class Car:
    def __init__(self,**kwa):
        self.name = kwa.get("name")
        self.model = kwa.get("model")
        self.price = kwa.get("price")
        self.color = kwa.get("color")

my_car = Car(name="Jeep", model="Jukebox")  # If you want to take only two keys fine.
print(my_car.name)
print(my_car.model)
