# Problem Statement Summary:
# Hame ek function get_first_element(lst) complete karna he jo:
# User se milne wali list ka pehla element print kare.
# or Yeh assume kiya gaya hai ke list kabhi khaali nahi hogi (matlab usme hamesha kuch na kuch hoga).

def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])

# print the first element of list which inden number is 0.

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

# User se ek ek karke list ke elements input lenge.
# Jab tak user khaali input (press enter) nahi kerta, woh input list mein add hota rahega.
# Jab user sirf enter press karega, input band hota hai aur final list return hoti hai.

def main():
    lst = get_lst()
    get_first_element(lst)

# get_lst() se user ki list banti hai.

# Us list ko get_first_element() mein bhejta hai taake pehla element print ho jaaye.

if __name__ == '__main__':
    main()
