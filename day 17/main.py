import data
from quiz_brain import Quiz

quiz = Quiz(data.question_data)
for i in range(len(quiz.questionBank)):
    quiz.ask()
