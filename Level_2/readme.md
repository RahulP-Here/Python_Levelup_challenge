[Scroll Down](#end)

# PYTHON : 10 DAYS LEVEL-UP CHALLANGE [DAY-2]

## 2. KBC
Congratulations on the completion of first day.

On Day 2 We Create Kaun Banega Crorepati in Python. In the prgram first welcome the participant after that computer show the question with the reward price if participant answer correctly then game continues otherwise he/she lose all the winning.

### Require Topics :

- [Python Lists](https://www.w3schools.com/python/python_lists.asp) 
- [For Loop Python](https://www.w3schools.com/python/python_for_loops.asp)
- [range() Function](https://www.w3schools.com/python/gloss_python_for_range.asp)
- [List Indexing](https://www.geeksforgeeks.org/python-list-index/)
- [Python Break Statement](https://www.w3schools.com/python/ref_keyword_break.asp)

so here we go...

**Steps :**

- [Basic Participant Login](#--basic-participant-login)
- [Store Data](#--store-data)
- [Start The Game](#--start-the-game)
- [Right Answer](#--right-answer)
- [Loose the Game](#--loose-the-game)
- [Output](#output)
          

### - Basic Participant Login

```python
participant = input('Enter Your Name: ')
print(f"! Hello {participant}, Welcome To KBC !".center(100, "."))
```

>Note : `print('''Multiline string''')` is used for multiline string

### - Store Data
After that the questions, options and answers store differently in different variables using python [lists](https://www.w3schools.com/python/python_lists.asp)

For EX.
```python
questions = [
    "What is Capial of india?",
    "Who is amitabh bachhan?"
]
```
  

### - Start The Game
Now we start code for the game with help of [For Loop](https://www.w3schools.com/python/python_for_loops.asp) in Python.

```python
for que in range(len(que_list)):
    #displaying the Question
    #displaying the Option
    #Ask for Answer

    #check the answer
```

* Here we use [For Loop](https://www.w3schools.com/python/python_for_loops.asp) with his [range( )](https://www.w3schools.com/python/gloss_python_for_range.asp) function to set the range when game is terminated

* In the loop we need to diplay question, options every time and also ask user for the right answer and at the end of loop we need to verify that answer and provide result to the user
  
* Here [List Indexing](https://www.geeksforgeeks.org/python-list-index/) also used to iterate each queation from `Questions list` and options from the `Option list`
  
### - Right Answer


```python
for que in range(len(que_list)):
    #displaying the Question
    #displaying the Option
    #Ask for Answer

    #check the answer
    if(Answer is correct):
        #win
    else:
        #loose
        break
```
If participant give right answer that simply display the winning reward for it and moving to the next question and one after the other for loop will go on like this untill participant's wrong answer or completion of loop.

### - Loose the Game
If participant loose the game we simply break the loop using [Loop Break Statement](https://www.w3schools.com/python/ref_keyword_break.asp) to terminated the loop in the middle of iteration
  
>Note : At the end of game we also need to clearify that if user give all answer correctly then game must be terminated automatically by congratulating the winner with the ending of the questions.

```python
 if(Answer is correct):
        if(Question is last_question):
            #You win the whole game
        
        #right answer
        reward = reward*2
    else:
        #loose
        break
```


##  output  
Welcome :  
![image](/img/level2_output/welcome.png) 

Right Answer :  
![image](/img/level2_output/right.png) 

Wrong Answer :  
![image](/img/level2_output/wrong.png) 

Winner :  
![image](/img/level2_output/winner.png) 


<br>

###### END


> See You In Level 3 👀....

