'''
Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
'''
def separate_even_odd():
    size = int(input("Enter the size of the list: "))
    elements = list(map(int, input(f"Enter {size} integers separated by spaces: ").split()))
    if size != len(elements):
        print("Error: The number of elements does not match the specified size.")
        return
    even_numbers = []
    odd_numbers = []
    for num in elements:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)
separate_even_odd()
'''
Enter the size of the list: 6
Enter 6 integers separated by spaces: 5 1 2 7 3 6
Even numbers: [2, 6]
Odd numbers: [5, 1, 7, 3]
