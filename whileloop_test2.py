x=False
while x==False:
    value = input("Enter the number between 1 and 5:")
    try:
        value=int(value)
        if value>5:
            print("Your value is over 5")
        elif value<1:
            print("Your value is less than 1")
        else:
            print("Your number is",value)
            x=True
    except ValueError:
        print("Please enter the number between 0 and 9")