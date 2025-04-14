def main():
    num = float(input("Type a number to see its square: "))
    
    # to calcualte the square
    squared = num ** 2

    # Round off to 2 decimal places
    squared = round(squared, 2)

    print(f"{num} squared is {squared}") 

if __name__ == '__main__':
    main()
