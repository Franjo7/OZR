print("\n")
print("VJEŽBE - 04 \n")

# PRVI ZADATAK
# Aproksimirajte Lagrangeovim polinomom funkciju (x ** 2) * (e ** x).
# Interpolirajte funkciju u čvorovima 0, 2 i 3 i izračunajte apsolutnu pogrešku aproksimacije u čvoru 1
# i usporedite sa teorijskom ocjenom pogreške interpolacijskog polinoma.

print("PRVI ZADATAK")

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

def fun(x):
    return x ** 2 * exp(x)

def lagrangeov_polinom(x, x0, x1, x2):
    return fun(x0) * l_0(x, x0, x1, x2) + fun(x1) * l_1(x, x0, x1, x2) + fun(x2) * l_2(x, x0, x1, x2)

print("Vrijednost funkcije u čvoru 0:", fun(0), ", vrijednost polinoma u čvoru 0:", lagrangeov_polinom(0, 0, 2, 3), ", apsolutna pogreška:", abs(fun(0) - lagrangeov_polinom(0, 0, 2, 3)))
# Vrijednost funkcije u čvoru 0: 0.0 , vrijednost polinoma u čvoru 0: 0.0 , apsolutna pogreška: 0.0

print("Vrijednost funkcije u čvoru 2:", fun(2), ", vrijednost polinoma u čvoru 2:", lagrangeov_polinom(2, 0, 2, 3), ", apsolutna pogreška:", abs(fun(2) - lagrangeov_polinom(2, 0, 2, 3)))
# Vrijednost funkcije u čvoru 2: 29.5562243957226 , vrijednost polinoma u čvoru 2: 29.5562243957226 , apsolutna pogreška: 0.0

print("Vrijednost funkcije u čvoru 3:", fun(3), ", vrijednost polinoma u čvoru 3:", lagrangeov_polinom(3, 0, 2, 3), ", apsolutna pogreška:", abs(fun(3) - lagrangeov_polinom(3, 0, 2, 3)))
# Vrijednost funkcije u čvoru 3: 180.76983230868902 , vrijednost polinoma u čvoru 3: 180.76983230868902 , apsolutna pogreška: 0.0

apsolutna_pogreska = abs(fun(1) - lagrangeov_polinom(1, 0, 2, 3))
print("Apsolutna pogreška u čvoru 1:", apsolutna_pogreska)
# Apsolutna pogreška u čvoru 1: 33.41866820229945

relativna_pogreska = apsolutna_pogreska / abs(fun(1))
print("Relativna pogreška u čvoru 1:", relativna_pogreska)
# Relativna pogreška u čvoru 1: 12.29404098295577

x_domena = linspace(-1, 4, 1000)
py.plot(x_domena, lagrangeov_polinom(x_domena, 0, 2, 3), 'g')
py.plot(x_domena, fun(x_domena), 'r')

print("\n")





# DRUGI ZADATAK
# Formirajte Newtonov interpolacijski polinom koji zadovoljava uvjete:
# p(0) = -1, p(2) = 2, p(6) = 3

print("DRUGI ZADATAK")

from numpy import *
import pylab as py

x = [0, 2, 6]                           # čvorovi
f = zeros([3, 3])                       # matrica podijeljenih razlika

f[0][0] = -1
f[1][0] = 2
f[2][0] = 3

f[0, 1] = (f[1, 0] - f[0, 0]) / (x[1] - x[0])
f[1, 1] = (f[2, 0] - f[1, 0]) / (x[2] - x[1])

f[0, 2] = (f[1, 1] - f[0, 1]) / (x[2] - x[0])

def newtonov_polinom(x_d, x, f):
    return f[0, 0] + (x_d - x[0]) * f[0, 1] + (x_d - x[0]) * (x_d - x[1]) * f[0, 2]

print("Vrijednost polinoma u čvoru 0:", newtonov_polinom(0, x, f))
# Vrijednost polinoma u čvoru 0: -1.0

print("Vrijednost polinoma u čvoru 2:", newtonov_polinom(2, x, f))
# Vrijednost polinoma u čvoru 2: 2.0

print("Vrijednost polinoma u čvoru 6:", newtonov_polinom(6, x, f))
# Vrijednost polinoma u čvoru 6: 3.0

py.plot(x, [-1, 2, 3], 'o')

