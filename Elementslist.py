'''
Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
'''
def create_and_display_list():
    inputs = list(map(int, input("Enter the size followed by the list elements: ").split()))
    size = inputs[0]
    if size != len(inputs) - 1:
        print("Size mismatch! The number of elements does not match the specified size.")
        return
    elements = inputs[1:size + 1]  # Get the elements based on the specified size
    print("Created list:", elements)
# Example usage:
create_and_display_list()
'''
Enter the size followed by the list elements: 5 10 20 30 40 50
Created list: [10, 20, 30, 40, 50]
