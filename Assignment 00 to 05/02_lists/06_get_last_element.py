# Problem Statement Summary:
# Hame ek function get_last_element(lst) complete karna he jo:
# User se milne wali list ka last element print kare.

def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """
    print(lst[len(lst) - 1])
    # print(lst[-1]) we can also print the last element of the list like this.

# Jo list lst ke naam se milti hai, uski length ko dekhte huway -1 lagane se last element print ho jayga.

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
    get_last_element(lst)

# get_lst() se user ki list banti hai.

# Us list ko get_last_element() mein bhejta hai taake last element print ho jaaye.

if __name__ == '__main__':
    main()
