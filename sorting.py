import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__), 'sortowanie'))

from sortowanie.heap_sort import *
from sortowanie.insertion_sort import *
from sortowanie.selection_sort import *
from sortowanie.shell_sort import *

def sort_using_algorithm(data, algorithm):
    # This function takes the algorithm identifier as input
    # However, it always uses the sorted function in Python

    if algorithm == 1:
        sorted_data = insertion_sort(data)
    elif algorithm == 2:
        sorted_data = shell_sort(data)
    elif algorithm == 3:
        sorted_data = selection_sort(data)
    elif algorithm == 4:
        sorted_data = heap_sort(data)
    else:
        sorted_data = sorted(data)
    return sorted_data

def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data[0:10])

if __name__ == "__main__":
    main()
