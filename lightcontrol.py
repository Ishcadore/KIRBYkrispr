import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = 05 #Pin 29
RELAIS_2_GPIO = 06
#GROUND @ PIN 30

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on

GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # out
GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # on


# import date and time modules
import datetime
import time
 
# Enter the times you want the appliance to turn on and off for
# each day of the week.
 
MonAMOn  = datetime.time(hour=1)
MonAMOff = datetime.time(hour=2)
MonPMOn  = datetime.time(hour=13)
MonPMOff = datetime.time(hour=14)
TueAMOn  = datetime.time(hour=1)
TueAMOff = datetime.time(hour=2)
TuePMOn  = datetime.time(hour=13)
TuePMOff = datetime.time(hour=14)
WedAMOn  = datetime.time(hour=1)
WedAMOff = datetime.time(hour=2)
WedPMOn  = datetime.time(hour=13)
WedPMOff = datetime.time(hour=14)
ThuAMOn  = datetime.time(hour=1)
ThuAMOff = datetime.time(hour=2)
ThuPMOn  = datetime.time(hour=13)
ThuPMOff = datetime.time(hour=14)
FriAMOn  = datetime.time(hour=1)
FriAMOff = datetime.time(hour=2)
FriPMOn  = datetime.time(hour=13)
FriPMOff = datetime.time(hour=14)
SatAMOn  = datetime.time(hour=1)
SatAMOff = datetime.time(hour=2)
SatPMOn  = datetime.time(hour=13)
SatPMOff = datetime.time(hour=14)
SunAMOn  = datetime.time(hour=1)
SunAMOff = datetime.time(hour=2)
SunPMOn  = datetime.time(hour=13)
SunPMOff = datetime.time(hour=13)
 
# Store these times in an array for easy access later.
OnTimeAM = [MonAMOn, TueAMOn, WedAMOn, ThuAMOn, FriAMOn, SatAMOn, SunPMOn]
OnTimePM = [MonPMOn, TuePMOn, WedPMOn, ThuPMOn, FriPMOn, SatPMOn, SunPMOn]
OffTimeAM = [MonAMOff, TueAMOff, WedAMOff, ThuAMOff, FriAMOff, SatAMOff, SunAMOff]
OffTimePM = [MonPMOff, TuePMOff, WedPMOff, ThuPMOff, FriPMOff, SatPMOff, SunAMOff]
 
 
# Start the loop that will run until you stop the program or turn off your Raspberry Pi.
 
while True:
    global state
    state = 1
    if state == 1:
        time.sleep(0.5)
        GPIO.output(RELAIS_1_GPIO, True)
        GPIO.output(RELAIS_2_GPIO, True)
        time.sleep(3600) #3600
        state = 0
        GPIO.output(RELAIS_1_GPIO4, False)
        GPIO.output(RELAIS_1_GPIO, False)
 
 
 
    # get the current time in hours, minutes and seconds
    currTime = datetime.datetime.now()
    #print(currTime)
    # get the current day of the week (0=Monday, 1=Tuesday, 2=Wednesday...)
    currDay = datetime.date.today().weekday()
 
    #Check to see if it's time to run the appliance for the AM hours
    while (currTime.hour >= OnTimeAM[currDay].hour and currTime.hour <= OffTimeAM[currDay].hour): 
    # set the GPIO pin to HIGH GPIO.output(24, True) GPIO.output(27, True) time.sleep(60) currTime = datetime.datetime.now() currDay = datetime.date.today().weekday() else: if (currTime.hour &gt;= OffTimeAM[currDay].hour - 1):
            GPIO.output(RELAIS_1_GPIO, True)
            GPIO.output(RELAIS_2_GPIO, True)
            time.sleep(60) 
            currDay = datetime.date.today().weekday() 
            currTime = datetime.datetime.now() 
            GPIO.output(RELAIS_1_GPIO, False)
            GPIO.output(RELAIS_2_GPIO, False)            
 
 
    #Check to see if it's time to run the appliance for the PM hours
    while (currTime.hour >= OnTimePM[currDay].hour and currTime.hour <= OffTimePM[currDay].hour): 
        GPIO.output(RELAIS_1_GPIO, True) 
        GPIO.output(RELAIS_2_GPIO, True) 
        time.sleep(60) 
        currDay = datetime.date.today().weekday() 
        currTime = datetime.datetime.now() 
        if (currTime.hour >= OffTimePM[currDay].hour - 1):
            GPIO.output(RELAIS_1_GPIO, False)
            GPIO.output(RELAIS_2_GPIO, False)