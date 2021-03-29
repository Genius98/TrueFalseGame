class QuizBrain:

    def __init__(self, q_list):  #initialize the attribute,q_list as a param which is passed over
        self.question_number = 0  #creating attribute
        self.score = 0 #user's initial score is zero
        self.question_list = q_list

    def still_has_questions(self): #to keep tracking on nect ques
        if self.question_number < len(self.question_list):
            return  True
        else:
            False
    def next_question(self): #creating method & get hold the current question
        current_question = self.question_list[self.question_number] #ques no will start from zero & its going into list which is basically going to be our list of question bank from our main.py & it has Question attribute which has text & answer attribute(question_model.py)

        self.question_number += 1  # to increase the question number by 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")#inserting current ques & #saving the user's input inside a variable
        self.check_answer(user_answer, current_question.answer) #correct_answer=current_question.answer


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1 #whenever the answer is correct score will be incremented
            print("You got it right!")
        else:
            print("That's wrong. :(")

        print(f"The correct answer was: {correct_answer}.") #once the if else block ends
        print(f"Your current score is: {self.score}/{self.question_number}") #printing the score after every ques they being asked like 30/50 or 50/50
        print("\n")