from plyer import notification
import time
import os
import platform
import random
def notify():
    nt_title = "Screen Time"
    nt_message = summary()
    wdir = os.getcwd()
    nt_icon = os.path.join(wdir, 'clock' + (".ico" if platform.platform() =="Windows" else ".png"))
    nt_time = 10

    notification.notify(
        title = nt_title,
        message = nt_message,
        app_icon = nt_icon,
        timeout = nt_time,
    )

def getData():
    with open("data.txt") as f:
        data = int(f.readline())
        print(data)
        min_to_sec = data * 60
        print(min_to_sec)
        f.close()

    return min_to_sec

def summary():
    #summarize data into message
    data = getData()
    sec_to_min = data / 60
    sumStr = [  "Time to stretch! You've been on for {:.0f} minutes. ".format(sec_to_min),
                "Thirsty? Time to get some water.",
                "It's been {:.0f} minutes. Time for a short break.".format(sec_to_min),
             ]
    print(sec_to_min)
    return random.choice(sumStr)

if __name__ == '__main__':
    notify()
