import random

# Word list
words = ["cat", "dog", "bat"]
word = random.choice(words)
display = ["_"] * len(word)
attempts = 6
guessed = []

print("🐾 Welcome to Hangman!")
print(" ".join(display))
print(f"Attempts left: {attempts}")

while attempts > 0 and "_" in display:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed:
        print("🔁 You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                display[index] = guess
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")

    print("\nWord: " + " ".join(display))
    print(f"Attempts left: {attempts}")
    print(f"Guessed letters: {', '.join(guessed)}\n")

# Final result
if "_" not in display:
    print("🎉 You won the game!")
else:
    print(f"💀 You lost! The word was: {word}")
