#Program By: Anu Mishra
#Roll No: 18
#List Assingment: 23

#A cricket player scored runs in 6 matches. Example:[45, 60, 10, 80, 55, 90] Write a program to: Find total runs Find highest score Count how many matches player scored more than 50 runs
runs = [45, 60, 10, 80, 55, 90]
count = 0
for r in runs:
    if r > 50:
        count +=1
print("Matches with more than 50 runs:", count)