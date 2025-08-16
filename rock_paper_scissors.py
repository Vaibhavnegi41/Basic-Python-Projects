import random

user_wins=0
computer_wins=0

options=["rock","paper","scissors"]

while True:
    user_value=input("type Rock/Paper/Scissors or Q to Quit :").lower()

    if user_value=="q":
        break

    if user_value not in options:
        print("please enter the valid value !")
        continue

    random_value=random.randint(0,2)
    # rock:0 paper:1 and scissors:2

    computer_pick=options[random_value]
    print("Computer picked :",computer_pick)

    if user_value=="rock" and computer_pick=="scissors":
        print("you win dear !")
        user_wins+=1
        continue

    elif user_value=="paper" and computer_pick=="rock":
        print("you win dear !")
        user_wins+=1
        continue

    elif user_value=="scissors" and computer_pick=="paper":
        print("you win dear !")
        user_wins+=1
        continue

    elif user_value=="scissors" and computer_pick=="scissors":
        print("There is a Tie !")
        continue
    elif user_value=="paper" and computer_pick=="paper":
        print("There is a Tie !")
        continue
    elif user_value=="rock" and computer_pick=="rock":
        print("There is a tie !")
        continue

    else:
        print("you lost dear !")
        computer_wins+=1


print(" You Win ",user_wins," times .")
print("computer win ",computer_wins,"times  .")




