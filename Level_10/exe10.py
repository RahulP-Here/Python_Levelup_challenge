''' EXERCISE - 10 : ! Congratulate Youself !'''

#Install pywin32 
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

#Input Your name
name = "Rahul Prajapati"
sentance = "Congratulations" + name + "You Successfully completed PYTHON LEVELUP CHALLANGE."

speak.Speak(sentance)
