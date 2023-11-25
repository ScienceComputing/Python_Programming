class ExtractTimeElement:    
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
    @classmethod
    def from_str(cls, date_str):
        element = date_str.split("-")
        year, month, day = int(element[0]), int(element[1]), int(element[2])
        return cls(year, month, day)
        
target_time = ExtractTimeElement.from_str('2023-01-30')   
print(target_time.year) # 2023
print(target_time.month) # 01
print(target_time.day) # 30
