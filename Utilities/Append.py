nums = [1, 7, 9, 0, 20, 59]
new_nums = []
for num in nums:
    new_nums.append(num + 1)
  
print(new_nums)
# [2, 8, 10, 1, 21, 60]


pairs = []
for num1 in range(5, 8):
    for num2 in range(9, 12):
        pairs.append((num1, num2))

print(pairs)
# [(5, 9), (5, 10), (5, 11), (6, 9), (6, 10), (6, 11), (7, 9), (7, 10), (7, 11)]
