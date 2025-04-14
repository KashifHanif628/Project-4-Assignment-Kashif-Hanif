def triangle():
    side1 = float(input("Enter the length of Side-1 : "))
    side2 = float(input("Enter the length of Side-2 : "))
    side3 = float(input("Enter the length of Side-3 : "))

    # to claculate the perimeter
    perimeter = side1 + side2 + side3

    # Round off to 2 decimal places
    perimeter = round(perimeter, 2)

    print("The perimeter of the triangle is:", perimeter)

if __name__ == "__main__":
   triangle()
