import requests
from question_model import Question
from quiz_brain import QuizBrain
from main_quiz_ui import TriviaUI
from params_ui import ParamsUI

"""
Main file for quiz game
"""


if __name__ == "__main__":
    params_ui = ParamsUI()
    parameters = params_ui.parameters

    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()

    # adds questions and their answers as Question objects to question bank
    question_bank = []
    for item in data["results"]:
        new_question = Question(text=item["question"], answer=item["correct_answer"])
        question_bank.append(new_question)

    # Makes new QuizBrain and gives it the Question objects list
    quiz = QuizBrain(question_bank)

    # Starts UI for quiz
    TriviaUI(quiz)
