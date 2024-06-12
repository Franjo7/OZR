print("\n")
print("VJEŽBE - 03 \n")
print("LAGRANGEOV POLINOM \n")

# ZADATAK SA PREDAVANJA (Interpolacija - Lagrangeov polinom)
# Odredite interpolacijski polinom ako su zadani uvjeti: p(0) = 3, p(2) = 4, p(4) = 2. 
# Potrebno je riješiti sustav: | 1  0  0  | | a0 |   | 3 |
#                              | 1  2  4  | | a1 | = | 4 | 
#                              | 1  4  16 | | a2 |   | 2 |
# Sustav je regularan i ima jedinstveno rješenje.

print("ZADATAK SA PREDAVANJA (Interpolacija - Lagrangeov polinom)")

from numpy import *
from numpy import linalg as l
from numpy.polynomial import polynomial as p

A = array([[1, 0, 0], [1, 2, 4], [1, 4, 16]])
b = array([3, 4, 2])

rjesenje = l.solve(A, b)
print("Koeficijenti polinoma su:", rjesenje)                                        # Koeficijenti polinoma su: [ 3.  1.25  -0.375]
print("Čvor je 0, a vrijednost polinoma u čvoru je:", p.polyval(0, rjesenje))       # Čvor je 0, a vrijednost polinoma u čvoru je: 3.0
print("Čvor je 2, a vrijednost polinoma u čvoru je:", p.polyval(2, rjesenje))       # Čvor je 2, a vrijednost polinoma u čvoru je: 4.0
print("Čvor je 4, a vrijednost polinoma u čvoru je:", p.polyval(4, rjesenje))       # Čvor je 4, a vrijednost polinoma u čvoru je: 2.0

print("\n")





# PRVI ZADATAK
# Konstruirajte i nacrtajte interpolacijski polinom koji zadovoljava uvjete:
# p(0) = 1; p(2) = 2; p(4) = 3

print("PRVI ZADATAK")

from numpy import *
from numpy import linalg as l
from numpy.polynomial import polynomial as p

A = array([[1, 0, 0], [1, 2, 4], [1, 4, 16]])
b = array([1, 2, 3])

rjesenje = l.solve(A, b)
print("Koeficijenti polinoma su:", rjesenje)                                        # Koeficijenti polinoma su: [ 1.  0.5  -0]
print("Čvor je 0, a vrijednost polinoma u čvoru je:", p.polyval(0, rjesenje))       # Čvor je 0, a vrijednost polinoma u čvoru je: 1.0
print("Čvor je 2, a vrijednost polinoma u čvoru je:", p.polyval(2, rjesenje))       # Čvor je 2, a vrijednost polinoma u čvoru je: 2.0
print("Čvor je 4, a vrijednost polinoma u čvoru je:", p.polyval(4, rjesenje))       # Čvor je 4, a vrijednost polinoma u čvoru je: 3.0

print("\n")





# DRUGI ZADATAK
# Konstruirajte i nacrtajte interpolacijski polinom koji zadovoljava uvjete:
# p(1) = 1; p'(1) = 2; p(4) = 3

print("DRUGI ZADATAK")

from numpy import *
from numpy import linalg as l
from numpy.polynomial import polynomial as p

A = array([[1, 1, 1], [0, 1, 2], [1, 4, 16]])
b = array([1, 2, 3])

rjesenje = l.solve(A, b)
print("Koeficijenti polinoma su:", rjesenje)                                        
# Koeficijenti polinoma su: [-1.44444444  2.88888889 -0.44444444]

print("Čvor je 1, a vrijednost polinoma u čvoru je:", p.polyval(1, rjesenje).round(2))       
# Čvor je 1, a vrijednost polinoma u čvoru je: 1.0

print("Čvor je 1 (prva derivacija), a vrijednost polinoma u čvoru je:", p.polyval(1, p.polyder(rjesenje)).round(2))
# Čvor je 1 (prva derivacija), a vrijednost polinoma u čvoru je: 2.0

print("Čvor je 4, a vrijednost polinoma u čvoru je:", p.polyval(4, rjesenje).round(2))
# Čvor je 4, a vrijednost polinoma u čvoru je: 3.0

print("\n")





