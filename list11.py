#Program By: Anu Mishra
#Roll no. :18
#List Assignment:11

#Take a list like [-5, 3, -2, 8].Create a new list where all negative numbers are converted to positive.

nums = [-5, 3, -2, 8 ]
new_list = []
for n in nums:
    new_list.append(abs(n))
print(new_list)