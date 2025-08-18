import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print("Wake up your time is over!")

t = input("Enter the time in seconds: ")


countdown(int(t))


#OUTPUT

Enter the time in seconds: 5
Wake up your time is over!