# TREĆI ZADATAK
# Konstruirajte i nacrtajte polinom koji interpolira vrijednosti funkcije i prve derivacije funkcije sin(x) u čvorovima 0 i π.

print("TREĆI ZADATAK")

from numpy import *
from numpy import linalg as l
from numpy.polynomial import polynomial as p

A = array([[1, 0, 0, 0], [0, 1, 0, 0], [1, pi, pi**2, pi**3], [0, 1, 2*pi, 3*pi**2]])
b = array([sin(0), cos(0), sin(pi), cos(pi)])

rjesenje = l.solve(A, b)
print("Koeficijenti polinoma su:", rjesenje)                                     
# Koeficijenti polinoma su: [ 0.          1.         -0.31830989  0.        ]

print("Vrijednost funkcije:", sin(0), ", vrijednost polinoma:", p.polyval(0, rjesenje))
# Vrijednost funkcije: 0.0 , vrijednost polinoma: 0.0

print("Vrijednost funkcije:", sin(pi), ", vrijednost polinoma:", p.polyval(pi, rjesenje))
# Vrijednost funkcije: 1.2246467991473532e-16 , vrijednost polinoma: 0.0

print("Vrijednost derivacije funkcije:", cos(0), ", vrijednost derivacije polinoma:", p.polyval(0, p.polyder(rjesenje)))
# Vrijednost derivacije funkcije: 1.0 , vrijednost derivacije polinoma: 1.0

print("Vrijednost derivacije funkcije:", cos(pi), ", vrijednost derivacije polinoma:", p.polyval(pi, p.polyder(rjesenje)))
# Vrijednost derivacije funkcije: -1.0 , vrijednost derivacije polinoma: -1.0

print("\n")





# ČETVRTI ZADATAK
# Aproksimirajte Lagrangeovim polinomom funkciju x * e ^ x. 
# Interpolirajte funkciju u čvorovima 1, 2, 3 i izračunajte relativnu pogrešku aproksimacije u čvoru 1.5.

print("ČETVRTI ZADATAK")

from numpy import *
import pylab as py

def l_0(x, x0, x1, x2):
    return (x - x1) * (x - x2) / ((x0 - x1) * (x0 - x2))

def l_1(x, x0, x1, x2):
    return (x - x0) * (x - x2) / ((x1 - x0) * (x1 - x2))

def l_2(x, x0, x1, x2):
    return (x - x0) * (x - x1) / ((x2 - x0) * (x2 - x1))

def x_os(x):
    return 0 * x

def f(x):
    return x * exp(x)

def lagrangeov_polinom(x, x0, x1, x2):
    return f(x0) * l_0(x, x0, x1, x2) + f(x1) * l_1(x, x0, x1, x2) + f(x2) * l_2(x, x0, x1, x2)

# Provjera
print("Vrijednost funkcije u čvoru 1:", f(1), ", vrijednost polinoma u čvoru 1:", lagrangeov_polinom(1, 1, 2, 3), ", apsolutna pogreška:", abs(f(1) - lagrangeov_polinom(1, 1, 2, 3)))
# Vrijednost funkcije u čvoru 1: 2.718281828459045 , vrijednost polinoma u čvoru 1: 2.718281828459045 , apsolutna pogreška: 0.0

print("Vrijednost funkcije u čvoru 2:", f(2), ", vrijednost polinoma u čvoru 2:", lagrangeov_polinom(2, 1, 2, 3), ", apsolutna pogreška:", abs(f(2) - lagrangeov_polinom(2, 1, 2, 3)))
# Vrijednost funkcije u čvoru 2: 14.7781121978613 , vrijednost polinoma u čvoru 2: 14.7781121978613 , apsolutna pogreška: 0.0

print("Vrijednost funkcije u čvoru 3:", f(3), ", vrijednost polinoma u čvoru 3:", lagrangeov_polinom(3, 1, 2, 3), ", apsolutna pogreška:", abs(f(3) - lagrangeov_polinom(3, 1, 2, 3)))
# Vrijednost funkcije u čvoru 3: 60.256610769563004 , vrijednost polinoma u čvoru 3: 60.256610769563004 , apsolutna pogreška: 0.0

# Relativna pogreška u čvoru 1.5
apsolutna_pogreska = abs(f(1.5) - lagrangeov_polinom(1.5, 1, 2, 3))
relativna_pogreska = apsolutna_pogreska / f(1.5)

