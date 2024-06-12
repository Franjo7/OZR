print("\n")
print("VJEŽBE - 01 \n")
print("APSOLUTNA I RELATIVNA GREŠKA \n")

# PRVI ZADATAK (1)
# Zadan je rezultat mjerenja 𝑥 = 20.5 ± 0.7, odredite relativnu grešku.

print("PRVI ZADATAK")

x_x = 20.5
delta_x = 0.7

relativna_greska = delta_x / abs(x_x)                                       # Formula za relativnu grešku
print("Relativna greška je:", round(relativna_greska * 100, 2), "%.")       # Relativna greška je: 3.41 %.
print("\n")





# DRUGI ZADATAK (2)
# Zaokružite broj π na tri decimale, zatim odredite apsolutnu i relativnu grešku aproksimacije.
# Referentna vrijednost je PI iz Math modula.

print("DRUGI ZADATAK")

from math import pi

priblizno_pi = round(pi, 3)                                                 # Zaokružujemo broj π na tri decimale
print("Približno π je:", priblizno_pi)                                      # Približno π je: 3.142

apsolutna_greska = abs(pi - priblizno_pi)                                   # Formula za apsolutnu grešku
relativna_greska = apsolutna_greska / abs(pi)                               # Formula za relativnu grešku

print("Apsolutna greška je:", round(apsolutna_greska, 4))                   # Apsolutna greška je: 0.0004              
print("Relativna greška je:", round(relativna_greska * 100, 3), "%.")       # Relativna greška je: 0.013 %.     
print("\n")





# TREĆI ZADATAK (6)
# Odredite relativnu i apsolutnu grešku pri izračunu vrijednosti funkcije 𝑓(𝑥, 𝑦, 𝑧) = (y𝑥 + 𝑥𝑧) / 𝑧
# ako je 𝑥 = 280 ± 0.2 , 𝑦 = 1011325 ± 20, 𝑧 = 100.
# Derivacija po x = (y + z) / z
# Derivacija po y = x / z

print("TREĆI ZADATAK")

x_x = 280
delta_x = 0.2
y_x = 1011325
delta_y = 20
z_x = 100

apsolutna_greska = abs((y_x + z_x) / z_x) * delta_x + abs(x_x / z_x) * delta_y + 0
relativna_greska = apsolutna_greska / abs((y_x * x_x + x_x * z_x) / z_x)

print("Apsolutna greška je:", round(apsolutna_greska, 2))                        # Apsolutna greška je: 2078.85
print("Relativna greška je:", round(relativna_greska * 100, 2), "%.")            # Relativna greška je: 0.07 %.
print("\n")





# ČETVRTI ZADATAK (5)
# Odredite relativnu i apsolutnu grešku pri izračunu vrijednosti funkcije 𝑓(𝑥, 𝑦, 𝑧) = 2𝑥𝑦 + z^3 * y
# ako je 𝑥 = 8.00 ± 0.1 , 𝑦 = 3.00 ± 0.04 , 𝑧 = 2.40 ± 0.05 .
# Derivacija po x = 2 * y
# Derivacija po y = 2 * x
# Derivacija po z = 3 * z^2

print("ČETVRTI ZADATAK")

x_x = 8.00
delta_x = 0.1
y_x = 3.00
delta_y = 0.04
z_x = 2.40
delta_z = 0.05

apsolutna_greska = abs((2 * y_x) * delta_x + abs(2 * x_x + z_x **3 ) * delta_y + abs(3 * z_x ** 2 * y_x) * delta_z)
relativna_greska = apsolutna_greska / abs(2 * x_x * y_x + z_x ** 3 * y_x)

print("Apsolutna greška je:", round(apsolutna_greska, 2))                       # Apsolutna greška je: 4.38
print("Relativna greška je:", round(relativna_greska * 100, 2), "%.")           # Relativna greška je: 4.9 %.
print("\n")





# PETI ZADATAK (7)
# Odredite apsolutnu i relativnu grešku pri izračunavanju volumena torusa 𝑉 = 2 * 𝑎𝑟^2 * 𝜋^2 koji
# nastaje rotacijom kruga radijusa 𝑟, čije je središte za 𝑎 udaljeno od centra rotacije ako je
# 𝑟 = 20.00 ± 0.2 , 𝑎 = 100 ± 0.5 .

print("PETI ZADATAK")

r_x = 20.00
delta_r = 0.2
a_x = 100
delta_a = 0.5

apsolutna_greska = abs(4 * a_x * r_x * pi ** 2) * delta_r + abs(2 * r_x ** 2 * pi ** 2) * delta_a
relativna_greska = apsolutna_greska / abs(2 * a_x * r_x ** 2 * pi ** 2)

print("Apsolutna greška je:", round(apsolutna_greska, 2))                       # Apsolutna greška je: 19739.21
print("Relativna greška je:", round(relativna_greska * 100, 2), "%.")           # Relativna greška je: 2.5 %.
print("\n")





# ŠESTI ZADATAK (8)
# Izračunajte apsolutnu i relativnu uvjetovanost funkcije 𝑓(𝑥) = ln(𝑥) u okolini točke 𝑥0 = 2.

print("ŠESTI ZADATAK")

from math import *

x0 = 2
apsolutna_uvjetovanost = abs(1 / x0)
relativna_uvjetovanost = abs(1 / log(x0))

print("Apsolutna uvjetovanost je:", apsolutna_uvjetovanost)                     # Apsolutna uvjetovanost je: 0.5
print("Relativna uvjetovanost je:", round(relativna_uvjetovanost, 2))           # Relativna uvjetovanost je: 1.44
print("\n")