# moduleabc.py
def abc_function():
    print("This is a abc function")

if __name__ == '__main__':
    print("This is the main part of the script")

# another_script.py
import moduleabc as mabc

mabc.abc_function()
