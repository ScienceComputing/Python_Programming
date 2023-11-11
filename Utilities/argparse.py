# Inside the multiply.py
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description="Multiply a number by a factor")

# Add arguments
parser.add_argument("number", type=int, help="The number to multiply")
parser.add_argument("-f", "--factor", type=int, default=2, help="Factor to multiply the number by (default: 2)")

# Parse arguments
args = parser.parse_args()

# Multiply and displaythe result
result = args.number * args.factor
print(f"The result of multiplying {args.number} by {args.factor} is {result}")

# Open the bash, type the following
# python multiply.py 6 -f 2
# The result of multiplying 6 by 2 is 12
