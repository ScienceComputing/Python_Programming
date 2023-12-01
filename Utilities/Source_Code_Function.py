import inspect
import moduleabc
  
source_code = inspect.getsource(moduleabc.abc_function)
print(source_code)

# def abc_function():
#     print("This is a abc function")
