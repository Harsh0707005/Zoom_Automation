from datetime import datetime
import time
import webbrowser as wb
import pyautogui as pag


while True: #running the loop until the scheduled time

    today_date = datetime.now() #getting the system's date and time
    Time = today_date.strftime("%I:%M:%S %p")

    f = open("Links.txt") #opening and accessing links of the meetings
    Links_Pass = f.readlines()

    '''
    You can add code for more meetings using the code as below with elif statement and time for the meeting.
    NOTE: Remember to add the links of the meetings in the links.txt file.
    '''

    if Time == "07:59:30 AM": #time for the first meeting
        # Change the time and name according to your need
        print("Initializing Computer Class...")
        Computer = Links_Pass[0]
        
        wb.open(Computer)
        print("Computer Class Initialized Successfully !")
        time.sleep(2000)

    elif Time == "08:36:00 AM":#time for the second meeting
        # Change the time and name according to your need
        print("Initializing English Class...")
        English = Links_Pass[1]
        
        wb.open(English)
        print("English Class Initialized Successfully !")

        time.sleep(2000)

    elif Time == "9:10:00 AM":#time for the third meeting
        # Change the time and name according to your need
        print("Initializing Chemistry Class...")

        Chemistry = Links_Pass[2]

        wb.open(Chemistry)
        print("Chemistry Class Initialized Successfully !")
        time.sleep(2280)

    elif Time == "09:51:00 AM":#time for the fourth meeting
        # Change the time and name according to your need
        print("Initializing Physics Class...")
        Physics = Links_Pass[3]


        wb.open(Physics)
        print("Physics Class Initialized Successfully !")
        time.sleep(2000)

    elif Time == "10:26:00 PM AM":#time for the last meeting
        # Change the time and name according to your need
        print("Initializing Maths Class...")
        Maths = Links_Pass[4]
        
        wb.open(Maths)
        print("Maths Class Initialized Successfully !")
        quit
    
    else:
        pass
