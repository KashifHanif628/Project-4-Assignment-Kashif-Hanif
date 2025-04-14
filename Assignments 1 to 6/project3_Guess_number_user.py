# Project 3 Guess the number game python project (user)

def main():
    print("Think a number between 1 to 100, and computer will guess it.")
    input("Once think, Please press the Enter...")

    low = 1
    high = 100
    feedback = ""

    while feedback != "correct":
        guess = (low + high) // 2
        print(f"Computer guess is: {guess}")
        feedback = input("If computer guess is low then write 'low', higher then write 'high', and correct then write 'correct': ").lower()

        if feedback == "low":
            low = guess + 1
        elif feedback == "high":
            high = guess - 1
        elif feedback != "correct":
            print("only answers 'low', 'high' or 'correct'.")

    print(f"Congrates...! Computer has guessed your number: {guess}, correctly! 🎉")

if __name__ == '__main__':
    main()
