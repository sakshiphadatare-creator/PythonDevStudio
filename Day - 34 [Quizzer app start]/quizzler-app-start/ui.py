from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def  __init__ (self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: {}",fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,width =280 , text="question",fill=THEME_COLOR , font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")

        self.button_false = Button(image=false_image, highlightthickness=0)
        self.button_false.grid(row=2, column=0)
        self.button_true = Button(image=true_image, highlightthickness=0)
        self.button_true.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
