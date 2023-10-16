# Method 1: positional formatting
from datetime import datetime
print(datetime.now())
# 2023-10-15 17:28:58.831746

print("Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now()))
# Today's date is 2023-10-15 17:30

from datetime import datetime
get_date = datetime.now()
message = "Good evening. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"
print(message.format(today=get_date))
# Good evening. Today is October 15, 2023. It's 17:36 ... time to work!

# Method 2: fstring
from datetime import datetime
get_date = datetime.now()
message = f"Good morning. Today is {get_date:%B %d, %Y}. It's {get_date:%H:%M} ... time to work!"
print(message)
# Good morning. Today is October 16, 2023. It's 07:30 ... time to work!
