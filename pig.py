import random

def roll():
    min=1
    max=6
    roll=random.randint(min,max)
    return roll

while True:
    players=input("enter the number of players (2-4) :")
    if players.isdigit():
        players=int(players)

        if 2 <= players <= 4 :
            break
        else:
            print("Must be between 2-4 players !")
    
    else:
        print("Invalid , try again !")


max_score=50
player_scores=[0 for _ in range( players)]

while max(player_scores) < max_score :

    for index in range(players):

        print("\n Player number ",index+1,"turns has just started !")
        print("Your total score is :",player_scores[index],"\n")
        current_score=0

        while True:
            should_roll=input("would you like to roll -yes or no :").lower()
            if should_roll != "yes":
                break

            value=roll()
            if value == 1:
                print("you rolled a 1 ! turn done !")
                current_score=0
                break
            else:
                current_score+=value
                print(" you rolled a :",value)

            print("your score is :",current_score)

        player_scores[index]+=current_score
        print("Your total score is :",player_scores[index])

max_score=max(player_scores)
winner=player_scores.index(max_score)
print("\n")
print("*"*140)
print("Player number ",winner+1,"is the winner with a score of :",max_score)