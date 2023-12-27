[Scroll Down](#end)

# PYTHON : 10 DAYS LEVEL-UP CHALLENGE [DAY-10]

## 10. Congratulate Yourself ! 

Welcome to Day 10, the final day of the Python 10 Days Level-Up Challenge! As a celebration of your achievements throughout this challenge, we have a special program for you. The "Congratulate Yourself" program utilizes the `pywin32` library to make your computer congratulate you!

Let's explore the details...

#### Required Module:
- [pywin32](https://pypi.org/project/pywin32/)

> #### Additional Note:
> - Make sure to install the `pywin32` library using the command `pip install pywin32`.
>
> ![pywin32](/img/Level10_output/pywin32.png)


---

### Program Overview

The "Congratulate Yourself" program is a fun way to acknowledge your successful completion of the Python Level-Up Challenge. The program uses the `win32com` module to access the Windows Speech API (SAPI) and speak out a congratulatory message.

---

### Code Implementation

```python
# Install pywin32 
import win32com.client as wincom

# Create a SAPI.SpVoice object
speak = wincom.Dispatch("SAPI.SpVoice")

# Input Your name
name = "Rahul Prajapati"
sentence = "Congratulations " + name + "! You have successfully completed the PYTHON LEVEL-UP CHALLENGE."

# Make the computer speak the congratulatory message
speak.Speak(sentence)
```

### Customization:

Modify the name variable with your own name.

>### Additional Information:
> - The [pywin32](https://pypi.org/project/pywin32/) library provides access to many Windows APIs, and in this case, it is used to interact with the Windows Speech API for text-to-speech functionality.
>
>- The program congratulates you and acknowledges your successful completion of the Python Level-Up Challenge.

---

Code : 
[Exercise 10](exe10.py)

<br>


###### END

> Congratulations and  Happy coding! 💻....