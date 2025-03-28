import random
import sys

sys.setrecursionlimit(10**6) 

def partition_left(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


def quick_sort_with_left_pivot(arr, low, high, pivot_choice="left"):
    if low < high:
        pivot_index = partition_left(arr, low, high)
        quick_sort_with_left_pivot(arr, low, pivot_index - 1, pivot_choice)
        quick_sort_with_left_pivot(arr, pivot_index + 1, high, pivot_choice)

def quick_sort_left_pivot(arr):
    pom1 = arr
    quick_sort_with_left_pivot(pom1, 0, len(pom1) - 1, pivot_choice="left")
    return pom1