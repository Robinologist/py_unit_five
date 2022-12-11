"""
Will return the sum of all the clean multiples of the given number.
Ex. get_sum(10) returns 18
"""

def get_sum(number):

    current = 0
    total = 0

    for x in range(number):
        current = current+1
        if number % current == 0:
            total = total + current

    return total

input=int(input("Number: "))
print(get_sum(input))