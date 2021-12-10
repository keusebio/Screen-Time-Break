from plyer import notification
import threading
from threading import *
import time
import os
import platform
import random


# notification method, displays notificaiton with given attributes
def notify():
    nt_app_name = "Screen Time Break"
    nt_title = "Screen Time Break"
    nt_message = summary()
    wdir = os.getcwd()
    nt_icon = os.path.join(wdir, 'clock' + (".ico" if platform.platform() =="Windows" else ".png"))
    #nt_time = 10

    notification.notify(
        app_name = nt_app_name,
        title = nt_title,
        message = nt_message,
        app_icon = nt_icon,
        #timeout = nt_time,
    )

# gets and returns time data in seconds, used for sleep function in ST_start()
def getData():
    with open("data.txt") as f:
        data = float(f.readline())
        min_to_sec = data * 60
        f.close()

    return min_to_sec

# returns random string to print out in notify message
def summary():
    #summarize data into message
    data = getData()
    sec_to_min = data / 60
    sumStr = [  "Time to stretch! You've been on for {:.1f} minutes. ".format(sec_to_min),
                "Thirsty? Time to get some water.",
                "It's been {:.1f} minutes. Time for a short break.".format(sec_to_min),
             ]
    #print(sec_to_min)
    return random.choice(sumStr)

# method to start the notification loop.
def ST_start():
    while True:
    #for x in range(2):
        sec = getData()
        for t in  range(int(sec/5)):
            print(t)
            temp = getData()
            time.sleep(5)

            if temp != sec:
                sec = temp
                break
        notify()

# to run script as stand alone program
if __name__ == "__main__":
    ST_start()
