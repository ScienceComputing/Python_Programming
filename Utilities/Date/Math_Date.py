from datetime import date

birthdate_list = [date(1998, 3, 9), date(2000, 12, 7)]
print(min(birthdate_list))
# 1998-03-09

(date(2000, 12, 7) - date(1998, 3, 9)).days
# 1004

from datetime import timedelta

print(date(1998, 3, 9) + timedelta(days=1004))
# 2000-12-07
