import sys, os
from generowanie import *

sys.path.append(os.path.join(os.path.dirname(__file__), 'sortowanie'))
                
from sortowanie.shell_sort import *
from sortowanie.quick_sort import *
from sortowanie.insertion_sort import *
from sortowanie.selection_sort import *

m = int(input("Podaj długość zbioru: "))

generators = ["random_array", "ascending", "descending", "constant", "a_shaped"]

while True:
    generator = str(input("Wybierz generator (random_array, ascending, descending, constant, a_shaped): "))
    if generator in generators: break
    else: print("Podany zły generator, spróbuj ponownie")

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

arr = s
pom1 = arr

print("Przed sortowaniem: ", s)

print("Po sortowaniu: ", shell_sort(s))

print("Po sortowaniu: ", insertion_sort(s))         #algorytm insertion sort

print("Po sortowaniu: ", selection_sort(s))         #algorytm selection sort

quick_sort(arr, 0, len(arr) - 1, pivot_choice="left")       
print("Po sortowaniu z pivota lewego:", arr)

arr = pom1

quick_sort(arr, 0, len(arr) - 1, pivot_choice="random")
print("Po sortowaniu z pivota losowego:", arr)



