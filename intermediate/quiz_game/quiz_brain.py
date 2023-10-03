from intermediate.quiz_game.main import take_question_list


class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.question_list = take_question_list()
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number].text
        actual_answer = self.question_list[self.question_number].answer

        user_answer = input(f"Q.{self.question_number + 1}: {question} (True/False)? ")

        self.question_number += 1
        self.check_answer(user_answer, actual_answer)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() != actual_answer.lower():
            print(f"That's wrong!")
        else:
            print("You got it right!")
            self.score += 1
        print(f"The correct answer was: {actual_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()


qb = QuizBrain()

while qb.still_has_question():
    qb.next_question()

print(f"You have completed the quiz.")
print(f"Your score is {qb.score}/{qb.question_number}")