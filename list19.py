#Program By: Anu Mishra
#Roll No: 18
#List Assingment: 19

#A teacher store attendance of students in a list(1 = present, 0 = absent).Example:[1, 1, 0, 1,0, 1, 1] Write a program to: count total persent count total absent print attendance percentage

attendance= [1, 1, 0, 1, 0, 1,1]
present = attendance.count(1)
absent = attendance.count(0)
percentage = (present / len(attendance)) * 100
print("Total Persent:",present)
print("Total Absent:",absent)
print("Attendance Percentage:",percentage,"%")