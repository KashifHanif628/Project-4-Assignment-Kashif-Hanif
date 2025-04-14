def main():

    num1: int = int(input("please enter the first number to be devided: "))
    num2: int = int(input("Please enter the second number to devided by: "))
    quotient: int = num1 // num2  
    remainder: int = num1 % num2  
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


if __name__ == '__main__':
    main()