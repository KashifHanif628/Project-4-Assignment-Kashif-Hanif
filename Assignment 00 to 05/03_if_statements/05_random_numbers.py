import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    
    for _ in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(number, end=' ')
    print()  # Line break at the end

if __name__ == '__main__':
    main()


# another programme for unique numbers.

import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Prints N_NUMBERS unique random integers between MIN_VALUE and MAX_VALUE (inclusive).
    Each number is separated by a space and printed on the same line.
    """
    numbers = random.sample(range(MIN_VALUE, MAX_VALUE + 1), N_NUMBERS)
    for number in numbers:
        print(number, end=' ')
    print()  # Line break at the end

if __name__ == '__main__':
    main()


# 3rd programme how to know these are unique numbers.

import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Prints N_NUMBERS unique random integers between MIN_VALUE and MAX_VALUE (inclusive),
    and confirms if all numbers are unique.
    """
    numbers = random.sample(range(MIN_VALUE, MAX_VALUE + 1), N_NUMBERS)

    print("Generated numbers:")
    print(*numbers)

    # Check uniqueness
    if len(numbers) == len(set(numbers)): # set numbers remove to automatically duplicate numbers.
        print("✅ All numbers are unique!") # if len(numbers) & len(set(numbers)) are equal ➝ then no duplicate will found.
    else:
        print("❌ Duplicate numbers found!") # other wise there duplicate number will found.

if __name__ == '__main__':
    main()
