# try:
#     file = open("a_file.txt")
#     dictionary = {"key":"value"}
#     print(dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as key_error:
#     print(f"that {key_error} does not exist")
# else:
#     contect = file.read()
#     print(contect)
# finally:
#     raise TypeError("Occurs an Exception")
# file.close()
# print("Program Execute Successfully")

height = float(input("Height:"))
weight = float(input("Weight:"))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / (height ** 2)     # height * height
print(bmi)


fruits = ["Apple", "Pear", "Orange"]
# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("This index has out of the range")
    else:
        print(fruit + " pie")

make_pie(2)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass
    return total_likes
count_likes(facebook_posts)

