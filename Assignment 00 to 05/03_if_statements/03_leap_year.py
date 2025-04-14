# 🧠 Problem Issue?
# Hame ek aisa program likhna hai jo user se saal (year) le aur yeh bataye ke woh saal leap year hai ya nahi.

# 📆 What is Leap Year?
# Leap year wo hota hai jisme February 28 ke bajaye 29 din ka hota hai — yani saal mein ek din zyada hota hai (366 din).

# ✅ Leap Year Ka Rule (Asaan Lafzon Mein):
# Agar saal 4 se divide ho jata hai to leap year ho sakta hai. yani year 2028 / 4 = 507 this is a leap year.
# Lekin agar saal 100 se bhi divide hota hai, to yeh leap year nahi hota.
# Magar agar 400 se bhi divide hota hai, to phir leap year hota hai.

def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    if year % 4 == 0:  
        if year % 100 == 0:  
            if year % 400 == 0:
                print("That's a leap year!")
            else:  
                print("That's not a leap year.")
        else:  
            print("That's a leap year!")
    else:  
        print("That's not a leap year.")


if __name__ == '__main__':
    main()