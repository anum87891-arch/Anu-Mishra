#Program By: Anu Mishra
#Roll No: 18
#List Assingment: 21

#A teacher stores marks of students in a list marks = [78, 65, 89, 90,56] Write a program to:1 print all marks  3 Find total marks 4Find average marks 5 Find highest marks 6 Find lowest marks
marks = [78, 65, 89, 90, 56]
print("ALL Marks:", marks)
total = 0
highest = marks[0]
lowest = marks[0]
for m in marks:
    total +=m
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
average = total/len(marks)
print("Total Marks:",total)
print("Average Marks:",average)
print("Highest Marks:",lowest)
