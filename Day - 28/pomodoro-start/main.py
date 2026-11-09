from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
# This is last step (10)
def reset_timer():
    win.after_cancel(timer)    # it's stop the timer
    # reset time_text 00:00
    canvas.itemconfig(timer_text, text=f"00:00")
    # Title as a "Timer"
    timer_label.config(text="Timer", fg=GREEN)
    # Reset it's check marks
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
# sixth step
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps == 8:
        timer_label.config(text="Break 🙌🏻", fg=RED, )     # this is seventh step
        count_down(long_break_sec)

    # If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        timer_label.config(text="Short Break✌🏻",  fg=GREEN)
        count_down(short_break_sec)

    # If it's the 1st/3rd/5th rep:
    else:
        timer_label.config(text="Study Time 📖", fg=PINK)
        count_down(work_sec)


    # count_down(1 * 60)    # 5 minutes converted to seconds

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# Fourth step
def count_down(count):
    global timer
    count_min = math.floor(count / 60 )     # Return the largest integer  Eg. 4.3 => 4    So 300 seconds ➝ 300 / 60 = 5 mins
    count_sec = count % 60                  #  302 seconds => 302 % 60 = 2 (so display = 5:02).
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # fifth step
    if count > 0:
        timer = win.after(1000,count_down,count-1)
    # Eighth step
    else:                              # Once count hits 0, the timer has finished ticking(tick-tick-tick).
        start_timer()
        # Nineth step
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# firstly Create the tkinter window
win = Tk()
win.title("Pomodoro")
win.config(padx=100, pady=50, bg=YELLOW)


# Thirdly Create the label and Buttons on the window
timer_label = Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

start_button = Button(text="Start", highlightthickness=0,command=start_timer)     #highlightthickness is border size why we use? we use if you given a bg color since, remaining the border this highlightthickness is help to create a border color as per your requirement else as like bg color.
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark = Label(text="✔",font=(FONT_NAME,20),fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)

# Secondly create the canvas widget, insert the Tomato image on the window
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)   #the Canvas widget is like a blank drawing board.

tomato_image = PhotoImage(file="tomato.png")

canvas.create_image(100,112,image=tomato_image)    # Here you clear your removed tomato make it proper.
timer_text = canvas.create_text(103,130,text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))  # font is a tuple
canvas.grid(column=1,row=1)



win.mainloop()


""" win.after(1000, ...) ➤ Tells your program to wait 1000 milliseconds (1 second) before doing something. Think of it like: "Hey, hold on a sec... then do the next thing."
        count_down ➤ This is the name of the function that should be called after 1 second. So it’s saying: “Call this countdown function again.”
        count - 1 ➤ This is what we pass into the count_down() function. Imagine your timer says “5 seconds”... this will make it say “4” next time, then “3”, and so on."""

# import time
# count = 5
# while True:
#     time.sleep(1)
#     count-=1
# Example of after method
# def say_something(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# win.after(1000, say_something, 8,9,6)

# canvas.create_line(0, 0, 200, 100, fill="blue", width=3)       Draws a line between two points
# canvas.create_rectangle(50, 50, 150, 100, fill="green")        Draws a rectangle
# canvas.create_oval(100, 100, 200, 200, fill="red")             Draws a circle or ellipse
# canvas.create_text(200, 50, text="Hello Canvas!", font=("Arial", 16))         Adds text

# What is itemconfig()?
#
# In Tkinter, itemconfig() is a method used with the Canvas widget to modify t
# he properties of items that have already been drawn—like changing the color of a shape,
# updating text, or tweaking line thickness
# Syntax:
# canvas.itemconfig(item_id, option=value, ...)
# item_id: The ID returned when you created the item (e.g., from create_rectangle, create_text, etc.)
# option=value: Any property you want to change (like fill, outline, width, font, etc.)