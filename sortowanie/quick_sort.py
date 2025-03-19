import random
import sys

def generuj_tablice(n):
    tablica = [random.randint(-sys.maxsize-1, sys.maxsize) for i in range(n)]
    return tablica

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

def partition_random(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    return partition_left(arr, low, high)

def quick_sort(arr, low, high, pivot_choice="left"):
    if low < high:
        if pivot_choice == "left":
            pivot_index = partition_left(arr, low, high)
        elif pivot_choice == "random":
            pivot_index = partition_random(arr, low, high)
        quick_sort(arr, low, pivot_index - 1, pivot_choice)
        quick_sort(arr, pivot_index + 1, high, pivot_choice)

pom1 = arr

print("Przed sortowaniem:", arr)

quick_sort(arr, 0, len(arr) - 1, pivot_choice="left")
print("Po sortowaniu z pivota lewego:", arr)

arr = pom1

quick_sort(arr, 0, len(arr) - 1, pivot_choice="random")
print("Po sortowaniu z pivota losowego:", arr)
