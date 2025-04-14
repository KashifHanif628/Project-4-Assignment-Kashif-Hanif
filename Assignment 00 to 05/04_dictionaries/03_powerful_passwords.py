from hashlib import sha256  # SHA256 hashing algorithm ko import kar rahe hain

def login(email, stored_logins, password_to_check):
    """
    Agar email ka password ka hash stored_logins mein match karta hai
    password_to_check ke hash se, toh True return karte hain, warna False.

    email: jis email ka password check karna hai
    stored_logins: ek dictionary jisme email ka hash password stored hota hai
    password_to_check: wo password jo hum check karna chahte hain login ke liye
    """
    
    # Agar stored login ka password hash password_to_check ke hash se match karta hai
    if stored_logins[email] == hash_password(password_to_check):
        return True  # Agar match ho jata hai, toh login successful hai
    
    return False  # Agar match nahi hota, toh login failed hai

# Yeh function password ko hash karta hai
def hash_password(password):
    """
    Password ko le kar uska SHA256 hash return karta hai.
    
    Inputs:
        password: wo password jo hum hash karte hain
    
    Outputs:
        hashed password (SHA256 ke format mein)
    """
    return sha256(password.encode()).hexdigest()  # SHA256 mein password ko convert karte hain

def main():
    # stored_logins dictionary mein emails aur unke hashed passwords hain
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # hash of "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # hash of "Karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # hash of "password"
    }
    
    # Test cases (login attempts):
    print(login("example@gmail.com", stored_logins, "word"))  # False, "word" ka hash "password" ke hash se match nahi hota
    print(login("example@gmail.com", stored_logins, "password"))  # True, "password" ka hash match karta hai

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # True, "Karel" ka hash match karta hai
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # False, "karel" ka hash match nahi hota

    print(login("student@stanford.edu", stored_logins, "password"))  # True, "password" ka hash match karta hai
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # False, yeh password match nahi karega

if __name__ == '__main__':
    main()  # Program ko run karte hain
