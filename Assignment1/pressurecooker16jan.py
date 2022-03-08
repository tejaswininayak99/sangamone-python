import time
import datetime

def timer(m,s):
    t_sec = m * 60 + s

    while t_sec > 0:
    #to analyize when the timer reaches 0
        t = datetime.timedelta(seconds = t_sec)
        #timedelta tells the diff btwn two time
        print(t, end="\n")

        time.sleep(1)
        #sleeps delays the program
        t_sec -= 1
        
m = input("Enter the minutes:\n")
s = input("Enter the seconds:\n")
timer(int(m), int(s))
from playsound import playsound
playsound('https://github.com/tejaswininayak99/sangamone-python/blob/25b197c1cffaa0b6cb5ffd2d7b4b3ffab14a9bc4/Assignment1/beep.mp3')
print("\n MoM turn off the cooker")


        
    
        
    
    
