import random

def function(mylist, a, b):
    number = random.choices(mylist, k = a)
    print(number)
    print(number[b-1]) #print the forth digit in the new list

function([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 18, 4)

