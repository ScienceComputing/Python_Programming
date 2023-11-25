# @staticmethod is a decorator for a class. It allows us to utilize the methods attached to a class, **without having to create an instance of that class**.
# Reference: https://docs.python.org/3/library/functions.html#staticmethod
class S:
    @staticmethod
    def static_fun(arg_1, arg_2, arg_n): ...
# A static method is callable both on the class itself, for example, as S.static_fun(), and on an instance of the class, like S().static_fun(). 
# Additionally, we can invoke them just like regular functions, as in static_fun().

# Case 1:
import re
class ProcessStockPrice:
    def __init__(self, price_string: str):
        self.price_string = price_string
    @staticmethod
    def remove_non_numeric_characters(price_string: str) -> str: 
        """Remove non-numeric characters from a stock price string"""
        return re.sub(r'[^0-9.]', '', price_string)

# -> remove_non_numeric_characters function is expected to return a string as its result.

price_string = "$123.45"  # Example stock price string with non-numeric characters
clean_price = ProcessStockPrice.remove_non_numeric_characters(price_string)
print(clean_price)

# ^ is a negation operator, which means it will match any character that is not in the following character class.
# [0-9.]: This is the character class itself. It matches any single character that is a digit (0 to 9) or a period (.). In regular expressions, a period is used to match any character, but when it's inside a character class (between square brackets), it matches a literal period.

# Case 2:
import re
class ProcessTranscriptID:
    def __init__(self, transcript_id: str):
        self.transcript_id = transcript_id
    @staticmethod
    def clean_transcript_id(transcript_id: str) -> str:
        """Remove non-alphanumeric characters from a transcript ID"""
        return re.sub(r'[^a-zA-Z0-9]', '', transcript_id)

transcript_id = "ENST00000501550#1"  # Example transcript ID with non-alphanumeric characters
cleaned_id = ProcessTranscriptID.clean_transcript_id(transcript_id)
print(cleaned_id) # 'ENST000005015501'

# Case 2 variant:
# In certain situations we want a reference to a function from within a class, and we also want to prevent it from automatically becoming an instance method. 
def clean_transcript_id(transcript_id: str) -> str:
    """Remove non-alphanumeric characters from a transcript ID"""
    return re.sub(r'[^a-zA-Z0-9]', '', transcript_id)
    
class ProcessTranscriptID:
    def __init__(self, transcript_id: str):
        self.transcript_id = transcript_id
    method = staticmethod(clean_transcript_id)

clean_transcript_id(transcript_id)
ProcessTranscriptID.method(transcript_id) # 'ENST000005015501'


