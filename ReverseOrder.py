'''
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
'''
def print_reverse_list():
    elements = list(map(int, input("Enter the list elements separated by spaces: ").split()))
    print("Reversed list:", elements[::-1])
print_reverse_list()
'''
Enter the list elements separated by spaces: 10 20 30 40 50
Reversed list: [50, 40, 30, 20, 10]
