import csv

variable = input("What's the variable of your interest?")
code = input("How is the variable of your interest coded?")

with open("variable_dictionary", "a") as f: # a: append mode, no overwrite
    w = csv.writer(f)
    w.writerow([variable, code])


"""If a CSV file has pre-defined column headers - variable name, code"""
variable = input("What's the variable of your interest?")
code = input("How is the variable of your interest coded?")

with open("variable_dictionary", "a") as f: 
    w = csv.DictWriter(f, fieldname=['variable name', 'code'])
    w.writerow({'variable name': variable, 'code': code}) # Or w.writerow({'code': code, 'variable name': variable})
