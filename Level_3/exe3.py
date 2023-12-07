''' EXERCISE - 3 : ROCK, PAPER, SCISSOR '''

import random

#Chance to Win
win = [
    "P and R",
    "S and P",
    "R and S"
]

#Threat to Loose
loose = [
    "R and P",
    "P and S",
    "S and R"
]

print("Rock, Paper or Scissor!".center(100, "."))

print("You can either use r, p, s or you type it full!")

score = 0
for round in range(3):

    while True:
        #cpu's Turn
        cpu = random.choice(["R", "P", "S"])
        
        #Player's Turn
        print(f"\n----! ROUND : {round+1} ! ----".center(100))
        player = input("Rock, Paper or Scissor : ")
        player = player.upper()[0]

        #Preparing the Inputs
        match_str = f"{player} and {cpu}"

        #Match Input
        if player is cpu:
            print(f"!Tied!: You choose {player} & I'm choose {cpu}")

        elif match_str in win:
            print(f"!Winner!: You choose {player} & I'm choose {cpu}")
            score = score + 1
            break

        elif match_str in loose:
            print(f"!Looser!: You choose {player} & I'm choose {cpu}")
            break

        else:
            print("Error: Enter valid input!")

if(score<2):
    print(f"! YOU LOOSE THE GAME (score:{score}) !".center(100, ("-")))
else:
    print(f"! YOU WIN THE GAME (score:{score}) !".center(100, ("-")))

