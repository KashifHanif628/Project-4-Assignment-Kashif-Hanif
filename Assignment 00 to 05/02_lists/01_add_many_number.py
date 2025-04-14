# We have written a function that takes a list of numbers and returns the sum of those numbers.

def add_many_numbers(numbers)-> int:

    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()


# another programme.
def Sum_Of_All (numbers):
    """Takes in a list of numbers and returns the sum of those numbers."""
    add = 0
    for i in numbers:
        add += i
    return add

def Main():
    numbers_list = [1,2,3,4,5,6,7]
    sum = Sum_Of_All(numbers_list)
    print(sum)
 
if __name__ == '__main__':
    Main()
        
        
    
