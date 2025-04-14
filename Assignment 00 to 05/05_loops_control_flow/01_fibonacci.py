# aik aisa program likhna hai jo Fibonacci sequence ke numbers ko print karey jab tak wo 10,000 se chhote hon.

# Fibonacci sequence mein pehle do numbers hote hain:
# 0 aur 1
# Aur har agla number pichlay do numbers ka jama (sum) hota hai:

# Fib(0) = 0  
# Fib(1) = 1  
# Fib(2) = 1 (0 + 1)  
# Fib(3) = 2 (1 + 1)  
# Fib(4) = 3 (1 + 2)  
# Fib(5) = 5 (2 + 3)  
# Fib(6) = 8 (3 + 5)  
# ... aur aise hi chalta rehta hai


# short and Understandable code.
max_value = 10000

def main():
    a, b = 0, 1

    while a <= max_value:
        print(a, end=" ")
        a, b = b, a + b

if __name__ == '__main__':
    main()


# another programme.

MAX_TERM_VALUE : int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

if __name__ == '__main__':
    main()