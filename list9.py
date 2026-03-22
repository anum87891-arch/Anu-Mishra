#Program By: Anu Mishra
#Roll no. :18
#List Assignment:9

#Write a program that takes a list of names and a "search_name" from the user.Print the index where the name is found,or "Not found."

names = ["Aman", "Rahul", "Rohit", "Sohan"]
search_name = input("Enter name to search:")
if search_name in names:
    print("Index:",names.index(search_name))
else:
    print("Not found")