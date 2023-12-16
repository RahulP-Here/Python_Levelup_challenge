[Scroll Down](#end)

# PYTHON : 10 DAYS LEVEL-UP CHALLANGE [DAY-5]

## 4. KEEP YOUR EYES COOL !
Congratulations!.. We're reached half of this challange.

On day 5 we will create `Eye Health Notifier` for pregrammers like us. In this program we create a notifier that will notify the programmer to take a break to rest the eyes. This notifier usually alerts to rest for 5 minutes, in every 1 hour.

<!-- --- -->
[while loop]:https://www.w3schools.com/python/python_while_loops.asp

[plyer module]:https://www.geeksforgeeks.org/python-desktop-notifier-using-plyer-module/ 

[time module]:https://docs.python.org/3/library/time.html
<!-- --- -->

#### Require Topics :
- [While Loop in Python][while loop]
- [Python plyer module][plyer module]  
- [Python time module][time module]  

so here we go...

<br>

---

**Steps :**

- [Import Modules](#--import-modules)
- [Set Title & Message](#--set-title--message)
- [Set Notification](#--set-notification)
- [Run as exe](#--run-as-exe)
- [Output](#output)
- [Stop the exe](#stop-the-exe)

---          

<br>

### - Import Modules

First, we need to import [Time Module](https://docs.python.org/3/library/time.html) and [Plyer Module](https://www.geeksforgeeks.org/python-desktop-notifier-using-plyer-module/).

```python
    from plyer import notification  
    import time
```
* Here we only import a specific [Python Class](https://docs.python.org/3/tutorial/classes.html) from whole [Plyer Module][plyer module]. 

<br>

> [Time Module][time module] : Provides many ways of representing time in code, such as objects, numbers, and string
>
> [Plyer Module][plyer module] : Provide Notification tool in python for desktop

---

<br>

### - Set Title & Message
We ser basic variables, named `Title` & `Msg` which include the string data to show in the notification.

```python    
Title = 'GREETINGS FROM YOUR HEALTH!'  
Msg = 'Keep Your Eyes Cool & Calm, via 5 min Break. \nThank you for reading. Have a Good Day.'
```

---

<br>
     
### - Set Notification
Now we set our notification with the help of [notification.notify()](https://python.plainenglish.io/how-to-send-desktop-notifications-with-python-62a738850fbf) method of notification class in `plyer`. 

```python
    while(True):

        time.sleep(60*60)

        notification.notify(  
            title = Title,  
            message = Msg,  
            app_icon = None,  
            timeout = 10,  
            toast = False  
        ) 
```
* For continuous notifications, we use [while loop](https://www.w3schools.com/python/python_while_loops.asp) with `infinite iteration`.

* after that we set `Msg` & ` Title` in [notification.notify()](https://python.plainenglish.io/how-to-send-desktop-notifications-with-python-62a738850fbf).

> Note : For more information about `notification.notify()` [Click here](https://python.plainenglish.io/how-to-send-desktop-notifications-with-python-62a738850fbf). 

![image](/img/level5_output/notification_notify.png)

---

<br>
       
### - Run as exe

> Warning : For verifying that program has not any error, run this as normal python file Before Run this as an exe   

`We need to run this file as exe instead of normal python file.` 

* To run this file as exe in background run this command in terminal:

```
    pythonw .\Level_5\exe5.py
```
![run exe](/img/level5_output/command.png)

* After run this file as an exe it run in the background without interrupt any other operation just like normal exe. and after 1 hour it will send notification and will continuously sending notification after gap of 1 hour.

> Note : For Find the output immediate keep `time.sleep()` for some minor second like. 
```
time.sleep(10)
``` 

---

<br>
     
##  Stop the exe 

Once the exe file being run, it will continuously run repetedly in background.

* `To Stop It :`
    - make while loop finite
```python
    i = True
    while(i == True):

        time.sleep(60*60)

        notification.notify(  
            title = Title,  
            message = Msg,  
            app_icon = None,  
            timeout = 10,  
            toast = False  
        )
        i = False
```

* `or`
    - Stop it from `start --> task manager --> processes --> vs code --> python --> end task`

<br>

`start --> task manager`
![Stop exe](/img/level5_output/stop_1.png)

<br>

`task manager --> processes --> vs code --> python --> end task`
![Stop exe](/img/level5_output/stop.png)

---

<br>
     
##  output  
Output uploaded soon.... 

<br>

###### END


> See You In Level 5 👀....
