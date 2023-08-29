from ui import QuizInterface
from quiz_brain import QuizSys


class Quizzler(QuizSys, QuizInterface):
    """
    The Quizzler class represents the main application that combines QuizSys and QuizInterface.
    It manages the quiz flow and user interaction.
    """

    def __init__(self, question_bank):
        """
        Initialize the Quizzler application.
        :param question_bank: List of question data.
        """
        self._id = None
        self._i = 0
        self._answered = 0

        # Initialize QuizSys and QuizInterface
        QuizSys.__init__(self, question_bank)
        QuizInterface.__init__(self)

        # Configure true and false buttons
        self._true.config(command=lambda: self.check("true"))
        self._false.config(command=lambda: self.check("false"))

        # Start the quiz by showing the first question
        self.next_question()

    def next_question(self):
        """
        Move to the next question in the quiz.
        """
        self._canvas.config(bg="#fff")
        if self._i < len(self):
            self.set_question(f"Q{self._i + 1}: " + self.__getitem__(self._i).question)
        else:
            self.set_question(f"Your Score: {self._answered}/{len(self)}")
            self._true.config(state="disabled")
            self._false.config(state="disabled")

    def check(self, answer):
        """
        Check the user's answer and proceed to the next question.
        :param answer: The user's answer ("true" or "false").
        """
        if self._id is not None:
            self._root.after_cancel(self._id)
        color = "red"
        if self.check_answer(self._i, answer):
            self._answered += 1
            self._score.config(text=f"Score: {self._answered}")
            color = "green"
        self._i += 1
        self._canvas.config(bg=color)
        self._id = self._root.after(600, self.next_question)
