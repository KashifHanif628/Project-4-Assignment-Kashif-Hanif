
# we have made a function of get list, inwhich we will get the input from the user to add the items in the list.
# when user add the one item in the list and will press the enter for next step then question will ask again, 
# please enter the item of your list, it will continoue until the user will not press enter without adding items.
# Once he press the enter without adding the items. its list will print.

def get_list():
    
    lst = []
    items: str = input("Please enter the item of your list: ")
    while items:
        lst.append(items)
        items = input("Please enter the item of your list: ")

    print("Here's the list of your items:", lst)
    
if __name__ == '__main__':
    get_list()
