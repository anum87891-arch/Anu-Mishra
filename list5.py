#Program By: Anu Mishra
#Roll No. :18
#List Assignment:5

#create a list of 10 random integers.Use a for loop to print each number multiplied by 2.

import random
nums = []
for i in range(10):
    nums.append(random.randint(1, 100))
for n in nums:
    print(n * 2)
