def get_sum(number):
    current=0
    for x in range(number):
        current=current+1
        if number%current == 0:
            print(current)

number=int(input("Number: "))
get_sum(number)