'''
Write a Program to find the search element in the given list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the elements of list in single line separated by space.
Third input consists of the element which we need to search
'''
def search_in_list():
    size = int(input("Enter the size of the list: "))
    elements = list(map(int, input(f"Enter {size} integers separated by spaces: ").split()))
    if size != len(elements):
        print("Error: The number of elements does not match the specified size.")
        return
    search_element = int(input("Enter the element to search: "))
    if search_element in elements:
        print(f"{search_element} found in the list.")
    else:
        print(f"{search_element} not found in the list.")
search_in_list()
'''
Enter the size of the list: 6
Enter 6 integers separated by spaces: 4 6 1 8 9 0 
Enter the element to search: 8
8 found in the list.
