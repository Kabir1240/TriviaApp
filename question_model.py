import html

class Question:
    """
    Questions for QuizBrain
    """
    def __init__(self, text, answer):
        """
        init Question and save its answer
        :param text: question
        :param answer: answer
        """
        self.text = html.unescape(text)
        self.answer = answer
