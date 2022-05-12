from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("The Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280, text="Question", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.label = Label(text=f"Score: {self.quiz.score}")
        self.label.config(fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        true = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=0)

        false = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=1)
        self.bol = None

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached the end of this quiz your final score is "
                                        f"{self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        self.bol = self.quiz.check_answer("true")
        self.feedback(self.bol)

    def false(self):
        self.bol = self.quiz.check_answer("false")
        self.feedback(self.bol)

    def feedback(self, bol):
        if bol:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(300, func=self.get_next_question)
