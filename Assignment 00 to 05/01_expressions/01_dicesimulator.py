# This programme is made to show that how variable scope are works ? i.e
# as per below code we have creadted a 2 function to prove that every funcation has their own vadriable & its cannot be used/execute from outside of their function.
# 1: def roll_dice(): in this function die1 & die2 cannot be used in def main(): function.
# 2: def main(): and in this funtion die1 cannot be used in def roll_dice(): function. 


# Import the random library which lets us simulate random things like dice!
import random

# made a variable to define the number of sides on each die to roll
NUM_SIDES = 6

# create a funtion
def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    # store the both side sums in below total variable.
    total: int = die1 + die2
    print("Total of two dice:", total)


# created the another mai(n function. when ever function will call so main() will run first. 
def main():
    die1: int = 10 # this variable will only axist in this main() function. 
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

# to call the main() function.
if __name__ == '__main__':
    main()



# another new programme. 
def roll_dice():
    dice1 = random.randint(1, 6)  # first dice will generate the number from 1 to 6
    dice2 = random.randint(1, 6)  # second dice will also generate the number from 1 to 6
    total = dice1 + dice2  # calculate the total of both dice numbers.
    print(f"Dice 1: {dice1}, Dice 2: {dice2}, Total: {total}")  # Result print
    return total # every dice total is returning and store 

# roll the dice 3 times.
print("Rolling Dice 3 Times...\n")

# create a variable to store the total of every roll.
grand_total = 0  

# roll the dice 3 times and add the total of this.
grand_total += roll_dice()
grand_total += roll_dice()
grand_total += roll_dice()

# All dice total print 
print("\nTotal of all rolls:", grand_total)
