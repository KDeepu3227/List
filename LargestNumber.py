'''
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
'''
def find_largest_number():
   size = int(input("Enter the size of the list: "))
    elements = list(map(int, input(f"Enter {size} integers separated by spaces: ").split()))
     if size != len(elements):
        print("Error: The number of elements does not match the specified size.")
        return
    largest_number = max(elements)
    print("Largest element:", largest_number)
find_largest_number()
'''
Enter the size of the list: 6
Enter 6 integers separated by spaces: 20 30 10 50 73 92
Largest element: 92
