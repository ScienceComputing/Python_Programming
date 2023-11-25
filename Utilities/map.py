# Case 1:
# The map function accepts two parameters: a function and a sequence, e.g., a list, and then proceeds to apply the specified function to each element within the given sequence.
# map(func, seq); map(lambda_func, seq)
num_list = [6, 8, 15, 0, 90, 50]
cubic_all = map(lambda num: num ** 3, num_list)
print(cubic_all) # This is a map object
print(list(cubic_all)) # View the actual elements in the map object

# Case 2:
from datetime import datetime
class ExtractTimeElement:    
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
    @classmethod
    def from_str(cls, date_str):
        element = date_str.split("-")
        year, month, day = map(int, datestr.split("-")) # Convert each element of the list from a string to an integer.
        # Old code: year, month, day = int(element[0]), int(element[1]), int(element[2])
        return cls(year, month, day)
    @classmethod
    def from_datetime(cls, date_obj):
        year, month, day = date_obj.year, date_obj.month, date_obj.day
        return cls(year, month, day)
        
target_time = ExtractTimeElement.from_str('2023-01-30')   
print(target_time.year) # 2023
print(target_time.month) # 01
print(target_time.day) # 30

target_time_2 = ExtractTimeElement.from_datetime(datetime.today())   
print(target_time_2.year) 
print(target_time_2.month)
print(target_time_2.day)
