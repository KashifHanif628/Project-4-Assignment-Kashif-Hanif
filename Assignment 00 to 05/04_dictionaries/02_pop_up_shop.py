def main():
    # A dictionary where the key is the fruit name and the value is its price
    fruits = {'apple': 1.5, 'durian': 50, 'cherry': 80, 'kiwi': 1, 'banana': 1.5, 'mango': 5}
    
    # Variable to keep track of the total cost
    total_cost = 0
    
    # Looping through each fruit in the dictionary
    for fruit_name in fruits:
        # Get the price of the fruit from the dictionary
        price = fruits[fruit_name]
        
        # Ask the user how many of this fruit they want to buy
        amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
        
        # Calculate the total cost for this fruit and add it to the overall total cost
        total_cost += (price * amount_bought)
    
    # Display the total cost
    print(f"Your total is ${total_cost}")
    
# Main function call
if __name__ == '__main__':
    main()
