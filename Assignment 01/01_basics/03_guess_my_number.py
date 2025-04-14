import random

def main():

    guess_number = random.randint(0, 99)

    print("Welcome to number guessing game and win exciting prizes.")

    guess = int(input("Please enter the number: "))

    while guess != guess_number:
        if guess < guess_number:
            print("your guess is too low")
        else:
            print("your guess is too high")

        print()
        guess = int(input("Please enter the number once again: "))

    print("Congrates! You guess the correct number: " + str(guess_number))
    print("Here is your wining prize of Rs. 1000/-")

if __name__ == '__main__':
    main()