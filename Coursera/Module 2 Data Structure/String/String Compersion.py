# we can compare the string

while True:
    word = input("Enter the fruit name: \n")

    # stop the loop
    if word == "Bas kar":
        print("Program stopped!")
        break

    if word == "Banana":
        print("You entered Banana")
    elif word == "Apple":
        print("You entered Apple")
    elif word == "Grapes":
        print("You entered Grapes")
    else:
        print(f"You entered {word} haha")
