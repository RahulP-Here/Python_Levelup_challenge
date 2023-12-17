''' EXERCISE - 5 : KEEP YOUR EYES COOL !'''

#import modules
from plyer import notification  
import time
  
# set title & msg
Title = 'GREETINGS FROM YOUR HEALTH!'  
Msg = 'Keep Your Eyes Cool & Calm, via 5 min Break. \nThank you for reading. Have a Good Day.'  

#set notification
while(True):
    time.sleep(60*60)
    notification.notify(  
        title = Title,  
        message = Msg,  
        app_icon = None,  
        timeout = 10,  
        toast = False  
    )  

# Run as Exe -->  pythonw .\Exercise\ex11.py  

# for stop this go in task manager --> backround process --> end python related execution which run in backgound.