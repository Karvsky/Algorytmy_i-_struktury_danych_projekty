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

while True:
    print("----Program sortujący---- \n-------------------------\n")
    m = input("Podaj długość zbioru: ")
    try:
        m = int(m)
        break 
    except ValueError:
        os.system('clear')
        print("To nie jest poprawna liczba całkowita. Spróbuj ponownie.\n")
        continue 

os.system('clear')
generators = ["1", "2", "3", "4", "5"]

while True:
    print("----Program sortujący---- \n-------------------------\n")
    generator = str(input("Wybierz generator: \nrandom_array - 1\nascending - 2\ndescending - 3\nconstant - 4\na_shaped - 5\n"))
    if generator in generators: break
    else: 
        os.system('clear')
        print("Podany zły generator, spróbuj ponownie\n")

os.system('clear')

while True:
    print("----Program sortujący---- \n-------------------------\n")
    sort = str(input("Wybierz algorytm sortujący: \nshell sort - 1\ninsertion sort - 2\nselection sort - 3\nheap sort - 4\nquick sort left pivot - 5\nquick sort random pivot - 6\n"))
    if sort in ["1", "2", "3", "4", "5", "6"]: break
    else: 
        os.system('clear')
        print("Podany zły algorytm, spróbuj ponownie\n")

if generator == "1":
    s = random_array(m)
elif generator == "2":
    s = ascending(m)
elif generator == "3":
    s = descending(m)
elif generator == "4":
    s = constant(m)
elif generator == "5":
    s = a_shaped(m)

os.system('clear')
print("----Program sortujący---- \n-------------------------\n \nPrzed sortowaniem: ", s ,"\n\n-------------------------\n")


if sort == "1":
    print("Posortowany zbiór: ", shell_sort(s))
elif sort == "2":
    print("Posortowany zbiór: ", insertion_sort(s))
elif sort == "3":
    print("Posortowany zbiór: ", selection_sort(s))
elif sort == "4":
    print("Posortowany zbiór: ", heap_sort(s))
elif sort == "5":
    print("Posortowany zbiór: ", quick_sort_left_pivot(s))
elif sort == "6":
    print("Posortowany zbiór: ", quick_sort_random_pivot(s))

