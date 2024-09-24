'''
Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
'''
def calculate_mean():
    inputs = list(map(int, input("Enter the size followed by the array elements: ").split()))
    n = inputs[0]
    if n > 20:
        print("Error: The maximum number of elements is 20.")
        return
    elements = inputs[1:n + 1]
    if n != len(elements):
        print("Error: The number of elements does not match the specified size.")
        return
    total_sum = sum(elements)
    mean = total_sum / n if n > 0 else 0  # Avoid division by zero
    print(f"Mean of the array: {mean:.2f}")
calculate_mean()
'''
Enter the size followed by the array elements: 1 5 6 2 8 9 8 3
Mean of the array: 5.00
