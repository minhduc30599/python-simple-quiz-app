import random

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.current_score = 0
        self.question_list = question_list

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.current_score += 1
            print('You got it right!')
            print(f'Your current score is: {self.current_score}/{self.question_number}.')
        else:
            print("That's wrong.")
            print(f'Your current score is: {self.current_score}/{self.question_number}.')

    def next_question(self):
        current_question = self.question_list[self.question_number]
        multi_choices = current_question.choices + list(current_question.answer.split("-"))
        random.shuffle(multi_choices)
        user_answer = input(f'Q{self.question_number}.{current_question.question} \n ({str(multi_choices)[1:-1]}): ')
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)