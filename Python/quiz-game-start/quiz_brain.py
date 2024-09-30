class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score=0
        self.questions = q_list

    def next_question(self):
        """Shows the user the next question, and gets the answer."""

        ans= input(f"Q{self.question_number+1}:{self.questions[self.question_number].question}?(True/False)").lower()
        self.question_number += 1
        self.check_answer(ans,self.questions[self.question_number].answer.lower())
        return ans

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def check_answer(self, answer, correct):
        if answer == correct:
            print("You got it!")
            self.score += 1
        else:
            print("That's not correct.")
        print(f"The correct answer was: {correct}")
        print(f"Your score is: {self.score}/{self.question_number}.\n\n")





