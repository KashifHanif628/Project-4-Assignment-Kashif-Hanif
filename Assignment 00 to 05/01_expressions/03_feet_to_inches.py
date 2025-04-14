
"""
An example program with constants
"""

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet from user, 
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")
    
# to call the main() function.
if __name__ == '__main__':
    main()



# 2nd programme.
Inches_per_foot: int = 12

def main():
    feet: int = int(input("Please enter the Feet, which you want to convert into Inches: "))
    inches_total: int = feet * Inches_per_foot 
    print("That is", inches_total, "inches!")
    
if __name__ == '__main__':
    main()