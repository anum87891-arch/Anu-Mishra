#Program By: Anu Mishra
#Roll No: 18
#List Assingment: 22

#Marks of students store in a list. marks = [78, 35, 90, 40, 55] Write a program to : Print PASS if marks > 40 Print FAIL if marks < 40 Count how many students passed
marks = [78, 35, 90, 40, 55]
pass_count = 0
for m in marks:
    if m >= 40:
        pass_count += 1
print("Students Passed:",pass_count)