from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.q_no_label = Label(text="Question: 1", bg=THEME_COLOR, fg="white")
        self.q_no_label.grid(column=0, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", borderwidth=1, relief="solid", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125,
                                                text="Question goes here.",
                                                font=("Arial", 18, "italic"),
                                                fill=THEME_COLOR,
                                                width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_btn_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_btn_img, highlightthickness=0, command=self.true_btn_function)
        self.true_btn.grid(column=0, row=2)
        false_btn_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_btn_img, highlightthickness=0, command=self.false_btn_function)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number}")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the Quiz.\n"
                                                       f"Your final score is: {self.quiz.score}/10")
            self.disable_buttons()
        self.q_no_label.config(text=f"Question: {self.quiz.question_number}")

    def true_btn_function(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_btn_function(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.disable_buttons()
        self.window.after(1000, self.get_next_question)
        if self.quiz.still_has_questions():
            self.window.after(1000, self.enable_buttons)

    def disable_buttons(self):
        self.true_btn["state"] = DISABLED
        self.false_btn["state"] = DISABLED

    def enable_buttons(self):
        self.true_btn["state"] = ACTIVE
        self.false_btn["state"] = ACTIVE
