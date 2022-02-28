#!/bin/env python
n_range = 1000  # Set the proper range
prime_list = []  # Create the empty list to be appended to later.

if __name__ == '__main__':
    for n in range(n_range + 1):  # Go through each number up to and including n_range as n
        if n > 1:
            for i in range(2, n):  # Go through each number up to n as i
                if (n % i) == 0:  # If the remainder of the division is 0, meaning the number is composite
                    break
            else:  # If for loop exits with break statement
                prime_list.append(n)

    print(prime_list)  # Print the resulting list of prime numbers
