#Program By: Anu Mishra
#Roll No: 18
#List Assingment: 15

#A week's temperatures are stored in a list.Find how many days were "Hot" (above 35℃)

temperature = [32, 36, 34, 38, 37, 33]
hot_days = 0

for temp in temperature:
    if temp > 35:
        hot_days +=1
print("number of hot days:",hot_days)