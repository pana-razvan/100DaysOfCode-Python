from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for item in question_data:
  question_bank.append(Question(item["question"], item["correct_answer"]))

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
  new_quiz.next_question()
print("Congratulations! You've completed the quiz.")
print(f"Your final score is {new_quiz.score}/{len(new_quiz.question_list)}")