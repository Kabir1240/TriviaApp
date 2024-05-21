from question_model import Question

class QuizBrain:
    """
    Class which handles the quiz game.
    """

    def __init__(self, question_list: list):
        """
        init QuizBrain
        :param question_list: list of Question objects
        """
        self.curr_question:Question
        self.curr_question = None
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self) -> bool:
        """
        checks if there are any questions remaining
        :return: True if there are questions remaining, False otherwise
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """
        updates question number, question and score. Returns updated question
        :return: updated question string
        """
        self.curr_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.curr_question.text}?: "

    def check_answer(self, user_answer: str) -> bool:
        """
        return True if user answered correctly, False otherwise. Updates score
        :param user_answer: user answer
        :return: True if user answered correctly, False otherwise
        """
        correct_answer = self.curr_question.answer

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False
