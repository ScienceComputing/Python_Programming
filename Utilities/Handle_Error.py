# ValueError
float('hello')

# TypeError
# Case 1:
def cubic(number): 
    """Returns the cubic of a number."""
    new_value = number ** 3
    return new_value

cubic('banana')

# Calse 2:
len(9999999)


# try-except-else or try-except
# Case 1:
def cubic(number): 
    """Returns the cubic of a number."""
    try: 
        return number ** 3
    except:
        print("The number you've input must be an int or float.")
        
cubic('hello')

# Case 1.1:
def cubic(number): 
    """Returns the cubic of a number."""
    try: 
        return number ** 3
    except TypeError: # Allow other errors except TypeError pass through
        print("The number you've input must be an int or float.")
        
cubic('hello')
    
# Case 2:
nums = [1, 2, "A"]
sum_nums = 0
for item in nums:
    try:
        float_num = float(item)
    except (ValueError, TypeError) as e:
        print(f"This is a non-numeric item: {item}")
    else:
        sum_nums += float_num 
        print(f"{sum_nums=}")

# Case 3: bioinformatics scenarior: load the BAM file and print reads in a specific region
import pysam
try:
    bam_file = pysam.AlignmentFile("alignment.bam", "rb")
except FileNotFoundError:
    print("Error: The BAM file 'alignment.bam' was not found.")
except (IOError, ValueError) as e:
    print(f"Error: An error occurred while reading the BAM file: {e}")
else:
    for read in bam_file.fetch('chr8', 100, 120):
        print(read)
        
    bam_file.close()

# Case 4: 
def sqrt(number): 
    """Returns the square root of a number."""
    if number < 0:
        raise ValueError("The number you've input must be non-negative.")
    try: 
        return number ** 0.5
    except TypeError:
        print("The number you've input must be an int or float.")
        
sqrt('hello')
sqrt(-8)
