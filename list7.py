#Program By: Anu Mishra
#Roll No :18
#List Assignment :7

#Ask a user for a fruit name.Check if it exists in your fruit_basket list using the in keyword

fruits = ("apple", "banana","mango","orange")
fruit = input("Enter fruit name:")
if fruit in fruits:
    print("Fruits is in the basket")
else:
    print("Fruits not found")
