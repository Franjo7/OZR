print("\n")
print("VJEŽBE - 07 \n")

print("Zadatke riješiti upotrebom odgovarajuće Newton-Cotesove formule.")
print("\n")

# PRVI ZADATAK
# Upotrebom trapezne formule izračunajte integral funkcije f(x) = (e ** x) * dx na intervalu [0, 3].
# Ocijenite pogrešku aproksimacije i izračunajte stvarnu pogrešku.

print("PRVI ZADATAK")

from numpy import *

def trapezna_formula(a, b, f): 
    return (b - a) * (f(a) + f(b)) / 2

a = 0
b = 3
f = lambda x: exp(x)

integral = trapezna_formula(a, b, f)
print("Integral funkcije preko trapezne formule:", integral) 
# Integral funkcije preko trapezne formule: 31.628305384781502

integral_prava_vrijednost = exp(3) - exp(0)
print("Prava vrijednost integrala:", integral_prava_vrijednost)
# Prava vrijednost integrala: 19.085536923187668

stvarna_apsolutna_pogreska = abs(integral - integral_prava_vrijednost)
print("Stvarna apsolutna pogreška:", stvarna_apsolutna_pogreska)
# Stvarna apsolutna pogreška: 12.542768461593834

M = exp(3)                                                              # maksimum druge derivacije podintegralne funkcije
ocjena_pogreske = abs((b - a) ** 3) * M / 12
print("Ocjena pogreške:", ocjena_pogreske)
# Ocjena pogreške: 45.192458077172255

print("\n")





# DRUGI ZADATAK
# Upotrebom trapezne formule izračunajte integral funkcije f(x) = (x ** 2 + x) * dx na intervalu [0, 3].
# Ocijenite pogrešku aproksimacije i izračunajte stvarnu pogrešku.
# Referentno rješenje je b ** 3 / 3 + b ** 2 / 2 - (a ** 3 / 3 + a ** 2 / 2)

print("DRUGI ZADATAK")

from numpy import *

def trapezna_formula(a, b, f):
    return (b - a) * (f(a) + f(b)) / 2

a = 0
b = 3
f = lambda x: x ** 2 + x

integral = trapezna_formula(a, b, f)
print("Integral funkcije preko trapezne formule:", integral)
# Integral funkcije preko trapezne formule: 18.0

integral_prava_vrijednost = b ** 3 / 3 + b ** 2 / 2 - (a ** 3 / 3 + a ** 2 / 2)
print("Prava vrijednost integrala:", integral_prava_vrijednost)
# Prava vrijednost integrala: 13.5

stvarna_apsolutna_pogreska = abs(integral_prava_vrijednost - integral)
print("Stvarna apsolutna pogreška:", stvarna_apsolutna_pogreska) 
# Stvarna apsolutna pogreška: 4.5

M = 2                                                                   # f''(x) = 2
ocjena_pogreske = abs((b - a) ** 3) * M / 12
print("Ocjena pogreške:", ocjena_pogreske)
# Ocjena pogreške: 4.5

print("\n")





# TREĆI ZADATAK
# Upotrebom Simpsonove formule izračunajte integral funkcije f(x) = (e ** x) * dx na intervalu [0, 3].
# Ocijenite pogrešku aproksimacije i izračunajte stvarnu pogrešku.

print("TREĆI ZADATAK")

from numpy import *

def simpsonova_formula(a, b, f):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

a = 0
b = 3
f = lambda x: exp(x)

integral = simpsonova_formula(a, b, f)
print("Integral funkcije preko Simpsonove formule:", integral)
# Integral funkcije preko Simpsonove formule: 19.506146602269965

integral_prava_vrijednost = exp(3) - exp(0)
print("Prava vrijednost integrala:", integral_prava_vrijednost)
# Prava vrijednost integrala: 19.085536923187668

stvarna_apsolutna_pogreska = abs(integral - integral_prava_vrijednost)
print("Stvarna apsolutna pogreška:", stvarna_apsolutna_pogreska)
# Stvarna apsolutna pogreška: 0.42060967908229685

M = exp(3)                                                              # maksimum četvrte derivacije podintegralne funkcije
ocjena_pogreske = abs((b - a) ** 5) * M / 2880
print("Ocjena pogreške:", ocjena_pogreske)
# Ocjena pogreške: 1.6947171778939596

print("\n")





# ČETVRTI ZADATAK
# Upotrebom Simpsonove formule izračunajte integral funkcije f(x) = (x ** 2 - x + 1) * dx na intervalu [1, 3].
# Ocijenite pogrešku aproksimacije i izračunajte stvarnu pogrešku.
# Referentno rješenje pronađite Gaussovom kvadraturnom formulom.

print("ČETVRTI ZADATAK")

from numpy import *
from scipy import integrate as i

def simpsonova_formula(a, b, f):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

a = 1
b = 3
f = lambda x: x ** 2 - x + 1

integral = simpsonova_formula(a, b, f)
print("Integral funkcije preko Simpsonove formule:", integral)
# Integral funkcije preko Simpsonove formule: 6.666666666666666

integral_prava_vrijednost = i.quad(f, a, b)[0]
print("Prava vrijednost integrala:", integral_prava_vrijednost)
# Prava vrijednost integrala: 6.666666666666668

