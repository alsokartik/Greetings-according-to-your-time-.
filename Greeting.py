import time

def greeting():
    current_hour = int(time.strftime('%H'))
    if current_hour < 12:
        print("Good Morning !")
    elif 12 <= current_hour < 18:
        print("Good Afternoon !")
    elif 18 <= current_hour <20:
        print("Good Evening !")
    else:
        print("Good Night !")

greeting()