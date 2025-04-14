def main():
    numbers = []
    
    # Step 1: Input from user
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        numbers.append(int(user_input))

    # Step 2: Count how many times each number appears
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Step 3: Show the result
    for num, count in counts.items():
        print(f"{num} appears {count} times.")

if __name__ == '__main__':
    main()

# 1- List numbers kyun banai? numbers = []
# List (numbers = []) ka use kiya gaya hai taake user se jo numbers input ho, unhe ek ordered collection 
# (yaani ek ordered list) mein store kiya ja sake.

# List mein duplicates allow hote hain, yani agar user ek hi number multiple baar enter kare, 
# toh woh list mein har baar add hoga.


# 2. Dictionary counts kyun banai? counts = {}
# Dictionary (counts = {}) ka use isliye kiya gaya hai taake har number ke saath uske count ko store kiya ja sake. 
# Dictionary mein keys unique hote hain, aur har key ke saath ek value hoti hai. Is case mein, keys wo numbers hain jo 
# user ne enter kiye, aur values un numbers ka count hai.

# Agar number pehle se dictionary mein hai, toh uska count badha diya jata hai. Agar number dictionary mein nahi hai, 
# toh uska count 1 se shuru hota hai.
