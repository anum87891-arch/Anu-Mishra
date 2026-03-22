# Program By: Anu Mishra
#Roll no. :18
#List Assignment:10

#Given a list of 10 student marks. count how many students scored above 40.

marks = [35, 50 , 60, 42, 20, 80, 39, 55, 70, 45]
count = 0
for m in marks:
    if m > 40:
        count += 1
print("Students scored above 40:", count)