print("Apsolutna pogreška u čvoru 1.5:", apsolutna_pogreska)
# Apsolutna pogreška u čvoru 1.5: 2.151670117634356

print("Relativna pogreška u čvoru 1.5:", relativna_pogreska)
# Relativna pogreška u čvoru 1.5: 0.32006833195622975

# Crtanje
x_domena = linspace(0, 4, 1000)
py.plot(x_domena, lagrangeov_polinom(x_domena, 1, 2, 3), 'g')
py.plot(x_domena, f(x_domena), 'r')

print("\n")





# PETI ZADATAK
# Nacrtajte grafove Lagrangeovih baza za čvorove 0, 2, 3.

print("PETI ZADATAK")

from numpy import *
import pylab as py

def l_0(x, x0, x1, x2):
    return (x - x1) * (x - x2) / ((x0 - x1) * (x0 - x2))

def l_1(x, x0, x1, x2):
    return (x - x0) * (x - x2) / ((x1 - x0) * (x1 - x2))

def l_2(x, x0, x1, x2):
    return (x - x0) * (x - x1) / ((x2 - x0) * (x2 - x1))

def x_os(x):
    return 0 * x

x_domena = linspace(-1, 4, 1000)
py.plot(x_domena, l_0(x_domena, 0, 2, 3), 'r')
py.plot(x_domena, l_1(x_domena, 0, 2, 3), 'g')
py.plot(x_domena, l_2(x_domena, 0, 2, 3), 'b')
py.plot(x_domena, x_os(x_domena))

print("\n")





# ŠESTI ZADATAK
# Aproksimirajte funkciju 1 / (x ** 2 + 1) na intervalu [-5, 5] upotrebom 
# 5, 10 i 20 čvorova. Izračunajte relativnu pogrešku u čvoru 0.6.

print("ŠESTI ZADATAK")

from numpy import *
import pylab as py
from scipy import interpolate as i

def f(x):
    return 1 / (x ** 2 + 1)

# 5 čvorova
x_5 = linspace(-5, 5, 5)
baricentrični_lagrangeov_polinom_4 = i.BarycentricInterpolator(x_5, f(x_5))

# 10 čvorova
x_10 = linspace(-5, 5, 10)
baricentrični_lagrangeov_polinom_9 = i.BarycentricInterpolator(x_10, f(x_10))

# 20 čvorova
x_20 = linspace(-5, 5, 20)
baricentrični_lagrangeov_polinom_19 = i.BarycentricInterpolator(x_20, f(x_20))

x_domena = linspace(-5, 5, 1000)
py.plot(x_domena, f(x_domena), 'r')
py.plot(x_domena, baricentrični_lagrangeov_polinom_4(x_domena), 'y')
py.plot(x_domena, baricentrični_lagrangeov_polinom_9(x_domena), 'g')
py.plot(x_domena, baricentrični_lagrangeov_polinom_19(x_domena), 'b')

apsolutna_pogreska_5 = abs(f(0.6) - baricentrični_lagrangeov_polinom_4(0.6))
relativna_pogreska_5 = apsolutna_pogreska_5 / abs(f(0.6))
apsolutna_pogreska_10 = abs(f(0.6) - baricentrični_lagrangeov_polinom_9(0.6))
relativna_pogreska_10 = apsolutna_pogreska_10 / abs(f(0.6))
apsolutna_pogreska_20 = abs(f(0.6) - baricentrični_lagrangeov_polinom_19(0.6))
relativna_pogreska_20 = apsolutna_pogreska_20 / abs(f(0.6))

print("Relativna pogreška u čvoru 0.6 (5 čvorova):", relativna_pogreska_5)
# Relativna pogreška u čvoru 0.6 (5 čvorova): 0.2771705888594163

print("Relativna pogreška u čvoru 0.6 (10 čvorova):", relativna_pogreska_10)
# Relativna pogreška u čvoru 0.6 (10 čvorova): 0.018394570338619347

print("Relativna pogreška u čvoru 0.6 (20 čvorova):", relativna_pogreska_20)
# Relativna pogreška u čvoru 0.6 (20 čvorova): 0.007542558242136206