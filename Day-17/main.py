# How to create the class
class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0      #defualt value so need write as a parameter
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("101", "Sakshi")
user_2 = User("123", "pranav")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
print("___________________")
print(user_1.user_name)
print(user_2.followers)


# class Car:
#     def __init__(self, name):
#         self.name = name
#         self.brand =input("Enter the brand of the car: ")
#         self.price = 0   #defualt value
#         print(f"Brand: {self.brand}")
# car1 = Car("blizzard")
#
# print(f"Name: {car1.name}")
# print(f"Brand: {car1.brand}")
# print(f"Price: {car1.price}")