stvarna_apsolutna_pogreska = abs(integral - integral_prava_vrijednost)
print("Stvarna apsolutna pogreška:", stvarna_apsolutna_pogreska)
# Stvarna apsolutna pogreška: 1.7763568394002505e-15

M = 0                                                               # maksimum četvrte derivacije podintegralne funkcije
ocjena_pogreske = abs((b - a) ** 5) * M / 2880
print("Ocjena pogreške:", ocjena_pogreske)
# Ocjena pogreške: 0.0

print("\n")





# PETI ZADATAK
# Upotrebom Simpsonove formule izračunajte integral funkcije f(x) = (x ** 3 + x) * dx na intervalu [0, 2].
# Ocijenite pogrešku aproksimacije i izračunajte stvarnu pogrešku.
# Referentno rješenje je b ** 4 / 4 + b ** 2 / 2 - (a ** 4 / 4 + a ** 2 / 2)

print("PETI ZADATAK")

from numpy import *

def simpsonova_formula(a, b, f):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

a = 0
b = 2
f = lambda x: x ** 3 + x

integral = simpsonova_formula(a, b, f)
print("Integral funkcije preko Simpsonove formule:", integral)
# Integral funkcije preko Simpsonove formule: 6.0

integral_prava_vrijednost = b ** 4 / 4 + b ** 2 / 2 - (a ** 4 / 4 + a ** 2 / 2)
print("Prava vrijednost integrala:", integral_prava_vrijednost)
# Prava vrijednost integrala: 6.0

stvarna_apsolutna_pogreska = abs(integral - integral_prava_vrijednost)
print("Stvarna apsolutna pogreška:", stvarna_apsolutna_pogreska)
# Stvarna apsolutna pogreška: 0.0

M = 0                                                               # maksimum četvrte derivacije podintegralne funkcije
ocjena_pogreske = abs((b - a) ** 5) * M / 2880
print("Ocjena pogreške:", ocjena_pogreske)
# Ocjena pogreške: 0.0

print("\n")





# ŠESTI ZADATAK
# Upotrebom produljene trapezne formule izračunajte integral funkcije f(x) = sin(x) * dx na intervalu [1, 3], 
# s točnošću od 10 ** (-5). Koliko je intervala dovoljno koristiti?
# Referentno rješenje pronađite Gaussovom kvadraturnom formulom.

print("ŠESTI ZADATAK")

from numpy import *
from scipy import integrate as i

a = 1
b = 3
f = lambda x: sin(x)
epsilon = 1.e-5

M = abs(sin(pi / 2))                                               # maksimum druge derivacije podintegralne funkcije
n = sqrt((b - a) ** 3 * M / (12 * epsilon))

print("Broj intervala:", n)
# Broj intervala: 258.1988897471611

n = 259                                                            # broj intervala mora biti cijeli broj, zaokružujemo na veći
print("Dovoljno je koristiti", n, "intervala.")
# Dovoljno je koristiti 259 intervala.

x = linspace(a, b, n + 1)                                          # broj čvorova je n + 1

produljena_trapezna_formula = i.trapezoid(f(x), x)
print("Integral funkcije preko produljene trapezne formule:", produljena_trapezna_formula)
# Integral funkcije preko produljene trapezne formule: 1.5302871982472044

integral_prava_vrijednost = i.quad(f, a, b)[0]
print("Prava vrijednost integrala:", integral_prava_vrijednost)
# Prava vrijednost integrala: 1.530294802468585

stvarna_apsolutna_pogreska = abs(produljena_trapezna_formula - integral_prava_vrijednost)
print("Stvarna apsolutna pogreška:", stvarna_apsolutna_pogreska)
# Stvarna apsolutna pogreška: 7.604221380574927e-06

print("\n")





# SEDMI ZADATAK
# Upotrebom produljene Simpsonove formule izračunajte integral funkcije f(x) = sin(x) * dx na intervalu [1, 3],
# s točnošću od 10 ** (-5). Koliko je intervala dovoljno koristiti?
# Referentno rješenje pronađite Gaussovom kvadraturnom formulom.

print("SEDMI ZADATAK")

from numpy import *
from scipy import integrate as i

a = 1
b = 3
f = lambda x: sin(x)
epsilon = 1.e-5

M = abs(sin(pi / 2))                                               # maksimum četvrte derivacije podintegralne funkcije
n = (((b - a) ** 5 * M) / (180 * epsilon)) ** (1 / 4)

print("Broj intervala:", n)
# Broj intervala: 11.547005383792515

n = 12
print("Prvi parni broj koji zadovoljava uvjet je:", n)
# Prvi parni broj koji zadovoljava uvjet je: 12

x = linspace(a, b, n + 1)            

produljena_simpsonova_formula = i.simpson(f(x), x)
print("Integral funkcije preko produljene Simpsonove formule:", produljena_simpsonova_formula)
# Integral funkcije preko produljene Simpsonove formule: 1.530301384130549

integral_prava_vrijednost = i.quad(f, a, b)[0]
print("Prava vrijednost integrala:", integral_prava_vrijednost)
# Prava vrijednost integrala: 1.530294802468585

stvarna_apsolutna_pogreska = abs(produljena_simpsonova_formula - integral_prava_vrijednost)
print("Stvarna apsolutna pogreška:", stvarna_apsolutna_pogreska)
# Stvarna apsolutna pogreška: 6.5816619641001495e-06

print("\n")