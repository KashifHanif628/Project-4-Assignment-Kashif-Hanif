# Function to read phone numbers and store them in a dictionary
def read_phone_numbers():
    """
    Ask the user to input names and numbers to store in the phonebook (dictionary).
    Returns the phonebook (dictionary).
    """
    phonebook = {}  # Created an empty dictionary for the phonebook

    while True:  # Keep asking for names and numbers until the user decides to stop
        name = input("Enter name (leave blank to stop): ")  # Ask for a name
        if name == "":  # If no name is entered, exit the loop
            break
        number = input("Enter phone number: ")  # Asked for the corresponding phone number
        phonebook[name] = number  # Add the name and number to the dictionary

    return phonebook  # Returned the complete phonebook


# Function to print all the entries in the phonebook
def print_phonebook(phonebook):
    """
    Print all names and their corresponding numbers in the phonebook.
    """
    for name in phonebook:  # Loop through all names in the phonebook
        print(f"{name} -> {phonebook[name]}")  # Print the name and phone number


# Function to allow the user to look up phone numbers by name
def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers by entering a name.
    """
    while True:
        name = input("Enter name to look up (leave blank to stop): ")  # Ask for a name
        if name == "":  # Exit the loop if no name is entered
            break
        if name not in phonebook:  # Check if the name is in the phonebook
            print(f"{name} is not in the phonebook.")  # If not, inform the user
        else:
            print(f"{name}'s number is: {phonebook[name]}")  # If found, print the number


# Main function to execute the program
def main():
    phonebook = read_phone_numbers()  # Call function to get phonebook entries from the user
    print_phonebook(phonebook)  # Call function to print all phonebook entries
    lookup_numbers(phonebook)  # Call function to allow name lookup


if __name__ == '__main__':
    main()  
