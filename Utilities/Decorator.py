# Reference: https://github.com/ScienceComputing/Python_Programming/blob/main/Utilities/**kwargs.py

# qc_check_required() is a decorator
def qc_check_required(func):  
    def wrapper(*args, **kwargs):
        qc_metrics = kwargs.get('qc_metrics', {}) # Retrieve the value associated with the key 'qc_metrics' from the kwargs dictionary.
        if qc_metrics.get('mito_percent', 0) < 5 and qc_metrics.get('n_genes', 0) > 200 and qc_metrics.get('n_count', 0) > 500: # If the key 'mito_percent' is not found in the qc_metrics dictionary, the method returns the default value 0. This ensures that the code doesn’t raise a KeyError and instead provides a fallback value.
            return func(*args, **kwargs)
        else:
            print("Data QC failed. Analysis not performed.")  # Data doesn't pass QC criteria
            return None
    return wrapper

@qc_check_required # qc_check_required(run_analysis)
def run_analysis(data, qc_metrics):
    print("Running analysis on the data!")
    # Add data analysis code here
    return "Analysis complete"

# *args: allows the wrapper function to accept any number of positional arguments.
# **kwargs: allows the wrapper function to accept any number of keyword arguments.
# If you define def wrapper() without *args and **kwargs, the wrapper function would not accept any arguments, making it impossible to pass any arguments to the original function. 
# This would limit the usefulness of the decorator, as it would only work for functions that take no arguments.

# Example usage:
qc_met = {'mito_percent': 4.5, 'n_genes': 250, 'n_count': 505}
data = {}  
result = run_analysis(data, qc_metrics=qc_met)
