questions = ("What is the capital of Japan? ",
             "Which of the following is NOT a programming language? ",
             "What is H2O commonly known as?",
             "Which planet is known as the Red Planet? ",
             "Who wrote the play 'Romeo and Juliet'? ")

options = (('A. Seoul', 'B. Beijing', 'C. Tokyo' , 'D. Bangkok'),
           ('A. Python', 'B. Java', 'C. HTML' , 'D. Rubt'),
           ('A. Oxygen', 'B. Water', 'C. Hydrogen' , 'D. Carbon Dioxide'),
           ('A. Earth', 'B. Venus', 'C. Mars' , 'D. Jupiter'),
           ('A. William Shakespeare', 'B. Charles Dickens', 'C. Mark Twain' , 'D. Jane Austen')
           )

answers = ('C', 'C', 'B', 'C', 'A')

guesses = []

score = 0

question_num = 0

for question in questions:
  print('---------------')
  print(question)
  for option in options[question_num]:
    print(option)
  guess = input("Enter your answer('A','B','C','D','E'): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("Correct!")
  else:
    print("Incorrect!")
    print(f"{answers[question_num]} is the correct answer!")
  question_num += 1

print("-----------------------------")
print("          RESULTS")
print("-----------------------------")
print("Answers: ", end=' ')
for answer in answers:
  print(answer, end = ' ')

print("\nGuesses: ", end=' ')
for guess in guesses:
  print(guess, end = ' ')

score = int((score / len(questions)) * 100)
print(f"\nYour Score: {score}")