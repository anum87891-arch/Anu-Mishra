#Program By: Anu Mishra
#Roll no. :18
#List Assignment:8

#Given a list of numbers 1-20, create a new list that contains only even numbers.

numbers = list(range(1, 21))
even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers)
