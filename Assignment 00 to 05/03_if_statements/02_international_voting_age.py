# Yeh ek simple condition-checking programme hai jisme user se unki age li ja rahi hai, aur phir bataya ja raha hai
# k woh teen fictional countries me vote kar sakte hain ya nahi — depending on unka voting age.

# 🧠 Samajhne wali baat:
# Har country ka voting age different hai:

# Peturksbouipo: 16
# Stanlau: 25
# Mayengua: 48

# To agar user ki age kisi country ke voting age se zyada ya barabar hai, to wo vote kar sakta hai. Agar kam hai, 
# to wo vote nahi kar sakta.

def main():
    # User se age lete hain
    age = int(input("How old are you? "))

    # Peturksbouipo voting check
    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    # Stanlau voting check
    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    # Mayengua voting check
    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

# Run the main function
if __name__ == "__main__":
    main()


# another programme

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Check if the user can vote in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    
    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    
    # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()