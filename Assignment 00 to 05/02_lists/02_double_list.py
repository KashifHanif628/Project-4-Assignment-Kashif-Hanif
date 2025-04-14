# we have created a programme here that doubles each element in a list of numbers.
# example: we have a list of numbers [1,2,3,4] then convert into double list of numbers. [2,4,6,8] i.e 
# each number is adding into the another number. 

def Main():
    numbers = [1,2,3,4,5]
    numbers = [num * 2 for num in numbers]
    print(numbers)

if __name__ == '__main__':
    Main()
        
    