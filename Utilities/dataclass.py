# Why use the dataclasses?
# We can set default values for particular fields to ensure that each time we use a dataclass those fields are preset. 
# Dataclasses also provide a default representation for print, log and other outputs. 
# If we need to convert our dataclass to a dictionary or a tuple, dataclasses have functions that can perform that conversion for us.
# We can also make custom properties that do more than just store a value. 
# It's also possible to make frozen instances of a dataclass that doesn't allow any edits to the properties after the dataclass has been created.

from dataclasses import dataclass # Import dataclasses from the dataclass module
