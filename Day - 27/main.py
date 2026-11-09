from  tkinter import *

# Create win page

# win = Tk()
# win.title("Simple GUI Page.")
# # win.geometry("500x500")
# win.minsize(500,500)
# #win.maxsize(800,800)
#
# # Label
#
# my_label = Label(text="Enter the name:",font=("Arial",20,"bold"))
# # my_label.pack(side="left")
# my_label.pack()
#
# # Change the label
# my_label["text"] = "New text"
# my_label.config(text="new text")     #config() method to update multiple attribute subsequent to object creation
#
# #Button
# # def button_clicked():
# #     print(" I got button_clicked")
# # button = Button(text="Click me", command=button_clicked)    # command equal to name of the function not, calling the function.
# # button.pack()
#
# #Change the label
#
# def button_clicked():
#     my_label.config(text="Button got clicked")
#     my_label.pack()
# button = Button(text="Click me", command=button_clicked)    # command equal to name of the function not, calling the function.
# button.pack()
#
# #Take input from user and then when the button clicked display the input which user written instead of existing label.
# def button_clicked():
#     my_label.config(text=input.get())
#     my_label.pack()
# button = Button(text="Click me", command=button_clicked)    # command equal to name of the function not, calling the function.
# button.pack()
# #Entry (It's just like Input)
#
# input = Entry(width = 10)
# input.pack()
# print(input.get())

"""
pack() will always start from the top and pack every other widget just below the previous change this 
place() the position in x-axis and y-axis  
grid() we write column and row in the format
Tip : we can't mix up grid and pack in the same program.
"""

win = Tk()
win.title("Simple GUI Page.")
win.minsize(500,500)
# win.config(padx=20,pady=20)
win.config(padx=100,pady=100)


my_label = Label(text="Enter the name:",font=("Arial",20,"bold"))
my_label.grid(column=0, row=0)
win.config(padx=100,pady=100)

my_label["text"] = "New text"
my_label.config(text="new text")


def button_clicked():
    my_label.config(text="Button got clicked")
    my_label.pack()
button = Button(text="Click me", command=button_clicked)    # command equal to name of the function not, calling the function.
button.grid(column=1,row=1)

#Take input from user and then when the button clicked display the input which user written instead of existing label.
def button_clicked():
    my_label.config(text=input.get())
    my_label.pack()
button = Button(text="Click me", command=button_clicked)    # command equal to name of the function not, calling the function.
button.grid(column=2,row=3)

input = Entry(width = 10)
input.grid(column=3,row=3)     #matrix
print(input.get())


win.mainloop()