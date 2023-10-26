#Pseudo code
#Print "Enter first number"
#READ firstnum
#Print "Enter second number"
#Read secondnum
#if secondnum is less than or equal zero
# Print "Second number must be greater than zero"
#else
# Print firstnum + "divied by " +secondnum
# Print firstnum/secondnum
firstnum=input("Enter first number :")
secondnum=input("Enter second number :")
try:
    firstnum=int(firstnum)
    secondnum=int(secondnum)
    if secondnum<=0:
        print("Second number must be greater than 0")
    else:
        print(firstnum," divided by",secondnum)
        print(firstnum/secondnum)
except ValueError:
    print("Please enter number only")