from tkinter import *
from tkinter_widgets import TkinterWidgets
from quiz_brain import QuizBrain
from functools import partial

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, 'italic')
LABEL_FONT = ("Arial", 10, 'bold')
TRUE_IMAGE_PATH = "images/true.png"
FALSE_IMAGE_PATH = "images/false.png"


class TriviaUI:
    def __init__(self, quiz_brain:QuizBrain):
        """
        Creates Tk window, initializes objects and starts mainloop
        """
        self.question_text = None
        self.question_answered = True
        self.quiz_brain = quiz_brain

        # create window and images
        self.window = Tk()
        self.window.title("Trivia Game!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # create widgets
        self.widgets = TkinterWidgets()
        self.create_photoimages()
        self.create_canvas()
        self.create_labels()
        self.create_buttons()

        self.get_next_question()
        # main loop
        self.window.mainloop()

    def create_photoimages(self) -> None:
        """
        creates a PhotoImage dictionary which is stored in the widgets data struct
        :return: None
        """

        # create 4 PhotoImages
        true_button_image = PhotoImage(file=TRUE_IMAGE_PATH)
        false_button_image = PhotoImage(file=FALSE_IMAGE_PATH)

        # create dictionary
        image_dict = {
            "true image": true_button_image,
            "false image": false_button_image,
        }

        # store in widgets
        self.widgets.add_image_dict(image_dict)

    def create_canvas(self) -> None:
        """
        creates canvas, adds image. Stores canvas in widgets
        :return: None
        """
        # create canvas with logo image
        canvas = Canvas(width=300, height=250)
        self.question_text = canvas.create_text(150, 125, text="Some Question", width=280,
                                                fill=THEME_COLOR, font=("Arial", 15, "italic"))
        canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.widgets.add_canvas("canvas", canvas)

    def create_labels(self) -> None:
        """
        creates required Label objects, organizes them in grid format, saves them in widgets
        :return: None
        """

        label_1 = Label(text="Score: 0", font=LABEL_FONT, fg="white", bg=THEME_COLOR)
        label_1.grid(row=0, column=1)

        label_dict = {
            "score": label_1,
        }

        self.widgets.add_label_dict(label_dict)


    def create_buttons(self) -> None:
        """
        creates required Button objects, organizes them in grid format, saves them in widgets
        :return: None
        """
        true_button_image = self.widgets.get_images("true image")
        false_button_img = self.widgets.get_images("false image")

        button_1 = Button(image=true_button_image, width=100, height=97, highlightthickness=0,
                          command=partial(self.check_answer, "true"))
        button_2 = Button(image=false_button_img, width=100, height=97, highlightthickness=0,
                          command=partial(self.check_answer, "false"))

        button_1.grid(row=2, column=0, pady=20, padx=20)
        button_2.grid(row=2, column=1, pady=20, padx=20)

        button_dict = {
            "true": button_1,
            "false": button_2,
        }

        self.widgets.add_button_dict(button_dict)

    def get_next_question(self) -> None:
        """
        updates question in canvas.
        :return: None
        """
        canvas = self.widgets.get_canvas("canvas")
        canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            next_question = self.quiz_brain.next_question()
            canvas.itemconfig(self.question_text, text=next_question)
            self.question_answered = False
        else:
            canvas.itemconfig(self.question_text, text=f"Final score: {self.quiz_brain.score}/{self.quiz_brain.question_number}")

    def check_answer(self, answer:str):
        """
        checks if user answer correctly or not. Updates score
        :param answer: true or false string
        :return: None
        """

        if not self.question_answered:
            score_label = self.widgets.get_labels("score")
            canvas = self.widgets.get_canvas("canvas")

            is_right = self.quiz_brain.check_answer(answer)
            updated_score = self.quiz_brain.score
            question_number = self.quiz_brain.question_number

            if is_right:
                canvas.config(bg="green")
            else:
                canvas.config(bg="red")

            score_label.config(text=f"Score: {updated_score}/{question_number}")
            self.question_answered = True
            self.window.after(1000, self.get_next_question)
