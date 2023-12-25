''' EXERCISE - 8 : ! NEWS APPLICATION !'''

import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

import requests 
import random
from termcolor import colored
from Level_8.FolderClass import loading

#LOAD NEWS ARTICLES
def load(Q):
    #Send get request to API    
    url = ('https://newsapi.org/v2/everything?q={Q}&apiKey=cdeda5db204c43d8803ef3c4e1115090')
    response = requests.get(url)
    
    loading(4)

    data = (response.json()) #return as a dict

    articles = data['articles']       

    #Print Articles
    for j in range(5):
        i = random.randint(0, len(articles)-1)

        print("\n----->")
        print(colored(((articles[i])['title']).center(100, "."), 'yellow'))
        print((articles[i])['description'])


#APPLICATION DASHBOARD
print(" WELCOME TO NEWSICA.COM ".center(100, "-"))
print("")

Query = input("Enter Feild which News You wann see? :")
load(Query)

while (True):
       print("")
       user=input(colored("Enter :- \n1 for change feild \n2 for load more news in same feild \n0 for quite \n", 'blue'))
       if (user == "0"):
              break
       elif(user == "1"):
              Query = input("Enter Feild which News You wann see? :")
              load(Query)
       elif(user == "2"):
              load(Query)
       else:
              print("PLz Enter valid input")
              
print(" THANK YOU FOR VISITING NEWSICA.COM ".center(100, "-"))






