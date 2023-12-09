[Scroll Down](#end)

# PYTHON : 10 DAYS LEVEL-UP CHALLANGE [DAY-4]

## 4. SECRET CODE LANGAUGE
Congratulations on the completion of Third Day.

On Day 4 We'll Create a `Screat Code Laguage Converter` in Python. In this Program we create a Dashboard in terminal which take a string as a input and Encrypt / Decrypt it in Secreat Code / Normal Langauge.

- #### Rules For Convert a Word into a Secret Code `{Encryption}`:
 
    - 1.&nbsp;&nbsp;&nbsp; If word has 2 or less then 2 characters then swap it.  
    `ex. is --> si`

    - 2.&nbsp;&nbsp;&nbsp; If word has more than 2 characters then swipe first character of word into last and add 3 random character word at start and at end of the word.    
    `ex. John --> ohnJ --> xyzohnJabc`

- #### Rules For Convert a Secret code into Normal Word `{Decryption} :`
 
    - 1.&nbsp;&nbsp;&nbsp; If word has 2 or less then 2 characters then swap it.  
    `ex. si = is`

    - 2.&nbsp;&nbsp;&nbsp; If word has more than 2 characters then remove first and last three character after swipe last character at start.      
    `ex. xyzohnJabc --> ohnJ --> John`


#### Require Topics :
- [Functions in Python](https://www.w3schools.com/python/python_functions.asp)
- [Python random module](https://www.w3schools.com/python/module_random.asp)  
- [Index Slicing](https://www.geeksforgeeks.org/how-to-index-and-slice-strings-in-python/)  
- [String Concatenation](https://www.w3schools.com/python/gloss_python_string_concatenation.asp)
- [Break  & Continue](https://www.geeksforgeeks.org/break-continue-and-pass-in-python/)

so here we go...

<br>

---

**Steps :**

- [Basic Structure](#--basic-structure)
- [Word Converter](#--word-converter)
- [Sentence Converter](#--sentence-converter)
- [Main Function](#--main-function)
- [Output](#output)

---          
- [Logic Template](#logic-template)
---

### - Basic Structure

Here, we need to convert each word of sentance into secreat language. For that we need to declare 3 [Functions](https://www.w3schools.com/python/python_functions.asp)..

- 1. [Functions](#--word-converter) that En/De-crypt Each word into Secret/Normal langauge.
    - `def convertWord(word) :`

- 2. [Functions](#--sentence-converter) That Break Sentance into Words & Reverse it with Converted Words. 
    - `def en_De_Sentance(sentence) :`

- 3. [Functions](#--main-function) That include `main` Converter Dashboard for user ineraction and input. 
    - `def main()`


```python
    def convertWord(word, encrypt):
        new_word = #Encrypt / Decrypt the word
    return new_word
    
   def en_De_Sentance(sentence, encrypt) :
    #devide sentence into word

    #convert each word
    convertWord(word, encrypt)

    ##join converted words into sentence

    def main():
        #user dashboard
    
    main()
```

> Note : Here the Argument in function called `encrypt` is either True or False, That indicates that the senteance need to encrypt or decrypt

---

<br>

### - Word Converter
For Converting the word , we need to identify the length of word with the help of [len()](https://www.w3schools.com/python/ref_func_len.asp)


```python
    if len(word)<3:
        #Swap chars
    else:
        #Encrypt or Decrypt it based on rule as per demand
```
> [len()](https://www.w3schools.com/python/ref_func_len.asp) is used to find length of variables like String, List.

we need to define that which type of convertion `[Encryption / Decryption]` user want to perform on the sentence.

```python
    if len(word)<3:
        new_word = #Swap chars

    else:
        #Encrypt or Decrypt it based on rule as per demand

        #Encryption
        if encrypt == True:
            new_word = #encrypt it according to encryption rules

        #Decryption
        else:
            new_word = #decrypt it according to decryption rules

    return new_word
```
> Note : we need to pass `True` in argument value of `encryption` if user want to encrypt else pass `False`. 

> - For Encryption Use : <br>
        - [Python random](https://www.w3schools.com/python/module_random.asp) : `for random chars `  
        - [Index Slicing](https://www.geeksforgeeks.org/how-to-index-and-slice-strings-in-python/)  
        - [String Concatenation](https://www.w3schools.com/python/gloss_python_string_concatenation.asp)
>       
> - For Decryption Use : <br>
        - [Index Slicing](https://www.geeksforgeeks.org/how-to-index-and-slice-strings-in-python/)

---

<br>
     
### - Sentence Converter
Now we start code for the Sentence Converter. 

First we need to Break whole String Words with help of `[String.split()](https://www.w3schools.com/python/ref_string_split.asp)` method pass each word in the argument of [convertWord()](#word-converter). 

At last we concatinate all new words returned from the [convertWord()](#word-converter) and create whole sentence which is Encrypted/Decrypted.

```python
    def en_De_Sentance(sentence, encrypt):
       #devide sentence into word

       for i in word_list:
        #En/De-crypt every word
    
       new_sentence = #Join words into sentences

    return new_sentence
```

* Here we should use [For Loop](https://www.w3schools.com/python/python_for_loops.asp) for pass each word in the function [convertWord()](#word-converter).

---

<br>
       
### - Main Function

In main Function we welcome the user then ask him/her for input that include the choice of `encryption / decryption / quit` and the sentense.

* After that pass the sentence and the choice in the [en_De_Sentance()](#sentence-converter).

```python
    def main():
        #User Dashboard

        while True:
            #ask For user's choice encryption / decryption / quit

            if user == 'encyption' :
                encrypt = True

            elif user == 'decyptio'n:
                encrypt = False
                

            elif user == 'Quit':
                #Close Program
                break
            
            else:
                #for Invalid Input
                continue

            user_input = input("User Sentence")
            output = en_De_Sentance(user_input, encrypt)

            print(f"---> {output}")

        print("! Thank You !".center(100, "."))

```
* we use [While](https://www.geeksforgeeks.org/python-while-loop/) to keep dashboard open.
> Note : Here we use [Break](https://www.geeksforgeeks.org/python-break-statement/) statement for Break the loop when user want to quit and [Continue](https://www.geeksforgeeks.org/python-continue-statement/) for skip the iteration when user enter invalid input.

---

<br>
     
##  Logic Template
```python
    def convertWord(word, encrypt):
        if len(word)<3:
            new_word = #Swap chars

        else:
            #Encrypt or Decrypt it based on rule as per demand

            #Encryption
            if encrypt == True:
                new_word = #encrypt it according to encryption rules

            #Decryption
            else:
                new_word = #decrypt it according to decryption rules

    return new_word
    
   def en_De_Sentance(sentence, encrypt):
       #devide sentence into word

       for i in word_list:
        #En/De-crypt every word
    
       new_sentence = #Join words into sentences

    return new_sentence

    def main():
        #User Dashboard

        while True:
            #ask For user's choice encryption / decryption / quit

            if user == 'encyption' :
                encrypt = True

            elif user == 'decyptio'n:
                encrypt = False
                

            elif user == 'Quit':
                #Close Program
                break
            
            else:
                #for Invalid Input
                continue

            user_input = input("User Sentence")
            output = en_De_Sentance(user_input, encrypt)

            print(f"---> {output}")

        print("! Thank You !".center(100, "."))
    
    main()
```

---

<br>
     
##  output  
Output uploaded soon....

<br>

###### END


> See You In Level 5 👀....
