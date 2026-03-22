#Program By: Anu Mishra
#Roll no. :18
#List Assignment:12

#Calculate the sum of all elements in a list without using the sum()function(use a loop and a tracker variable)

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
   total = total+num
print("total marks:",total)


numbers = [10, 20, 30, 40, 50]
total = 0
count = 0
for number in numbers:
    if number>=40:
     total = total + number
     count=count+1

print("Avg mark",total/count)