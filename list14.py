#Program By: Anu Mishra
#Roll No: 18
#List Assingment: 14

#Store prices of 5 items in a list. Calculate the total bill and the average marks

prices = [120, 250, 80, 150, 200]
total = 0
for price in prices:
    total = total + price
average = total / len(prices)

print("Total Bill:", total)
print("Average price per item", average)