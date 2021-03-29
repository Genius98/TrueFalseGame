from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain

question_bank = [] #this bank consist of a list of question from data.py
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank) #new quiz brain object


#while loop will continue untill the end of the quiz
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}") #10/12 like quizscore/total marks