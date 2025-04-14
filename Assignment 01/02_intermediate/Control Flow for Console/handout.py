# 🔍 High-Low Game

# Maqsad: Ye ek chhoti si guessing game hai. Har round mein:
# hame ek number milta hai (1 se 100 ke darmiyan).
# Computer ko bhi ek number milta hai (1 se 100 ke darmiyan) — lekin wo hame nazar nahi aata.
# Aap guess karte ho: kya aapka number computer ke number se "higher" ya "lower" hai?
# Agar aapka guess sahi hota hai, aapko ek point milta hai.
# Aise kai rounds khelne hote hain (jaise 5 rounds).
# Har round ke baad aapka score bataya jata hai.
# Game ke end mein performance ke mutabiq ek message milta hai.

# 🔧 Milestones Summary (Kya-kya karna hai):
# Random numbers generate karo.
# User se guess lo ("higher" ya "lower").
# Check karo guess sahi tha ya nahi.
# Game ko multiple rounds tak chalao.
# Score track karna.
# End pe performance ka message do.

import random
# constant
NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_number}") # prints the all 5 rounds
        your_number = random.randint(1, 100) # to generate our random number.
        computer_number = random.randint(1, 100) # to generate computer random number

        print(f"Your number is {your_number}") # it will show the our random number.

        # Get valid input
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        while guess != "higher" and guess != "lower":
            guess = input("Please enter either higher or lower: ").lower()

        # Check result
        if your_number == computer_number:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        elif (guess == "higher" and your_number > computer_number) or (guess == "lower" and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}")
        print()  # Blank line between rounds

    # Final performance message
    print("Thanks for playing!")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game
if __name__ == '__main__':
    main()