x_domena = linspace(-1, 7, 1000)
py.plot(x_domena, newtonov_polinom(x_domena, x, f), 'r')

print("\n")





# TREĆI ZADATAK
# Formirajte Newtonov interpolacijski polinom koji interpolira funkciju e ** x u čvorovima 2, 3 i 5
# i ocijenite globalnu pogrešku na intervalu.

print("TREĆI ZADATAK")

from numpy import *
import pylab as py

x = [2, 3, 5]                           
f = zeros([3, 3])

def fun(x):
    return exp(x)

f[0, 0] = fun(x[0])
f[1, 0] = fun(x[1])
f[2, 0] = fun(x[2])

f[0, 1] = (f[1, 0] - f[0, 0]) / (x[1] - x[0])
f[1, 1] = (f[2, 0] - f[1, 0]) / (x[2] - x[1])

f[0, 2] = (f[1, 1] - f[0, 1]) / (x[2] - x[0])

def newtonov_polinom(x_d, x, f):
    return f[0, 0] + (x_d - x[0]) * f[0, 1] + (x_d - x[0]) * (x_d - x[1]) * f[0, 2]

print("Vrijednost polinoma u čvoru 2:", newtonov_polinom(x[0], x, f), ", vrijednost funkcije u čvoru 2:", fun(x[0]))
# Vrijednost polinoma u čvoru 2: 7.38905609893065 , vrijednost funkcije u čvoru 2: 7.38905609893065

print("Vrijednost polinoma u čvoru 3:", newtonov_polinom(x[1], x, f), ", vrijednost funkcije u čvoru 3:", fun(x[1]))
# Vrijednost polinoma u čvoru 3: 20.085536923187668 , vrijednost funkcije u čvoru 3: 20.085536923187668

print("Vrijednost polinoma u čvoru 5:", newtonov_polinom(x[2], x, f), ", vrijednost funkcije u čvoru 5:", fun(x[2]))
# Vrijednost polinoma u čvoru 5: 148.4131591025766 , vrijednost funkcije u čvoru 5: 148.4131591025766

py.plot(x, fun(x), 'o')
x_domena = linspace(-1, 7, 1000)
py.plot(x_domena, fun(x_domena), 'g')
py.plot(x_domena, newtonov_polinom(x_domena, x, f), 'r')

print("\n")





# ČETVRTI ZADATAK
# Aproksimirajte funkciju 1 / 1 + 5 * x ** 2 na intervalu [-1, 1] upotrebom 
# 5, 10 i 20 čvorova. Izračunajte relativnu pogrešku u čvoru 0.95.

print("ČETVRTI ZADATAK")

from numpy import *
import pylab as py
from scipy import interpolate as i 

def fun(x):
    return 1 / (1 + 5 * x ** 2)

x = linspace(-1, 1, 5)
Interpolacijski_polinom_5 = i.BarycentricInterpolator(x, fun(x))

x = linspace(-1, 1, 10)
Interpolacijski_polinom_10 = i.BarycentricInterpolator(x, fun(x))

x = linspace(-1, 1, 20)
Interpolacijski_polinom_20 = i.BarycentricInterpolator(x, fun(x))

x_int = linspace(-1, 1, 1000)
py.plot(x_int, fun(x_int), 'r')
py.plot(x_int, Interpolacijski_polinom_5(x_int), 'y')
py.plot(x_int, Interpolacijski_polinom_10(x_int), 'g')
py.plot(x_int, Interpolacijski_polinom_20(x_int), 'b')

print("Relativna pogreška u čvoru 0.95 za 5 čvorova:", abs(fun(0.95) - Interpolacijski_polinom_5(0.95)) / fun(0.95))
# Relativna pogreška u čvoru 0.95 za 5 čvorova: 0.5316289062500005

print("Relativna pogreška u čvoru 0.95 za 10 čvorova:", abs(fun(0.95) - Interpolacijski_polinom_10(0.95)) / fun(0.95))
# Relativna pogreška u čvoru 0.95 za 10 čvorova: 0.3739423048599579

print("Relativna pogreška u čvoru 0.95 za 20 čvorova:", abs(fun(0.95) - Interpolacijski_polinom_20(0.95)) / fun(0.95))
# Relativna pogreška u čvoru 0.95 za 20 čvorova: 0.3783203995088997

print("\n")