def generateDigit(a,b,c,loop):
    loop=loop-1
    c=a+b
    a=b
    b=c
    print(c)
    if loop > 1:
        generateDigit(a, b, c,loop)

a=1
b=0
c=0
loop=int(input("How many digits would you like to print?\n"))
generateDigit(a,b,c,loop)
