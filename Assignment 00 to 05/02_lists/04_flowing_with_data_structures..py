# clarification between immutable dadta types & mutable data types.

# Immutable data types:
# Jab hum immutable data types (jaise numbers ya strings) ko kisi function mein modify karte hain, to woh changes 
# function ke bahar apply nahi hote jab tak hum value ko return karke wapas assign na karein.

# Mutable data types:
# Lekin mutable data types (jaise lists ya dictionaries) ka behavior alag hota hai. Agar aap list ya dictionary ko 
# function mein change karte ho, to woh changes function ke bahar bhi nazar aate hain, return karne ki zarurat nahi hoti.

def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

# my_list aur data input le raha hai.
# 3 dafa data ko my_list ke andar append (add) kar raha hai.

#⚠️ Important: my_list ek mutable data type hai (list), to jab hum isme kuch bhi append() karte hain, 
# woh changes original list mein reflect hotay hain — chahe hum function se kuch return karein ya na karein.

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()

# User se message input liya ja raha hai (e.g., "Hello world!").

# Ek khaali list my_list = [] banayi he.

# add_three_copies() ko call kiya gaya, jo us message ko list mein 3 dafa daal dega.

# Function se kuch return nahi ho raha, lekin list ke andar changes ho gaye he.

# Is liye "List after:" wale print mein woh 3 copies dikhti hain.

