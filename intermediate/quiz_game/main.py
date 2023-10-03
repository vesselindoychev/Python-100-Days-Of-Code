from data import question_data


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return self.text, self.answer


def take_question_list():
    all_questions = []
    for i in range(len(question_data)):
        t = question_data[i]['text']
        a = question_data[i]['answer']
        q = Question(t, a)
        all_questions.append(q)
    return all_questions

