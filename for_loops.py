
def count(first, last):
    current=0
    for x in range(last-first+1):
        print(first+current)
        current=current+1


def main():
    number1=int(input("First Number: "))
    number2=int(input("Second Number: "))

    if number1 > number2:
        first = number2
        last = number1
        count(first, last)

    elif number2 > number1:
        first = number1
        last = number2
        count(first, last)

    elif number1 == number2:
        print(number1)

    print("Done!")

if __name__ == '__main__':
    main()
