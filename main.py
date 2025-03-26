import sys, os
from generowanie import *

sys.path.append(os.path.join(os.path.dirname(__file__), 'sortowanie'))
                
from sortowanie.shell_sort import *
from sortowanie.insertion_sort import *
from sortowanie.selection_sort import *
from sortowanie.heap_sort import *
from sortowanie.quick_sort_left_pivot import *
from sortowanie.quick_sort_random_pivot import *
os.system('clear')

print("----Program sortujący---- \n-------------------------\n")
m = int(input("Podaj długość zbioru: "))
os.system('clear')
generators = ["random_array", "ascending", "descending", "constant", "a_shaped"]

while True:
    print("----Program sortujący---- \n-------------------------\n")
    generator = str(input("Wybierz generator (random_array, ascending, descending, constant, a_shaped): "))
    if generator in generators: break
    else: print("Podany zły generator, spróbuj ponownie")

os.system('clear')

while True:
    print("----Program sortujący---- \n-------------------------\n")
    sort = str(input("Wybierz algorytm sortujący (shell_sort, insertion_sort, selection_sort, heap_sort, quick_sort_left_pivot, quick_sort_random_pivot): "))
    if sort in ["shell_sort", "insertion_sort", "selection_sort", "heap_sort", "quick_sort_left_pivot", "quick_sort_random_pivot"]: break
    else: print("Podany zły algorytm, spróbuj ponownie")

if generator == "random_array":
    s = random_array(m)
elif generator == "ascending":
    s = ascending(m)
elif generator == "descending":
    s = descending(m)
elif generator == "constant":
    s = constant(m)
elif generator == "a_shaped":
    s = a_shaped(m)

os.system('clear')
print("----Program sortujący---- \n-------------------------\nPrzed sortowaniem: ", s ,"\n")


if sort == "shell_sort":
    print("Posortowany zbiór: ", shell_sort(s))
elif sort == "insertion_sort":
    print("Posortowany zbiór: ", insertion_sort(s))
elif sort == "selection_sort":
    print("Posortowany zbiór: ", selection_sort(s))
elif sort == "heap_sort":
    print("Posortowany zbiór: ", heap_sort(s))
elif sort == "quick_sort_left_pivot":
    print("Posortowany zbiór: ", quick_sort_left_pivot(s))
elif sort == "quick_sort_random_pivot":
    print("Posortowany zbiór: ", quick_sort_random_pivot(s))

