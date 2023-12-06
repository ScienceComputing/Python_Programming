from collections import Counter

"""
Case 1
"""
list1 = ['a', 'a', 'b']
list1_freq = Counter(list1)
print(list1_freq)
# Counter({'a': 2, 'b': 1})
print(list1_freq['a'])
# 2

"""
Case 2
"""
list2 = ['a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 100]
list2_freq = Counter(list2)
list2_freq.most_common()
# [('a', 4), ('c', 2), ('b', 1), ('d', 1), (100, 1)]
list2_freq.most_common(3)
# [('a', 4), ('c', 2), ('b', 1)]

"""
Case 3
"""
def element_counter(obj, n_most_common=3):
  counter_obj = Counter(obj)
  top_elements = counter_obj.most_common(n_most_common)
  return top_elements

# Visualize the frequency of most common elements
import matplotlib.pyplot as plt

def plot_most_common_element(top_elements):
    top_elements_dict = dict(top_elements)
    plt.figure()
    plt.bar(range(len(top_elements_dict)), list(top_elements_dict.values()), align='center')
    plt.xticks(range(len(top_elements_dict)), list(top_elements_dict.keys()), rotation='vertical')
    plt.tight_layout()
    plt.show()

list2 = ['a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 100]
element_counter(list2)
# [('a', 4), ('c', 2), ('b', 1)]
plot_most_common_element(element_counter(list2))

"""
Case 4
"""
def sum_counters(counters):
    return sum(counters, Counter())

counter1 = Counter({'apple': 3, 'banana': 2, 'cherry': 1}) #!
counter2 = Counter({'apple': 2, 'banana': 4, 'date': 3})
counter3 = Counter({'banana': 1, 'date': 2, 'elderberry': 5})
counters_list = [counter1, counter2, counter3] #!
result_counter = sum_counters(counters_list)
print(result_counter)
# Counter({'banana': 7, 'apple': 5, 'date': 5, 'elderberry': 5, 'cherry': 1})

"""
Case 5
"""
from collections import Counter

class Document:
    def __init__(self, text):
        self.text = text
        self.tokens = self._tokenize()
        self.word_counts = self._count_words()
    def _tokenize(self):
        # Tokenize the document using a non-public method.
        return tokenize(self.text)
    def _count_words(self):
        # Tally the document's word counts using Counter (non-public method).
        return Counter(self.tokens)
      
def select_word_counts(word_counts, first_char):
    """
    Count the words selected by the first character

    :param word_counts: Word counts attribute of a Document class instance
    :param first_char: Select counts of words that start with this character

    >>> # Count the words which start with 'Z'
    >>> select_word_counts(document.word_counts, 'Z')
    """
    return Counter({w: c for w, c in word_counts.items() if w[0].lower() == first_char.lower()})

quote = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair.'
quote_doc = Document(text=quote)
select_word_counts(quote_doc.word_counts, 'i')
# Counter({'it': 9, 'It': 1, 'incredulity': 1})

