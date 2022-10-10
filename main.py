from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for item in question_data:
    question = item['question']
    answer = item['correct_answer']
    choices = item['incorrect_answers']

    data = Question(question, answer, choices)
    question_bank.append(data)

text = QuizBrain(question_bank)

while text.still_has_question():
    text.next_question()