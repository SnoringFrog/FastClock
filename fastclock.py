import datetime
import random
import threading

MAXOFFSET=600 #in seconds, should eventually read from .fastclockrc

#Internal functions
def changeOffset():
    t = threading.Timer(30, changeOffset)
    t.daemon = True
    global offset
    offset = random.randint(0, MAXOFFSET)
    
    t.start()

def update():
    t = threading.Timer(1.0, update)
    t.daemon = True
    
    current_time = datetime.datetime.now()
    global displayed_time
    displayed_time = current_time + datetime.timedelta(0, offset)
    
    #print(displayed_time.time().strftime("%I:%M"))
    t.start()

#External interfaces
def start(): #start FastClock
    changeOffset()
    update()

#Get current FastClock time object  
def getTime():
    global displayed_time
    return displayed_time.time()

#Get current FastClock time in human-readable format
def getReadableTime():
    global displayed_time
    return displayed_time.time().strftime("%I:%M")
