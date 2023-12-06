''' EXERCISE - 2 : KBC [Kaun Banega Crorepati]'''


#BASIC PARTICIPANT LOGIN 
participant = input('Enter Your Name: ')
print(f"! Hello {participant}, Welcome To KBC !".center(100, "."))

print('''RULES:
      1. ans in only a, b, c or d
      2. do not use any keyword instead of a, b, c, d
      3. if you win the game you win the price otherwise you loose the all money''')

#STORE DATA 
#Question:
questions = [
    "What is Capial of india?",
    "Who is amitabh bachhan?",
    "What is full form of IT?",
    "How many states in india?"
]

#Options
options = [
    ["india", "delhi", "gujrat", "kashmir"],
    ["athelte", "singer", "actor", "cricketer"],
    ["information technology", "induas tech", "itech", "international tred"],
    ["5", "10", "24", "28"]
]

#Labels
label = ["A", "B", "C", "D"]

#Answers
answers = ["B", "C", "A", "D"]

#Set Starting reward
reward = 25000

#START THE GAME
for i in range (len(questions)):

    #Displaying Questions
    print(f"{reward} \u20B9 ke liye sawaal aapki computer screen pr".center(100, "."))
    print(f"Q.{i+1}.", questions[i].title())
    
    #Displaying Options
    for option in options[i]:
        print(label[options[i].index(option)], option.upper(), sep=". ")
        
    #Ask For Input
    Ans = input("Answer: ").upper()

    #Verifying the Answer
    if(Ans == answers[i]):
        print("! Sahi Jawab !")
        if (i == (len(questions)-1)):
            print("CONGRATULATONS AAP JIT CHUKE HAI 200000 \u20B9".center(100, "."))
            print("! KBC me bhag lene k liye dhanyawad !".center(100))
        else:
            print(f"CONGRATULATONS AAP JIT CHUKE HAI {reward} \u20B9".center(100, "."))
            reward = reward*2
    else:

        print("! Galat Jawab ! ")
        print("! Aap apni rashi haar chuke hai ! ")
        break

    print("") #for line break b/w two questions.





