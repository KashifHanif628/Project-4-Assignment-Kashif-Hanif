
PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Sophia is working late in the office. Her manager says: Sophia, before you leave, make sure all the windows are closed. Sophia nods and replies: Okay! Next morning, the manager finds all Windows computers in the office shut down. Sophia smiles: I closed all the Windows."
SORRY: str = "Sorry I only tell jokes."

def main():
    user_input = input(PROMPT)
    
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
