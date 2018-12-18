import re
print("Hello Everyone! This is magical calculator")
print("For exit the Window type 'Quit' \n")
previous=0 #intialise previous equal to 0 firs
run= True
def calculator():
    global previous
    # mark global previous and run
    evaluate = ""
    global run
    if previous == 0:
        evaluate = input("Enter Equation: ").strip()
    else:
        evaluate=input(str(previous))

    if evaluate == "Quit":
        run=False
    else:
        evaluate=re.sub('[a-zA-Z,.:()" "]'," ",evaluate)#re.sub is using for removing those data which are in the square bracket
        evaluate=evaluate.strip()
        if previous==0:
            previous=eval(evaluate)
        else:
            previous=eval(str(previous)+evaluate)#calculating next value with previous value
        print("The Result is: ",previous)

while run:
    calculator()

