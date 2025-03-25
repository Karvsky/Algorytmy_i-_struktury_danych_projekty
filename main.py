import sys, os
from generowanie import *

sys.path.append(os.path.join(os.path.dirname(__file__), 'sortowanie'))
                
from sortowanie.shell_sort import *
from sortowanie.insertion_sort import *
from sortowanie.selection_sort import *
from sortowanie.heap_sort import *
from sortowanie.quick_sort_with_left_pivot import *
from sortowanie.quick_sort_with_random_pivot import *

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

print("Przed sortowaniem: ", s)

print("Po sortowaniu: ", shell_sort(s))

print("Po sortowaniu: ", insertion_sort(s))       

print("Po sortowaniu: ", selection_sort(s))        


quick_sort_left_pivot(s)
a = quick_sort_left_pivot(s)        #sortowanie quick sort z lewym pivotem
print("Po sortowaniu z pivota lewego:", a)

quick_sort_random_pivot(s)
a = quick_sort_random_pivot(s)   #sortowanie quick sort z randomowym pivotem
print("Po sortowaniu z pivota losowego:", a)

print("Po sortowaniu: ", heap_sort(s))




