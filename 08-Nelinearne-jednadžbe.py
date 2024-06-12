print("\n")
print("VJEŽBE - 08 \n")
print("NELINEARNE JEDNADŽBE \n")

# PRVI ZADATAK
# Funkcija f: R -> R, zadana je formulom f(x) = x ** 5 - x ** 3 - 2.
# Odredite broj realnih nultočki funkcije te ih izračunajte sa točnošću 10 ** (-3) koristeći metodu bisekcije.

print("PRVI ZADATAK")

from numpy import *
import pylab as py
from scipy import optimize as o

def f(x):
    return x ** 5 - x ** 3 - 2

def x_os(x):
    return x * 0

x_domena = linspace(-1, 2, 1000)                                    # Imamo jednu nultočku između 1.0 i 1.5
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))

x_domena = linspace(1.34, 1.35, 1000)                               # Uski interval sa nultočkom
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))                       
x_nultocke = o.bisect(f, 1.34, 1.35, xtol = 1.e-3)
print("Nultočka funkcije je:", x_nultocke)                          
# Nultočka funkcije je: 1.3481250000000002
print("Vrijednost funkcije u nultočki je:", f(x_nultocke))          
# Vrijednost funkcije u nultočki je: 0.0028430247232997807

print("\n")





# DRUGI ZADATAK
# Funkcija f: R -> R, zadana je formulom f(x) = 4 * sin(x) - x. 
# Odredite broj realnih nultočki funkcije te ih izračunajte sa točnošću 10 ** (-3) koristeći metodu bisekcije.

print("DRUGI ZADATAK")

from numpy import *
import pylab as py
from scipy import optimize as o

def f(x):
    return 4 * sin(x) - x

def x_os(x):
    return x * 0

x_domena = linspace(-10, 10, 1000)                                   # Imamo tri nultočke                          
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))

# Prva nultočka
x_domena = linspace(-2.48, -2.47, 1000)
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))
x_nultocke_1 = o.bisect(f, -2.48, -2.47, xtol = 1.e-3)
print("Prva nultočka funkcije je:", x_nultocke_1)                    
# Prva nultočka funkcije je: -2.474375
print("Vrijednost funkcije u prvoj nultočki je:", f(x_nultocke_1))
# Vrijednost funkcije u prvoj nultočki je: -0.000835891148718737

# Druga nultočka
x_domena = linspace(-0.0002, 0.0002, 1000)  
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))
x_nultocke_2 = o.bisect(f, -0.0002, 0.0002, xtol = 1.e-3)
print("Druga nultočka funkcije je:", x_nultocke_2)                   
# Druga nultočka funkcije je: 0.0
print("Vrijednost funkcije u drugoj nultočki je:", f(x_nultocke_2))
# Vrijednost funkcije u drugoj nultočki je: 0.0

# Treća nultočka
x_domena = linspace(2.474, 2.476, 1000)  
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))
x_nultocke_3 = o.bisect(f, 2.474, 2.476, xtol = 1.e-3)
print("Treća nultočka funkcije je:", x_nultocke_3)                   
# Treća nultočka funkcije je: 2.475
print("Vrijednost funkcije u trećoj nultočki je:", f(x_nultocke_3))
# Vrijednost funkcije u trećoj nultočki je: -0.001753458232602867

print("\n")





# TREĆI ZADATAK
# Odredite najveće realno rješenje jednadžbe ln(x - 1) = ((x ** 3) / 3) - ((2 * (x ** 2)) / 3) - x.
# Rješenje izračunajte sa točnošću 10 ** (-5) koristeći metodu bisekcije. 

print("TREĆI ZADATAK")

from numpy import *
import pylab as py
from scipy import optimize as o

def f(x):
    return log(x - 1) - ((x ** 3) / 3) + ((2 * (x ** 2)) / 3) - x

def x_os(x):
    return x * 0

x_domena = linspace(1.1, 5, 1000)                                   # Nemamo nultočke
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))

print("Jednadžba nema rješenja.")

print("\n")





# ČETVRTI ZADATAK
# Odredite sjecište funkcije e ** x i kružnice x ** 2 + y ** 2 = 4 proizvoljnom metodom.

print("ČETVRTI ZADATAK")

from numpy import *
import pylab as py
from scipy import optimize as o

def f(x):
    return exp(x) - sqrt(4 - x ** 2)

def x_os(x):
    return x * 0

x_domena = linspace(-2, 1, 1000)                                    # Imamo dvije nultočke
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))

# Prva nultočka
x_domena = linspace(-2, -1.98, 1000)
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))
x_nultocke_1 = o.bisect(f, -2, -1.98, xtol = 1.e-11)
print("Prva nultočka funkcije je:", x_nultocke_1)                   
# Prva nultočka funkcije je: -1.9953731700684874
print("Vrijednost funkcije u prvoj nultočki je:", f(x_nultocke_1))
# Vrijednost funkcije u prvoj nultočki je: 7.693559678223494e-11

# Druga nultočka
x_domena = linspace(0.63, 0.64, 1000) 
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))
x_nultocke_2 = o.bisect(f, 0.63, 0.64, xtol = 1.e-11)
print("Druga nultočka funkcije je:", x_nultocke_2)                  
# Druga nultočka funkcije je: 0.6392630748171358
print("Vrijednost funkcije u drugoj nultočki je:", f(x_nultocke_2))
# Vrijednost funkcije u drugoj nultočki je: 1.945976713102482e-11

