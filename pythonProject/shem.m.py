"""
# how to check the available modules
help("modules")

import  messages  as msg
msg.bye()
msg.hello()
"""
"""
# rock game of rock scissor
import random
while True:
    choices = ["rock","scissor","paper"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
       player = input("rock,paper,or scissor?: ").lower()

    if player ==computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
           print("computer: ",computer)
           print("player: ",player)
           print("you lose!")
        if computer == "scissor":
           print("computer: ",computer)
           print("player: ",player)
           print("you win!")
    elif player == "scissor":
        if computer == "rock":
           print("computer: ",computer)
           print("player: ",player)
           print("you lose!")
        if computer == "scissor":
           print("computer: ",computer)
           print("player: ",player)
           print("you win!")
    elif player == "paper":
        if computer == "scissor":
           print("computer: ",computer)
           print("player: ",player)
           print("you lose!")
        if computer == "rock":
           print("computer: ",computer)
           print("player: ",player)
           print("you win!")
    play_again = input("Play again?(yes/no)").lower()
    if play_again!="yes":
        break

print("Bye!")
"""
"""
#------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print(key)
        print("------------------------------------")
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C, or D):")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses  += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
#------------------------------------
def display_score(correct_guesses, guesses):
    print("------------------------------------")
    print("RESULTS")
    print("------------------------------------")
    print("Answers:",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses:", end=" ")
    for i in guesses :
        print(i,end=" ")
    print()
    score = int(correct_guesses/len(questions)*100)
    print("Your score is: "+str(score)+"%")
#------------------------------------
def play_again():
    response = input("Do you want to play again? (yes or no):")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#------------------------------------

questions = {
"Who created python?: ": "A",
"What year was Python created?: ": "B",
"Python is tribited to which comedy group?: ": "C",
"Is the Earth round?: ": "A"
}
options = [["A.Guiddo Van Rossum","B.Elon Musk","C.Bill Gates","D.Mark Zukerburg"],
           ["A.1989","B.1991","C.2000","D.2016"],
           ["A.Lonely Island","B.Smosh","C.Monty Python","D.SNL"],
           ["A.True","B.False","C.Sometimes","D.What's the Earth"]]

new_game()

while play_again():
    new_game()

print("Thank you")
"""


#poop classes and object

from vehicle import Vehicle

vehicle_1 = Vehicle("Toyota","lexus",2022,"White")
vehicle_2 = Vehicle("Marcedes","AMG",2015,"Black")
vehicle_3 = Vehicle("Ford","luxury",2016,"Yellow")

print(vehicle_1.wheels)
print(vehicle_1.make)
print(vehicle_1.color)
print(vehicle_1.year)
print(vehicle_1.model)

vehicle_2.drive()
vehicle_1.stop()


