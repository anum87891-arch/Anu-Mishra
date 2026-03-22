#Program By: Anu Mishra
#Roll no. :18
#List Assignment No:3

#create a list of 6 numbers. Remove the 3rd element by index and the value 10 by name

numbers = [1, 2, 3, 4, 5, 6,]
numbers.pop(2) # remove 3rd element
numbes = [i * 10 for i in numbers]
print(numbers)