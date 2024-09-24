'''
Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
'''
def count_value_occurrences():
    elements = list(map(int, input("Enter the list elements separated by spaces: ").split()))
    value_to_count = int(input("Enter the value to count: "))
    count = elements.count(value_to_count)
    print(f"The value {value_to_count} is repeated {count} times in the list.")
count_value_occurrences()
'''
Enter the list elements separated by spaces: 30 20 54 76 15 36 20 49 20 60 20
Enter the value to count: 20
The value 20 is repeated 4 times in the list.
