# Aapko ek aisa program banana hai jo user se poochhe:

"Aap ka qad kitna hai?"

# Aur phir yeh bataye:
# Agar user ka qad 50 ya usse zyada hai →
"Aap ride ke liye kaafi lambi qad rakhte hain!" # (Yani aap ride pe jaa sakte hain)
# Agar user ka qad 50 se kam hai →
"Aap abhi ride ke liye chhote hain, lekin agle saal shayad!"

def tall_enough_extension():
    while True: #  Isme while True: ka matlab hai ke code bar bar chalega, jab tak user khud blank na chhod de.
        user_input = input("How tall are you? or (Leave blank to exit): ")
        if user_input == "":
            break
        height = int(user_input)
        if height >= 50:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    tall_enough_extension()

