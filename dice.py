"""
Question 1:
Write a program to design a Dice game. There should be two players. Ask the users to enter their names and roll the dice(four times each). Display the scores and calculate the final score and print the name of the winner.
"""

import random

player = ""
score = {}
names = {}
def get_name(name):
    n = ""
    while not n:
        n = input(f"ENTER THE NAME {name}: ")   """read the player names"""
    return n

def dice(name):  """finding the score of each player in each turn by a random throwing of dice"""
    dices = random.choices(range(1,7),k=2)
    print(f"{names[name]} threw: {dices}", end = " ")
    if sum(dices) % 2 == 0:
        score[name] += 10

    else:
        score[name] -= 4

def disp_score():   """displaying the score of each player"""
    for n in score:
        print(f"  {names[n]} has got {score[n]} points.")

def won(s,n): """displaying the name of winner """
    disp_score()
    if score["player1"] > score["player2"]:
        print(f"{names['player1']} won")
    else:
        print(f"{names['player2']} won") 





for n in ["player1","player2"]:
    names[n] = get_name(n)
    score[n] = 0



for j in range(8):
    # switches between player1 and player2
    player = "player1" if player != "player1" else "player2"

    print(f"chance {j//2 + 1}: it is {names[player]}'s turn.")
    disp_score()
    dice(player)

won(score,names)

