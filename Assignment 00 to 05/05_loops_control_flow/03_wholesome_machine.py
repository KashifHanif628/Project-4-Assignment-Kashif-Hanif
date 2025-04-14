# Ek aisa Python program banao jo user se baar baar ek specific sentence type karwane ko kahe, jab tak wo usay bilkul 
# theek na likh de.
# Example:

# "I am capable of doing anything I put my mind to."
# Agar user galat likhe, to usay bataye:
# "That was not the affirmation."
# Aur phir dubara bole:
# "Please type the following affirmation: ..."
# Jab user sahi likh de, to bole:
# "That's right! :)"

# Affirmation kya hota hai?
# Affirmation ek positive sentence hota hai jo hum khud ko ya doosron ko motivate karne ke liye kehte hain.
# Example:

#"Main kuch bhi kar sakta hoon."
#"Mujhe apne upar bharosa hai."
#"Main strong hoon."

#Ye sentences humare confidence aur positive thinking ko badhate hain

# code.
affirmation = "I believe in myself and I am growing every day."

def main():

    while True:
        print("Please type the following affirmation: " + affirmation)
        user_input = input()
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("That was not the affirmation.")

if __name__ == '__main__':
    main()
