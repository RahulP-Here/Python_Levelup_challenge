[Scroll Down](#end)

# PYTHON : 10 DAYS LEVEL-UP CHALLENGE [DAY-9]

## 9. News Application !

Congratulations!.. We're close to complete this challange

Welcome to Day 9 of the `Python 10 Days Level-Up Challenge`! Today, we have created a simple `News Application` that allows users to explore news articles based on a specified field. 
The application fetches news data from the [NewsAPI](https://newsapi.org/) and provides an interactive dashboard for users.


#### Required Modules:
- [sys](https://docs.python.org/3/library/sys.html)
- [os](https://docs.python.org/3/library/os.html)
- [requests](https://docs.python-requests.org/en/latest/)
- [random](https://docs.python.org/3/library/random.html)
- [termcolor](https://pypi.org/project/termcolor/)
- [FolderClass](/Level_8/FolderClass.py) (Custom Module)

#### API Used:
- [NewsAPI](https://newsapi.org/)

Let's delve into the details...


<br>

---

**Steps :**

- [Import Modules](#1-import-modules)
- [Create Load Function](#2-load-news-articles)
- [Get Your Api Key](#3-get-your-api-key)
- [Set Application Dashboard](#4-application-dashboard)
- [Execute User Commands](#5-execute-user-commands)

---

- [Logic template](#logic-template)
- [Output](#output)

---

<br>

- ### 1. Import Modules
    Import the necessary modules, including requests, random, and termcolor.

    ```python
    import sys
    import os

    # Add the parent directory to sys.path (change directory in runtime)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

    import requests
    import random
    from termcolor import colored
    from Level_8.FolderClass import loading
    ```


* [Python Request Module](https://docs.python-requests.org/en/latest/) allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data.

* [Python Random Module](https://docs.python.org/3/library/random.html) defines a series of functions for generating or manipulating random integers.

> Additional Note: Ensure the `FolderClass.py` module is available in the specified path.

* [Python sys Module](https://docs.python.org/3/library/sys.html) provides information about constants, functions and methods of the Python interpreter.

* [Python OS Module](https://docs.python.org/3/library/os.html) interacting with the operating system, like creating files and directories, management of files and directories, input, output, environment variables, process management, etc.
---

- ### 2. Load News Articles
    Define a function `load(Q)` to load news articles based on the provided query (`Q`) using the NewsAPI.

    ```python
    def load(Q):
        # Implementation of the load function...

        #Send get request to API    
        url = ('https://newsapi.org/v2/everything?q={Q}&apiKey=c{Your Api key}') #use your own api key
        response = requests.get(url)
        
        loading(4) #loading function of folderclass

        data = (response.json()) #return as a dict
        articles = data['articles']

        #Print the Articles
    ```

> Note:  Remember to customize the API key in the URL for the NewsAPI. Use Your own `Api key` from the [NewsAPI](https://newsapi.org/) 

---
### 3. `Get Your Api Key`
- __Open Website :__ [NewsAPI](https://newsapi.org/)

    ![img](/img/Level9_output/api%20key/webiste.png)
- __Register Yourself :__ 

    ![img](/img/Level9_output/api%20key/register.png)
- __Api Key :__ 

    ![img](/img/Level9_output/api%20key/got%20api.png)


### 4. Application Dashboard

Create an interactive dashboard for the News Application. Allow users to input a field for news, load initial news articles, and provide options to change the field, load more news, or quit.

```python
    # Implementation of the application dashboard...
    '''
    Ask User to input the Query [which feild news he want get]
    '''
    #pass query into load function
    load(query)
```

---

### 5. Execute User Commands

Execute user commands based on their input in the dashboard. Use while loop for repetedly execution of dashboard.

```python
    while True:
       user=input(colored("Enter :- \n1 for change feild \n2 for load more news in same feild \n0 for quite \n", 'blue'))

        # User command execution...
```
__`User Commands`__ :
- i.   Exit Application
- ii.  Load More Article 
- iii. Change Field
---

<br>

##  Logic Template
```python
    import sys
    import os

    # Add the parent directory to sys.path (change directory in runtime)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

    import requests
    import random
    from termcolor import colored
    from Level_8.FolderClass import loading

    #LOAD NEWS ARTICLES
    def load(Q):
        # Implementation of the load function...

        #Send get request to API    
        url = ('https://newsapi.org/v2/everything?q={Q}&apiKey=c{Your Api key}') #use your own api key
        response = requests.get(url)
        
        loading(4) #loading function of folderclass

        data = (response.json()) #return as a dict
        articles = data['articles']

        #Print the Articles

    # Implementation of the application dashboard...
    '''
    Ask User to input the Query [which feild news he want get]
    '''
    #pass query into load function
    load(query)

    while True:
       user=input(colored("Enter :- \n1 for change feild \n2 for load more news in same feild \n0 for quite \n", 'blue'))

        # User command execution...
```

---

##  Output  
#### Enter Feild :  
![image](/img/Level9_output/News%20feild.png) 

#### Response :  
![image](/img/Level9_output/output.png) 

#### Chane the feild :  
![image](/img/Level9_output/change%20feild.png) 

#### Exit App :  
![image](/img/Level9_output/quit.png) 

<br>

---


[Exercise 9](exe9.py)

###### END


> See You In Level 10 👀....

