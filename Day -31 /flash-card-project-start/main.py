"""
Purpose of the program
This is a flashcard app built using Tkinter and Pandas.
It helps users learn French words by showing a French word first, then flipping the card to show its English meaning after 3 seconds.
If the user knows the word, they can click a button to remove it from the learning list.
"""
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}  # random.choice(to_learn) instead of this we create only item dict and inside the function we write as global variable
to_learn = {}

try:
    data = pandas.read_csv("data/words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")      #convert data into dictionary

def next_card():
    global current_card, flip_timer
    win.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text = "French",fill="black")
    canvas.itemconfig(card_word, text = current_card["French"],fill="black")   # this line shows french words
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = win.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text= current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words.csv", index=False)
    next_card()


win = Tk()
win.title("Flashy")
win.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

## Schedule flip_card to be called after 3 seconds (3000 milliseconds)
flip_timer = win.after(3000, func=flip_card)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 50, "bold"))
canvas.configure( bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")
unknown_button = Button(image=cross_image, command= next_card)
unknown_button.grid(row=1, column=0)
known_button = Button(image=check_image, command= is_known)   # first we this known_button = Button(image=check_image, command= next_card) then modify for if user known this word then that word remove from the dictionary
known_button.grid(row=1, column=1)

next_card()

win.mainloop()



# what is itemconfig()
#Specifies one or more tags to apply to the image.
# When used in Canvas.itemconfigure, this replaces any existing tags for the image.
# An empty list may also be specified. The default value is an empty list.

"""
next_card()
Picks a random word from to_learn.
Updates the canvas to show the French word.
Starts a timer to flip the card after 3 seconds.

flip_card()
Changes the card to show the English translation.
Updates the background image and text color.

is_known()
Removes the current word from the list.
Saves the updated list to words.csv.
Shows the next card."""