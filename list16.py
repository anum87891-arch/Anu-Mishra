#Program By: Anu Mishra
#Roll No: 18
#List Assingment: 16

#Store marks of 5 students in a list and calculate the average marks.

marks = [75, 85, 90, 68, 86]
total = 0
for m in marks:
    total += m
average = total /len (marks)
print("Average marks:",average)