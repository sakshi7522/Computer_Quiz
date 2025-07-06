print("\n")
print("##### WELCOME TO THE COMPUTER QUIZ #####")

print(" ")
play = input("Do you want to start the quiz? ")

if play.lower() != "yes":
    print("YOU CHOOSE TO QUIT, BYE :(")
    quit()

## variable to store score
score = 0

## LIST OF QUIZ QUESTIONS ##

#Q1.
Q1 = input("Question 1 : What does CPU stands for? (Type 'hint' for a clue) ")
#Hint
if Q1.lower() == "hint":
    print("HINT : It's the brain of the computer.")
    Q1 = input("Now enter your answer: ")

if Q1.lower() == "central processing unit":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT!")

#Q2.
Q2 = input("Question 2 : What does GPU stands for? (Type 'hint' for a clue)")
#Hint
if Q2.lower() == "hint":
    print("Hint: Used to render images, especially in games.")
    Q2 = input("Now enter your answer: ")

if Q2.lower() == "graphics processing unit":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT!")

#Q3.
Q3 = input("Question 3 : What does RAM stands for? (Type 'hint' for a clue)")
#Hint
if Q3.lower() == "hint":
    print("Hint: It's a type of temporary memory.")
    Q3 = input("Now enter your answer: ")

if Q3.lower() == "random access memory":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT!")

#Q4.
Q4 = input("Question 4 : What does ROM stands for? (Type 'hint' for a clue)")
#Hint
if Q4.lower() == "hint":
    print("Hint: Memory you can't change, but it's essential for booting.")
    Q4 = input("Now enter your answer: ")

if Q4.lower() == "read only memory":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT!")

#Q5.
Q5 = input("Question 5 : What does PSU stands for? (Type 'hint' for a clue)")
#Hint
if Q5.lower() == "hint":
    print("Hint: Provides electricity to the entire computer.")
    Q5 = input("Now enter your answer: ")

if Q5.lower() == "power supply unit":
    print("CORRECT!")
    score+=1
else:
    print("INCORRECT!")


## RESULT
if score == 1:
    print(f"YOU GOT {score} QUESTION CORRECT")

else:
    print(f"YOU GOT {score} QUESTIONS CORRECT")
 

print(f"YOU SCORED {score/5*100} %")

print(" ")

print("##### THANK YOU FOR PLAYING #####")


