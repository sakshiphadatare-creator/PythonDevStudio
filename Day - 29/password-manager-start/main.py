#TODO:1 Create main window with insert imag
#TODO:2 Add labels, entries and button.
#TODO:3 Create definition "save" to get the information & store a new variable open the file & store into file then delete the entry.
#TODO:4 Generate password user pyperclip

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]
    password_number = [choice(numbers) for _ in range(randint(2,4))]
    password_keys = password_letter + password_symbol + password_number
    shuffle(password_keys)

    password = "".join(password_keys)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {"website": website,
                "email": email,
                "password": password}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please make sure you haven't left any fields empty!",)
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)                 # load to use read data from the json file
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 4)
        else:
            # Updating old data with new data
            data.update(new_data)                       # Obviously update the data to the json file

            with open ("data.json","w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)   # 4 place Indent  # dump to use write into the json file
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", text="No data file found.")
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email} | Password:{password}")
        else:
            messagebox.showinfo(title="Error", text=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Password Manager")
win.config(padx=50, pady= 50)
photo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=400, height=200 )
canvas.create_image(100,100,image= photo_image, anchor="center")
canvas.grid(row=0, column=1,columnspan=2,sticky="ew")

#labels
website_label=Label(text="Website:")
website_label.grid(row=1, column=0,sticky="ew")
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0,sticky="ew")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0,sticky="ew")

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1,sticky="ew")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2,sticky="ew")
email_entry.insert(0,"sakshiphatare2021@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1,sticky="ew")
#Buttons
search_button = Button(text="Search", command= find_password, )
search_button.grid(row=1, column=2,sticky="ew")
generate_button = Button(text="Generate", width=10, command=password_generator)
generate_button.grid(row=3, column=2,sticky="ew")
add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2,sticky="ew")


win.mainloop()



# # Actual code
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
# def password_generator():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#     nr_letters = randint(8, 10)
#
#     password_letter = [choice(letters) for _ in range(nr_letters)]
#     password_symbol = [choice(symbols) for _ in range(randint(2,4))]
#     password_number = [choice(numbers) for _ in range(randint(2,4))]
#     password_keys = password_letter + password_symbol + password_number
#
#     shuffle(password_keys)
#
#     password = "".join(password_keys)
#     password_entry.insert(0, password)      # Display the password on user interface simply, I called insert method to the password on the position of entry password.
#     pyperclip.copy(password)                      # copy the password automatically so we can paste anywhere
#
#     # password = ""
#     # for char in password_keys:
#     #     password += char
#     # print(password)
#
# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     if len(website) == 0 or len(email) == 0 or len(password) == 0:
#         messagebox.showinfo("Oops", "Please make sure you haven't left any fields empty!",)
#     else:
#         is_ok = messagebox.askokcancel(title=website, message=f"these are the details \nentered: Email:{email} \n"
#                                                       f" Password:{password}\n Is it ok to save?")
#
#         if is_ok:
#             with open("data.txt", "a") as data_file:
#                 data_file.write(f"{website} | {email} | {password}\n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
#
# # ---------------------------- UI SETUP ------------------------------- #
# win = Tk()
# win.title("Password Manager")
# win.config(padx=50, pady= 50)
# photo_image = PhotoImage(file="logo.png")
# canvas = Canvas(width=200, height=200 )
# canvas.create_image(100,100,image= photo_image)
# canvas.grid(row=0, column=1)
#
# #labels
# website_label=Label(text="Website:")
# website_label.grid(row=1, column=0)
#
# email_label=Label(text="Email/Username:")
# email_label.grid(row=2, column=0)
#
# password_label = Label(text="Password:")
# password_label.grid(row=3, column=0)
#
# #Entries
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
#
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# #email_entry.insert(0,"sakshiphatare2021@gmail.com")     # insert the text at the given index syntax: insert(INDEX, text) or insert(END, text) append text to the widget
#
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
#
#
# #Buttons
# generate_button = Button(text="Generate Password", width=10, command=password_generator)
# generate_button.grid(row=3, column=2)
#
# add_button = Button(text="Add", width=33, command=save)         #exculte width is 36
# add_button.grid(row=4, column=1, columnspan=2)
#
# win.mainloop()




# --------------------------Rough work-----------------------------#

# file = open("data.txt","a")
#     file.write(f"{web} | {email} | {password}\n")
#
#     file.close()
# messagebox.showinfo(title="Title", message="Enter your password")

# Join()

# my_list = ["Sakshi", "Prashant", "pranav"]
# x = "#".join(my_list)
# print(x)
# x = "".join(my_list)
# print(x)
# x = " ".join(my_list)
# print(x)

# pyperclip
# Pyperclip is a cross-platform Python module for copy and paste clipboard functions.
# Example:

# # importing the library
# import pyperclip as pc
# text1 = "GeeksforGeeks"
# # copying text to clipboard
# pc.copy(text1)
# # pasting the text from clipboard
# text2 = pc.paste()
# print(text2)