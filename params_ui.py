from tkinter import *

THEME_COLOR = "#375362"

class ParamsUI:
    def __init__(self) -> None:
        """
        Creates UI that allows user to set params for a request for open trivia
        """

        self.cat_dictionary = \
            {
                "Film": 11,
                "Books": 10,
                "Music": 12,
                "Video Games": 15,
                "Computers":18,
                "Maths": 19,
                "Science & Nature": 17,
                "History": 23,
                "Mythology": 20,
            }

        self.parameters = {}

        # create window
        self.window = Tk()
        self.window.title("Trivia Game!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # create labels
        self.category_label = Label(text="Category: ", font=("Arial", 10, "bold"), bg=THEME_COLOR)
        self.amount_label = Label(text="Number of Questions: ", font=("Arial", 10, "bold"), bg=THEME_COLOR)
        self.category_label.grid(row=0, column=0)
        self.amount_label.grid(row=1, column=0)

        # create dropdown
        self.selected_option = StringVar()
        self.dropdown = OptionMenu(self.window, self.selected_option,
                              "Books",
                              "Music",
                              "Video Games",
                              "Computers",
                              "Maths",
                              "Science & Nature",
                              "History",
                              "Film",
                              "Mythology",
                              )

        self.dropdown.grid(row=0, column=1)

        # create spinbox
        self.spinbox = Spinbox(from_=1, to=20, width=5)
        self.spinbox.grid(row=1, column=1, pady=15)

        # create button
        self.button = Button(text="Accept", font=("Arial", 10, "bold"), command=self.set_params)
        self.button.grid(row=2, column=1)

        # tk main loop
        self.window.mainloop()

    def set_params(self) -> None:
        """
        sets params and destroys UI
        :return: None
        """

        # update params category
        user_category = self.selected_option.get()
        category_param = self.cat_dictionary[user_category]
        self.parameters["category"] = category_param

        # update params amount
        amount_param = self.spinbox.get()
        self.parameters["amount"] = amount_param

        # update params type
        self.parameters["type"] = "boolean"

        # destroy UI
        self.window.destroy()
