# Problem #1: List 
# Kya karna hai:
# Ek list banani hai jisme 5 fruits hoon: 'apple', 'banana', 'orange', 'grape', 'pineapple'
# List ka length print karna hai (yaani list mein kitne items hain).
# List ke end mein 'mango' add karna hai.
# Fir updated list print karni hai.


# 🔹 Problem #2: Index Game
# Is problem mein 4 parts hain:
# List Banana: Kam az kam 5 elements wali koi list banao (numbers ya strings ya dono ka mix).

# Element Access Karna:
# Function banao jo list aur index lega aur us index wala element return karega.
# Agar index galat hua (out of range), to error message de.
# Element Modify Karna:
# Function banao jo list, index aur new value lega aur us index par new value daalega.
# Agar index galat hua to error message de.
# List Slice Karna:
# Function banao jo list, start index aur end index lega aur un elements ka naya list dega.
# Galat index pe error handle kare.
# Game Style Interaction:
# User se poocha jaye ke wo kya karna chahta hai: access, modify ya slice.
# Us hisaab se input le aur result dikhaye.


def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except:
        return "Invalid indices."

def main():
    # 🔹 Problem #1: List Practice
    print("Problem #1: List Practice")
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("Length of fruit list:", len(fruit_list))

    fruit_list.append('mango')
    print("Updated fruit list:", fruit_list)

    # 🔹 Problem #2: Index Game
    print("\nProblem #2: Index Game")
    my_list = ['cat', 'dog', 42, 'apple', 3.14]

    while True:
        print("\nChoose an operation: access / modify / slice / exit")
        choice = input("Your choice: ").lower()

        if choice == "access":
            idx = int(input("Enter index to access: "))
            result = access_element(my_list, idx)
            print("Result:", result)

        elif choice == "modify":
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            result = modify_element(my_list, idx, new_val)
            print("Updated list:" if isinstance(result, list) else "Error:", result)

        elif choice == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == "exit":
            print("Exiting the game.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# Pehle fruit list banata hai, uska size print karta hai, usme 'mango' add karta hai.
# Phir ek simple list game chalata hai jisme tum access, modify, ya slice kar sakte ho list ko.
# Har operation mein user se inputs liye jaate hain aur output diya jata hai.