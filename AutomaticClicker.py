import pyautogui, sys, time
from datetime import datetime
from threading import Timer

mousePosition = pyautogui.position()

startMessage = """
  ___        _                        _           _ _____ _ _      _             
 / _ \      | |                      | |         | /  __ \ (_)    | |            
/ /_\ \_   _| |_ ___  _ __ ___   __ _| |_ ___  __| | /  \/ |_  ___| | _____ _ __ 
|  _  | | | | __/ _ \| '_ ` _ \ / _` | __/ _ \/ _` | |   | | |/ __| |/ / _ \ '__|
| | | | |_| | || (_) | | | | | | (_| | ||  __/ (_| | \__/\ | | (__|   <  __/ |   
\_| |_/\__,_|\__\___/|_| |_| |_|\__,_|\__\___|\__,_|\____/_|_|\___|_|\_\___|_|   
                                                                                 
"""

print(startMessage)
# print("Current Mouse Position: " + str(pyautogui.position()))
print("Available modes: (Type one of the digits below [1 or 2] to select a mode)")
print("1) Single scheduled click")
print("2) Beat the clock - be the first one to click on something at a certain time")
clickMode = input()

def clickNow():
    pyautogui.moveTo(mousePosition)
    print("Time of clicking is between \t" + str(datetime.today()))
    pyautogui.click()
    print("and \t\t\t\t" + str(datetime.today()))

def testingMode(nextClick):
    while nextClick == "\'":
        print("Testing Mouse Position: " + str(pyautogui.position()))
        nextClick = input()

def await_and_click(inputHour, inputMinute, inputSecond = 0, inputMicrosecond = 0):

    print("Move your mouse to the place you would like to click at, then press 'y'")
    success = input()
    global mousePosition
    mousePosition = pyautogui.position()
    while success != "y":
        print("Move your mouse to the place you would like to click at, then press 'y'")
        success = input()
        mousePosition = pyautogui.position()
    print("You've selected the mouse position: " + str(pyautogui.position()))
    time.sleep(2)
    print("Moving to location: ")
    pyautogui.moveTo(mousePosition)
    x=datetime.today()
    y=x.replace(hour=inputHour, minute=inputMinute, second=inputSecond, microsecond=inputMicrosecond)
    print("Current Time is: " + str(x))
    print("Time it will click at is approximately: " + str(y))
    print("Time remaining is: " + str(y-x))
    delta_t=y-x

    secs=delta_t.seconds+1
    t = Timer(secs, clickNow)
    t.start()

def checkValidTime(hour,minute):
    if (hour < 1 or hour > 24):
        print ("Invalid hour specified, must be between 1 and 24")
        quit()
    if (minute < 0 or minute > 59):
        print ("Invalid minute specified, must be between 0 and 60")
        quit()
    return

print("Select a time to click at using the 24-hour format (ex 11:23 is 11:23 AM, or 17:59 is 5:59PM)")
timeString = input()
timeArray = timeString.split(":")
selectedHour = int(timeArray[0])
selectedMinute = int(timeArray[1])
checkValidTime(selectedHour,selectedMinute)
print("You've selected the time: " + str(selectedHour) + ":" + str(selectedMinute))

if clickMode == "1":
    await_and_click(selectedHour, selectedMinute, 0, 0)

if clickMode == "2":
    await_and_click(selectedHour, selectedMinute - 1, 59, 909999)




