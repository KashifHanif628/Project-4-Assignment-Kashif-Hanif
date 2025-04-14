# Hame ek function shorten(lst) banana hai jo:
# Ek list (lst) leta hai.
# Us list ke aakhri elements hataata rahta hai (remove karta hai).
# Har baar jo element hattaaye, usse print bhi kare.
# Yeh process tab tak chalta hai jab tak list mein sirf 3 items bache (yaani MAX_LENGTH = 3 ho jaye).
# Agar list pehle se 3 ya 3 se kam items ki ho, toh usay waise hi chhod do, kuch bhi na karo.

# example 
# if input list is: 
# lst = [10, 20, 30, 40, 50]

# Toh shorten(lst) ko ye karna chahiye:
# 50 ko hataaye aur print kare
# 40 ko hataaye aur print kare

# Ab list ban jaayegi: [10, 20, 30]
# Bus, ab 3 elements reh gaye, to ham is se aage nahi jainge.

MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print("remove element is:", last_elem)


def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    items = input("Please enter the item of your list or press enter to stop. ")
    while items != "":
        lst.append(items)
        items = input("Please enter the item of your list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()
 