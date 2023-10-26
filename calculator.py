#Pseudo code
#Print "Enter first number"
#READ firstnum
#Print "Enter Operator(+,-,*,/)"
#READ opeartor
#Print "Enter second number"
#READ secondnum
#output=true
#if operator is + then
#   result=firstnum + secondnum
#else if operator is - then
#   result=firstnum - secondnum
#else if operator is * then
#   result=firstnum * secondnum
#else if operator is / then
#   result=firstnum / secondnum
#else
#   Print "Wrong operator"
#   output=false
#if output==true
#Print("Result is"),result
#--------------------------------------
x=input("Enter first value:")
y=input("Enter second value:")
op=input("Operator (+,-,*,/):")
try:
    x=int(x)
    y=int(y)
    output=True
    if op=="+":
        result=x+y
    elif op=="-":
        result=x-y
    elif op=="*":
        result=x*y
    elif op=="/":
        result=x/y
    else:
        output=False
        print("Wrong operator")
    if output :
        print("Result is",result)
except ValueError:
    print("Please enter number only")
    print(ValueError)