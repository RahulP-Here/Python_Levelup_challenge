''' EXERCISE - 4 : SECRET CODE LANGUAGE '''

import random

#ENCRYPT & DECRYPT EACH WORD
def convertWord(word, encrypt):

    #If word contains LESS then 3 character
    if len(word)<3:

        #Swape chars
        new_word = word[::-1]
        # return new_word

    #If word contains MORE then 3 character
    else:

        #Encryption
        if encrypt == True:

            #Random Chars
            more = "abcdefghijklmnopqrstuvwxyz1234567890"

            #Generate 3 char's random word
            start = "".join(random.choices(more, k=3)) #to put at the start of a word
            end = "".join(random.choices(more, k=3)) #to put at the end of a word

            #Encrypted word
            new_word = start + word[1:] + word[0] + end

        #Decryption
        else:

            #Decrypted word
            new_word = word[len(word)-4] + word[3:(len(word)-4)]   

    return new_word
#-----------------------------------------------

#Encrypt / Decrypt Sentence
def en_De_Sentance(sentence, encrypt):

    #devide sentence into word
    sentence_list = sentence.split(" ")

    for i in sentence_list:
        index = sentence_list.index(i)

        #En/De-crypt every word 
        sentence_list[index] = convertWord(i, encrypt)
    
    #join words into sentence
    new_sentence = " ".join(sentence_list)
    return new_sentence 
#-----------------------------------------------

#MAIN PROGRAM 
def main():
    print("! Welcome To Code/Decode !".center(100, "."))

    while True:
        print("\n")
        ed = input("Enter (E for encryption) & (D for decryption) or (q for quit): ")

        if ed.lower() == "d":
            encrypt = False

        elif ed.lower() == "e":
            encrypt = True
            

        elif ed.lower() == "q":
            print("Program closed successfully!")
            break
        
        else:
            print("Invalid Input: plz enter only q,e or d!")
            continue

        user_input = input("Enter you Meassager here: ")
        output = en_De_Sentance(user_input, encrypt)
        print(f"---> {output}")

    print("! Thank You !".center(100, "."))

main()    



    






