# with this session is BroCode 6 Countdown timer (easy) found on youtube

# first thing is to import the time module

# Type Casting is the method to convert the Python
# variable datatype into a certain data type in order to perform the required operation by users

import time
# this will let program sleep
#time.sleep(5)
# after 5 secs it will print this statement
#print("Time is up")


# asking a user to set a sleep timer
my_time = int(input("Enter a time is Secs: "))

# just range is forward
# but we want to go backwards so inclose range with the reverse function like this "reversed(range(0, my_time))"
# or you can use a step like this range(my_time, 0, -1)
for x in range(my_time, 0, -1):
    # want to display a clock so now to calculate secs min and hours
    seconds = x % 60 # the % remidingless of 60
    # theres 60 secs in a minute
    # will type cast using a int() then with the % 60
    # this will keep it at a max of 60
    minutes = int(x / 60) % 60
    # there is 3600 secs in 1 hour
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up")
