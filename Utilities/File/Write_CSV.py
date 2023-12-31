import csv

variable = input("What's the variable of your interest?")
code = input("How is the variable of your interest coded?")

with open("variable_dictionary", "a") as f: # a: append mode, no overwrite
    w = csv.writer(f)
    w.writerow([variable, code])
