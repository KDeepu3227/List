'''
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
'''
def sort_and_print_list():
    elements = list(map(int, input("Enter the list elements separated by spaces: ").split()))
    elements.sort()
    print("Sorted list:", elements)
sort_and_print_list()
'''
Enter the list elements separated by spaces: 30 20 10 50 40
Sorted list: [10, 20, 30, 40, 50]
