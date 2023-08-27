import numpy as np

def main():
    """
    This is the main function that runs the code.
    """
    # Create a 2D array using numpy
    A = np.array([
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ])

    # Print the first two columns of array A
    print(A[:, :2])

    # Print the first two rows of array A
    print(A[:2, :])

    # Print the 2x3 sub-array from array A
    print(A[:2, :3])


    # Create an array using numpy's arange function
    a = np.arange(5)

    # Add 20 to each element in array a
    print(a + 20)

    # Check if each element in array a is less than or equal to 3
    print(a <= 3)

if __name__ == "__main__":
    main()
