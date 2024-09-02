import time

# Get the current hour as an integer
hr = int(time.strftime('%H'))

# Determine the appropriate greeting based on the hour
if 6 <= hr <= 11:
    print("Good Morning Sir!")
elif hr <= 17:
    print("Good Afternoon Sir!")
elif hr <= 20:
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")

