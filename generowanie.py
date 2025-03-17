from random import *

def random_array(n):
    return [randint(1, n) for _ in range(n)]

def ascending(n):
    return list(range(n))

def descending(n):
    return list(range(n-1, -1, -1))

def constant(n):
    return [n] * n

def a_shaped(n):
    mid = (n + 1) // 2
    ascending = list(range(1, mid + 1))
    descending = list(range(n, mid, -1))
    return ascending + descending
