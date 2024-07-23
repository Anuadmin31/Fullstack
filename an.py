import datetime

current_time = datetime.datetime.now().time()
current_hour = current_time.hour

if 5 <= current_hour <12:
    print("Good morning! the current time is:",current_time)
elif 12>= current_hour <18:
    print("Good Afternoon!, the current time is:",current_time)
elif 18>= current_hour <24:
    print("Good evening, the current time is:",current_time)
else:
    print("Good night! ,the current time is:",current_time)