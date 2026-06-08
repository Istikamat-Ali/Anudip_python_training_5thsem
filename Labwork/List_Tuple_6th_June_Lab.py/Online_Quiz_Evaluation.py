'''7. Online Quiz Evaluation
Problem Statement
Correct answers:
correct = ['A', 'C', 'B', 'D', 'A']
Student answers:
student = ['A', 'B', 'B', 'D', 'C']
Write a program to:
• Calculate score. 
• Display incorrectly answered question numbers. 
• Count correct and wrong answers. 
• Determine pass/fail (minimum 60%).'''
print("--------------------- Online Quiz Evaluation ---------------------")
#given list of correct answers
correct_answers = ['A', 'C', 'B', 'D', 'A']
#given list of student answers
student_answers = ['A', 'B', 'B', 'D', 'C']
#calculate score
score = 0
for i in range(len(correct_answers)):
    if correct_answers[i] == student_answers[i]:
        score += 1
#display incorrectly answered question numbers
print("Incorrectly Answered Question Numbers:")
for i in range(len(correct_answers)):
    if correct_answers[i] != student_answers[i]:
        print(i + 1)
#count correct and wrong answers
correct_answers_count = correct_answers.count('A')
wrong_answers_count = len(correct_answers) - correct_answers_count
print("Correct Answers Count:", correct_answers_count)
print("Wrong Answers Count:", wrong_answers_count)
#determine pass/fail (minimum 60%)
if score >= 60:
    print("Pass")
else:
    print("Fail")  
    

