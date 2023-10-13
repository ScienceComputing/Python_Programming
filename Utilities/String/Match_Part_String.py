cake_name = ['Vanilla Cake', 'Red Velvet Cake', 'Black Forest Cake']
print([name for name in cake_name if name.startswith('B')])
# ['Black Forest Cake']

print([name for name in cake_name if name.startswith('b')])
# []

print([name for name in cake_name if name.lower().startswith('b')])
# ['Black Forest Cake']

quote = 'We are what we repeatedly do. Excellence, then, is not an act, but a habit.'
'habit' in quote
# True
'Habit' in quote
# False

quote_upper = 'We are what we repeatedly do. Excellence, then, is not an act, but a habit.'.upper()
'HABIT' in quote_upper
# True
