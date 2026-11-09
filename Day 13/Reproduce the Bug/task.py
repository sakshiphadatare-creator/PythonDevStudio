from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # starts from 0 because list items always starts from 0.
print(dice_images[dice_num])
