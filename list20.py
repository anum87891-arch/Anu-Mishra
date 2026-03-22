#Program By: Anu Mishra
#Roll No: 18
#List Assingment: 20

#A cricket player runs in 6 matches.Example:[45, 60, 10, 80, 55, 90]find:total runs highest score

runs = [45, 60, 10, 80, 55, 90]
total = 0
highest = runs[0]
for r in runs:
    total +=r
    if r> highest:
        highest = r
print("Total Runs:",total)
print("Highest Score:",highest)



