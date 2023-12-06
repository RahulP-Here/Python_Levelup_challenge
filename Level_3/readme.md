[Scroll Down](#end)

# PYTHON : 10 DAYS LEVEL-UP CHALLANGE [DAY-3]

## 3. ROCK, PAPER, SCISSOR
Congratulations on the completion of second day.

On Day 3 We'll Create another game in Python called Rock, Paper & Scissor. Player will play this fanastic game with the computer. Game will declarify in 3 rounds. First computer will choose from rock, paper, scissor and after that player's turn. At the end of each round gueses are matched and according to the game rule winner win the round. For win the game player must been win minimum 2 rounds of the game.

### Require Topics :

- [Python Lists](https://www.w3schools.com/python/python_lists.asp) 
- [For Loop Python](https://www.w3schools.com/python/python_for_loops.asp)
- [While Loop Python](https://www.w3schools.com/python/python_while_loops.asp)
- [Python Random Module](https://docs.python.org/3/library/random.html)
- [Python f-string](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)

so here we go...

**Steps :**

- [Game Rule](#--define-rules)
- [Set Scratch Score](#--set-scratch-score)
- [Start The Game](#--start-the-game)
- [Cpu's Turn](#--cpus-turn)
- [Player's Turn](#--players-turn)
- [Match the Guesses](#--match-the-guesses)
- [Declaring the Result](#--declaring-the-result)
- [Output](#output)

---          
- [Logic Template](#logic-template)
---

### - Define Rules

Here, we first define the rules of winnig and losing the game in the [Python Lists](https://www.w3schools.com/python/python_lists.asp).

```python
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
```

### - Set Scratch Score
For the Score count of player we define `score` before starting of game which is `zero`. That will increse with the winning of the round and maximum reach of score is always 3. 

```python
score = 0
```
  

### - Start The Game
Now we start code for the game with help of [For Loop](https://www.w3schools.com/python/python_for_loops.asp) in Python.

```python
    for round in range(3):
        while True:

            #CPU's Turn
            #Player's Turn
            #Matching the Guesses with winnig list and losing list

    #Declaring the Result

```

* Here we use [For Loop](https://www.w3schools.com/python/python_for_loops.asp) with his [range( )](https://www.w3schools.com/python/gloss_python_for_range.asp) function to set the range when game is completed.

> Note : We need to use a [While loop](https://www.w3schools.com/python/python_while_loops.asp) for continuing the same iteration of [For loop](https://www.w3schools.com/python/python_for_loops.asp).

* In the loop we need to get choice from Cpu & Player, then matching it with the conditions which is store in winning and losing variables after that we've to displaying the result that player is win or lose the round. 
  


### - Cpu's Turn
```python
import random
for round in range(3):
    #CPU's Turn
    cpu = random.choice(["R", "P", "S"])

```
For Cpu's Turn we gonna use [Python random](https://docs.python.org/3/library/random.html) module which has
[`random.choice()`](https://www.w3schools.com/python/ref_random_choice.asp) who will help cpu to play its turn

### - Player's Turn
```python
    #Player's Turn
    player = input("Rock, Paper or Scissor : ")
```
For Player's Turn we gonna use [Python input()]() functions to ask player for choosing from R, P, S.

> Note: In that case if user enter whole word instead of one character like `['Rock' Instead of 'R'] or ['Paper' Instead of 'P']` then we fix that with the help of Python [String Indexing](https://www.w3schools.com/python/ref_string_index.asp) and also covert it into capital with `.upper()` method.

```python
    #Player's Turn
    player = input("Rock, Paper or Scissor : ")
    player = player.upper()[0]
```

### - Match the Guesses
Here first we created the match_str staterment with the help of [Python f-string](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings) which formatted the inputs according to the strings that belongs to the win and loose.
```python
    match_str = f"{player} and {cpu}"
    #Matching the Guesses with winnig list and losing list
```

> Note : [Python f-string](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings) is fromatted variables into string. 


Now match being compared with win and loose with the help of [if..elif..else](https://www.geeksforgeeks.org/python-if-else/)statement according to the match we declare that player is win the round or lose it. 
 * If player win the game the score being updated by increment via 1`score + 1` .

```python
    match_str = f"{player} and {cpu}"
    #Matching the Guesses with winnig list and losing list
    if match_str in win:
        #winner
        score = score + 1
        break
    elif match_str in loose:
        #loose
        break
```

>Note : If the player wins or loses the round the [While loop](https://www.w3schools.com/python/python_while_loops.asp) will be broke for starting a new game round `[new iteration of the loop]`.

 * We also need to define a tied situation when player and cpu guess same choice and a else block all the invalid inputs by player will be handel.

```python
    match_str = f"{player} and {cpu}"
    #Matching the Guesses with winnig list and losing list
    if player == cpu:
        #tied
    elif match_str in win:
        #winner
        score = score + 1
        break
    elif match_str in loose:
        #loose
        break
    else:
        #invalid input by player
```
>Note : In Tied and Invalid Input can't break the [While loop](https://www.w3schools.com/python/python_while_loops.asp) so the game re started with the same round. 


### - Declaring the Result
For declaring the result we use the [if...else] statement. The winner will be declared on the score.

```python
    #Declaring the Result
    if(score<2):
        #win
    else:
        #lose
```

##  Logic Template
```python
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

    for round in range(3):
    while True:

        #CPU's Turn
        cpu = random.choice(["R", "P", "S"])

        #Player's Turn
        player = input("Rock, Paper or Scissor : ")
        player = player.upper()[0]

        match_str = f"{player} and {cpu}"
        #Matching the Guesses with winnig list and losing list
        if player == cpu:
            #tied
        elif match_str in win:
            #winner
            score = score + 1
            break
        elif match_str in loose:
            #loose
            break
        else:
            #invalid input by player

    #Declaring the Result
        if(score<2):
            #win
        else:
            #lose
```

## output  
Output uploaded soon......... 


<br>

###### END


> See You In Level 4 👀....

