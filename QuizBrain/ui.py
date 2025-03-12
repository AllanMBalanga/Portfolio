from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quizzes: QuizBrain):
        self.quiz = quizzes
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300,height=250,highlightthickness=0,bg="white")
        self.question = self.canvas.create_text(150,125,
                                                width= 280, # margin sa loob ng text
                                                text="Question Mark?",
                                                font=("Arial",20,"italic"),
                                                fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)

        check = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=check,highlightthickness=0,bg=THEME_COLOR,command=self.true_answer)
        self.true_button.grid(row=2,column=0)

        cross = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=cross,highlightthickness=0,bg=THEME_COLOR,command=self.false_answer)
        self.wrong_button.grid(row=2,column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=text)
        else:
            self.true_button.destroy()
            self.wrong_button.destroy()
            self.score.destroy()
            self.canvas.itemconfig(self.question, text=f"That is the end of the quiz. Your final score is: {self.quiz.score} ")

    def true_answer(self):
        self.feedback(self.quiz.check_answer("true"))

    def false_answer(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self,right):
        if right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)