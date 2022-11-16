def generateDigit(digits):
    a = 1
    b = 0
    c = 0
    for x in range(digits):
        c=a+b
        a=b
        b=c
        print(c)

digits=int(input("How many digits would you like to print?\n"))
generateDigit(digits)
