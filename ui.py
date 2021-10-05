from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        wrong_image = PhotoImage(file="./images/false.png")
        right_image = PhotoImage(file="./images/true.png")
        self.window.config(width=350, height=450)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Your question will go\nHello",
                                                     font=("Arial", 20, "italic"))
        self.button_wrong = Button(image=wrong_image, highlightthickness=0, command=self.got_it_wrong)
        self.button_wrong.grid(row=2, column=1)
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.got_it_right)
        self.right_button.grid(row=2, column=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text,
                                   text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def got_it_right(self):
        is_right = self.quiz.check_answer("True")
        self.is_right_(is_right)

    def got_it_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.is_right_(is_right)

    def is_right_(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)
