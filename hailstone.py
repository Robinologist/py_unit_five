def sequence(number):
    steps = 0
    while number != 1:
        if number % 2 == 1:
            number = number * 3 + 1
            print(int(number))
        else:
            number = number / 2
            print(int(number))
        steps = steps + 1
    return(steps)

number = int(input("What is the starting number?\n"))
print("Steps:", sequence(number))
