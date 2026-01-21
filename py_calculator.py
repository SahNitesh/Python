                            #5) basic_python_calculator

valid_operators = ["+", "-", "*", "/", '%', "**"] #lsit of valid operators
is_online = True                                   #for while loop activation and demolation

while is_online:                                    #star of loop
    print("!-----------Baisc python Calculator-------------!")  # some decoration
    print("!-----enter operator and numbers(only 2)--------!")
    print("!--------------Tx xite press 'x'_---------------!")
    "----------------------------------------------------------------------------------------"

    operator = input("Enter an operator (+ - * / % **) : ")  # getting users input on operators

    if operator == "x" or operator == "X":                        # for closing the calculator x
        is_online = False                             #it make the is_online value false and therefore makes the while loop end
        print("---clculator_closed---")
    elif operator not in valid_operators:             #if the operator does not match the valid_operators list it will not register
        print("please enter a valid  operator-!!!")
        print("")
        continue                                      # goes back to the top or start of while lloop

    "------------------------------------------------------------------------"

    num_1 = float(input("number: "))                   # getting users input on num
    num_2 = float(input("second number: "))            #keeping it float value

    "------------------------------------------------------------------------"

    if operator == "+":                 #assign logic on what to do
        result = num_1 + num_2          #assigning the answer of the calulation to a variable
        print("output:  ", end=" ")
        print(round(result, 3))         #printing result with max 3no's after decimal points
    elif operator == "-":
        result = num_1 - num_2
        print("output:  ", end=" ")
        print(round(result, 3))
    elif operator == "*":
        result = num_1 * num_2
        print("output:  ", end=" ")
        print(round(result, 3))
    elif operator == "/":
        result = num_1 / num_2
        print("output:  ", end=" ")
        print(round(result, 3))          #asssigning the logic to varius operators

    elif operator == "%":
        result = num_1 % num_2
        print("output:  ", end=" ")
        print(round(result, 3))

    elif operator == "**":
        result = num_1 ** num_2
        print("output:  ", end=" ")
        print(round(result, 3))

    "--------------------------------------------------------------------"
    print("do you wish to do another calculation")              #getting users input
    another = input('press "y" for yes or "n" for no:  ') .lower()   # for another calulation y/n
    if another == "y":                                          # if yes the while loop is active
        is_online = True
    else:                                                       # if no while loop is false deactivate
        is_online= False

                                            # end of program


print("!_--Calulator closed---!")    #End of calculaot

"--------------------------------------------------------------------------"
# if you enter anything except for a number is num_1 and num_2 input area it will throw up an error
        # bored enough to fix it