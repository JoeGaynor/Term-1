import datetime as dt
time = dt.datetime.now().hour

name = input("Please enter your name: ")
if 5 <= time < 12:
    greeting = "morning"
elif 12 <= time < 19:
    greeting = "afternoon"
else:
    greeting = "night"

print(f"Hello {name.capitalize()}, it is nice to see you. I wish you a good {greeting}")
