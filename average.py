numbers=[]  #makes an empty list to contain all the numbers
output=0

def mainloop():
    add = input("what number would you like to add to the average calculation? (Q to end)\n")

    if add == "q":              #ends the loop if Q is inputted
        print("Here are your inputted numbers:",numbers)
        output=sum(numbers)/len(numbers)
        print("Here is their average:",output)

    else:
        add = int(add)          #adds to the list if a number is inputted
        numbers.append(add)
        print(add,"has been added!")
        mainloop()

#starts the loop
mainloop()