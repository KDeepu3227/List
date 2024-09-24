'''
write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
'''
def create_and_display_list():
    inputs = list(map(int, input("Enter the size followed by the list elements: ").split()))
    size = inputs[0]
    elements = inputs[1:size + 1]
    if size != len(elements):
        print("Error: The number of elements does not match the specified size.")
        return
    print("Created list:", elements)
create_and_display_list()
'''
Enter the size followed by the list elements: 5 10 20 30 40 50
Created list: [10, 20, 30, 40, 50]
