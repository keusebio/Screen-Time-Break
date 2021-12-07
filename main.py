from plyer import notification
import time

def notify():
    nt_title = "Screen Time"
    nt_message = summary()
    nt_icon = "clock.ico"
    nt_time = 10
    
    notification.notify(
        title = nt_title,
        message = nt_message,
        app_icon = nt_icon, 
        timeout = nt_time,
    )

def getData():
    screen_analytics = [    "Today",
                            "Weekly",
                            "Monthly",
                        ]


    #read from file
    with open("data.txt") as f:
        for stats in screen_analytics:
            data = f.readline()
    return data

def summary():
    #summarize data into message
    data = getData()
    
    return "test"

if __name__ == '__main__':
    notify()
       