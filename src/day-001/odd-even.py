#!/bin/env python
n_range = 1000  # Set the number range t o one thousand.
odd_list, even_list = [], []  # Initialize the lists to be appended to later

if __name__ == '__main__':
    for n in range(n_range + 1):  # Go through each number up to and including n_range
        if (n % 2) == 0:  # If the remainder of the division is zero, meaning it is even
            even_list.append(n)  # Append n to the even number list
        else:  # If not
            odd_list.append(n)  # Append n to the odd number list

    print(f"Even:\n{even_list}\nOdd:\n{odd_list}")
