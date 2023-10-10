# ValueError
float('hello')

# TypeError
def cubic(number): 
    """Returns the cubic of a number."""
    new_value = number ** 3
    return new_value

cubic('banana')

# try-except-else
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

# Bioinformatics scenarior: load the BAM file and print reads in a specific region
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
