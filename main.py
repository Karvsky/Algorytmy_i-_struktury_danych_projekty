import sys, os
from generowanie import *

sys.path.append(os.path.join(os.path.dirname(__file__), 'sortowanie'))
                
from sortowanie.shell_sort import *

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


