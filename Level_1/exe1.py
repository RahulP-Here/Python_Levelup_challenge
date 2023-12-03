''' EXERCISE - 1 : WELCOME TO THE CHALLANGE '''

import time
realTime = int(time.strftime('%H'))

#Welcome User
user = input("Enter Your Name: ")

if(realTime<12):
    print("Good Morning", user, end=". ")

elif(realTime<16):
    print("Good Afternoon", user, end=". ")

elif(realTime<20):
    print("Good Evening", user, end=". ")
      
else:
    print("Good Night", user, end=". ")

print("Welcome To The 10 Days Python Level-Up Challange.")
