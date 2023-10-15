from datetime import datetime
print(datetime.now())
# 2023-10-15 17:28:58.831746

print("Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now()))
# Today's date is 2023-10-15 17:30
