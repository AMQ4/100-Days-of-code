import html
from question_model import Question


class QuizSys:
    """
    This class represents the quiz system that manages the question bank and checks answers.
    """

    def __init__(self, question_bank=None):
        """
        Initialize the QuizSys with an optional question bank.
        :param question_bank: List of dictionaries containing question and answer data.
        """
        self._questionBank = []
        if question_bank is not None:
            for question in question_bank:
                self.add_question(html.unescape(question['question']), question['correct_answer'].lower())

    def add_question(self, question, answer):
        """
        Add a question to the question bank.
        :param question: The question text.
        :param answer: The correct answer to the question.
        """
        self._questionBank.append(Question(question, answer))

    def check_answer(self, qNO, answer):
        """
        Check if the provided answer is correct for the given question number.
        :param qNO: The question number.
        :param answer: The answer to check against.
        :return: True if the answer is correct, False otherwise.
        """
        if answer == self._questionBank[qNO].answer:
            return True
        else:
            return False

    def __getitem__(self, index):
        """
        Get a question from the question bank using indexing.
        :param index: The index of the question.
        :return: The Question object.
        """
        return self._questionBank[index]

    def __len__(self):
        """
        Get the number of questions in the question bank.
        :return: The length of the question bank.
        """
        return len(self._questionBank)