print("\n")





# PETI ZADATAK
# Funkcija f: R -> R, zadana je formulom f(x) = x ** 5 - x ** 3 - 2.
# Odredite broj realnih nultočki funkcije te ih izračunajte sa točnošću 10 ** (-3) koristeći Newtonovu metodu.

print("PETI ZADATAK")

from numpy import *
import pylab as py
from scipy import optimize as o

def f(x):
    return x ** 5 - x ** 3 - 2

def x_os(x):
    return x * 0

def d1(x):
    return 5 * x ** 4 - 3 * x ** 2

def d2(x):
    return 20 * x ** 3 - 6 * x

x_domena = linspace(-1, 2, 1000)                                    # Imamo jednu nultočku između 1.0 i 1.5
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))

# Nultočka
x_domena = linspace(1.34, 1.35, 1000)                               # Uski interval sa nultočkom
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))
x_pocetna = 1.35                                                    # Naša aproksimacija nultočke
print("Provjera je li umnožak veći od 0:", f(x_pocetna) * d2(x_pocetna))
# Provjera je li umnožak veći od 0: 0.9725392195313034
x_nultocke = o.newton(f, x_pocetna, d1, tol = 1.e-3)
print("Nultočka funkcije je:", x_nultocke)                          
# Nultočka funkcije je: 1.3478678961183042
print("Vrijednost funkcije u nultočki je:", f(x_nultocke))          
# Vrijednost funkcije u nultočki je: 1.4329941677715397e-09

print("\n")





# ŠESTI ZADATAK - prvi dio
# Funkcija f: R -> R, zadana je formulom f(x) = x ** 2 + 4 * sin(x) - 1.
# Odredite broj realnih nultočki funkcije te ih izračunajte sa točnošću 10 ** (-8) koristeći metodu bisekcije.

print("ŠESTI ZADATAK - prvi dio")

from numpy import *
import pylab as py
from scipy import optimize as o

def f(x):
    return x ** 2 + 4 * sin(x) - 1

def x_os(x):
    return x * 0

x_domena = linspace(-3, 2, 1000)                                     # Imamo dvije nultočke                
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))

# Prva nultočka
x_domena = linspace(-2.11, -2.1, 1000)  
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))
x_nultocke_1 = o.bisect(f, -2.11, -2.1, xtol = 1.e-8)
print("Prva nultočka funkcije je:", x_nultocke_1)
# Prva nultočka funkcije je: -2.1068670749664307
print("Vrijednost funkcije u prvoj nultočki je:", f(x_nultocke_1))
# Vrijednost funkcije u prvoj nultočki je: -2.78971010736484e-08

# Druga nultočka
x_domena = linspace(0.23, 0.24, 1000) 
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))
x_nultocke_2 = o.bisect(f, 0.23, 0.24, xtol = 1.e-8)
print("Druga nultočka funkcije je:", x_nultocke_2)
# Druga nultočka funkcije je: 0.23807290077209473
print("Vrijednost funkcije u drugoj nultočki je:", f(x_nultocke_2))
# Vrijednost funkcije u drugoj nultočki je: -7.737912754990361e-09

print("\n")





# ŠESTI ZADATAK - drugi dio
# Funkcija f: R -> R, zadana je formulom f(x) = x ** 2 + 4 * sin(x) - 1.
# Odredite broj realnih nultočki funkcije te ih izračunajte sa točnošću 10 ** (-8) koristeći Newtonovu metodu.

print("ŠESTI ZADATAK - drugi dio")

from numpy import *
import pylab as py
from scipy import optimize as o

def f(x):
    return x ** 2 + 4 * sin(x) - 1

def x_os(x):
    return x * 0

def d1(x):
    return 2 * x + 4 * cos(x)

def d2(x):
    return 2 - 4 * sin(x)

x_domena = linspace(-3, 2, 1000)                                     # Imamo dvije nultočke
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))

# Prva nultočka
x_domena = linspace(-2.11, -2.1, 1000)
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))                                                 
x_pocetna_1 = -2.2   
print("Provjera je li umnožak veći od 0:", f(x_pocetna_1) * d2(x_pocetna_1))
# Provjera je li umnožak veći od 0: 3.1718705722848317
x_nultocke_1 = o.newton(f, x_pocetna_1, d1, tol = 1.e-8)
print("Prva nultočka funkcije je:", x_nultocke_1)
# Prva nultočka funkcije je: -2.106867079425129
print("Vrijednost funkcije u nultočki je:", f(x_nultocke_1))
# Vrijednost funkcije u nultočki je: 8.881784197001252e-16

# Druga nultočka
x_domena = linspace(0.23, 0.24, 1000)
py.plot(x_domena, f(x_domena))
py.plot(x_domena, x_os(x_domena))
x_pocetna_2 = 0.3
print("Provjera je li umnožak veći od 0:", f(x_pocetna_2) * d2(x_pocetna_2))
# Provjera je li umnožak veći od 0: 0.22254012481541904
x_nultocke_2 = o.newton(f, x_pocetna_2, d1, tol = 1.e-8)
print("Druga nultočka funkcije je:", x_nultocke_2)
# Druga nultočka funkcije je: 0.23807290254549382
print("Vrijednost funkcije u nultočki je:", f(x_nultocke_2))
# Vrijednost funkcije u nultočki je: -1.1102230246251565e-16

print("\n")