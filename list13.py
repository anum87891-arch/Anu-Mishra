#Program By: Anu Mishra
#Roll no. :18
#List Assignment:13

#Create a list of ages.Create two new lists:minors(under 18)and adults(18 and above)

ages = [10, 15, 18, 22, 30]
minors = []
adults = []
for age in ages:
    if age < 18:
        minors.append(age)
    else:
        adults.append(age)

print("Minors:", minors)
print("Adults:", adults)