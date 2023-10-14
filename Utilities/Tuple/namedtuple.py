# A namedtuple is a tuple where each position (column) has a name.
# It is alternative to a pandas DataFrame row.
# The namedtuple works when we do not need the nested structure of a dictionary.

# Create a namedtuple type: name + a list of fields
from collections import namedtuple
TV_show = namedtuple('TV_show', ['title', 'genre', 'rating', 'seasons'])
TV_show_collection = []
best_TV = [{'title': 'Game of Thrones',
            'genre': 'Action, Adventure, Drama',
            'rating': 9.3,
            'seasons': 6}]

for TV_i in best_TV:
    # print(TV_i)
    details = TV_show(TV_i['title'], 
                      TV_i['genre'], 
                      TV_i['rating'], 
                      TV_i['seasons'])
    TV_show_collection.append(details)
  
print(TV_show_collection)
# [TV_show(title='Game of Thrones', genre='Action, Adventure, Drama', rating=9.3, seasons=6)]

# Each field is available as an attribute of the namedtuple
for TV_i in TV_show_collection:
    print(TV_i.title)
    print(TV_i.genre)
    print(TV_i.rating)
    print(TV_i.seasons)

# Game of Thrones
# Action, Adventure, Drama
# 9.3
# 6
