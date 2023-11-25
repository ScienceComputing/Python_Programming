# @staticmethod is a decorator for the class we'are going to make.
# It allows us to utilize the methods attached to a class, without having to create an instance of that class.

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
class ProcessTranscriptID:
    def __init__(self, transcript_id: str):
        self.transcript_id = transcript_id
    @staticmethod
    def clean_transcript_id(transcript_id: str) -> str:
        """Remove non-alphanumeric characters from a transcript ID"""
        return re.sub(r'[^a-zA-Z0-9]', '', transcript_id)

transcript_id = "ENST00000501550#1"  # Example transcript ID with non-alphanumeric characters
cleaned_id = ProcessTranscriptID.clean_transcript_id(transcript_id)
print(cleaned_id)
