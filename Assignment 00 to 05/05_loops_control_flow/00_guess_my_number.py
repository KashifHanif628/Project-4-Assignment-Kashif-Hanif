import random

def main():
    
    guess_number = random.randint(0, 99)

    print("Welcome to Number guessing Game, Please guess the correct number & win exciting prizes!")

    guess = int(input("Guess the number: "))

    while guess != guess_number:
        if guess < guess_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high")

        print()
        guess = int(input("Please guess the once number again: "))

    print("Congrates! You guess the correct number: " + str(guess_number))
    print("Here is your wining prize of Rs. 1000/-")

if __name__ == '__main__':
    main()
