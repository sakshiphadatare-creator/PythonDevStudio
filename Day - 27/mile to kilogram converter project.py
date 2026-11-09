"""
steps:
first create window/front page
declare\initialize which you want to display into the window like label, button, entry...ect
then write it's position where you display over the window
Create a function to calculate the result
"""

from tkinter import *

def convert_mile():
    mile = float(enter_mile.get())
    result_km = mile * 1.609
    kilo_result_label.config(text=f"{round(result_km)}")
def delect_screen():
    win.destroy()

win = Tk()
win.title("Mile to Km Converter")
# win.geometry("300x300")
win.minsize(400,200)
win.config(padx=60,pady=40)


enter_mile = Entry(width = 8, font=("Arial",18))
enter_mile.grid(column=1,row=0)

mile_label = Label(text="Miles", font=("Arial",18))
mile_label.grid(column=2,row=0)

is_equal_to = Label(text="is equal to",font=("Arial",18))
is_equal_to.grid(column=0,row=1)

kilo_result_label = Label(text='0',font=("Arial",18))
kilo_result_label.grid(column=1,row=1)

kilo_label = Label(text="km",font=("Arial",18))
kilo_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate", font=("Arial",18), command=convert_mile)
calculate_button.grid(column=1,row=2)

delect_button = Button(text="Delect", font=("Arial",18), command=delect_screen)
delect_button.grid(column=1,row=3)
win.mainloop()