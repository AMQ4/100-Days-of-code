import random
from question_model import Question


class Quiz:

    def __init__(self, question_bank=None):
        self.questionBank = []
        self.score = 0
        self.i = 0
        if question_bank is not None:
            for question in question_bank:
                self.add_question(question['text'], question['answer'])
            random.shuffle(question_bank)

    def add_question(self, question, answer):
        self.questionBank.append(Question(question, answer))

    def check_answer(self, answer):
        if answer == self.questionBank[self.i].answer:
            return True
        else:
            return False

    def update_score(self, result):
        print(f"{'You got it right' if result is True else 'That is wrong.'}!")
        print(f"The correct answer was: {self.questionBank[self.i].answer}.")
        self.score = self.score + 1 if result is True else self.score
        self.i += 1
        print(f"Your current score is: {self.score}/{self.i}")

    def ask(self):
        answer = input(f"Q.{self.i + 1}:" + self.questionBank[self.i].question + "`true` ir `false` ?\n> ").lower()
        self.update_score(self.check_answer(answer))

    def __del__(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.i}")
