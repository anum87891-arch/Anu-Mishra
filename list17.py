#Program By: Anu Mishra
#Roll No: 18
#List Assingment: 17

#Store temperature of 7 days in a list and find the highest temperature
temperature= [32, 35, 30, 37, 33, 36, 34]
highest= temperature[0]
for t in temperature:
    if t > highest:
        highest = t
print("Highest Temperature:",highest)