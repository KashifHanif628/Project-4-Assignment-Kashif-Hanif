def main():
    # User se number input lena
    curr_value = int(input("Enter a number: "))

    # Jab tak number 100 se chhota hai, double karte jao aur print karte jao
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# Program ka entry point
if __name__ == "__main__":
    main()
