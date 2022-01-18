class QuizBrain:

  def __init__(self, question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    """Retrieve the item at the current question_number and from the question_list
    Uses the input() function to show the user the Question text and ask for the user's answer. Returns the answer as str()"""
    question_text = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {question_text.text} (True/False)?: ")
    self.check_answer(user_answer, question_text.answer)

  
  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      print("You got it right!")
      self.score += 1
    else:
      print("That's wrong!")
    print(f"The correct answer was {correct_answer}.")
    print(f"Your current score is {self.score}/{self.question_number}.")
    print("\n")

# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're at the end of the quiz