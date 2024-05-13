print("\n")
print("VJEŽBE - 06 \n")

# PRVI ZADATAK
# Neka je zadano pet točaka u ravnini:

# |   x   |   1   |   3   |   4   |   6   |   7   |
# |   y   |   1   |   3   |   2   |   4   |   3   |

# Izračunajte i nacrtajte regresijski pravac.

print("PRVI ZADATAK")

from numpy import *
import pylab as py

x = [1, 3, 4, 6, 7]
y = [1, 3, 2, 4, 3]

py.plot(x, y, 'o')

a = polyfit(x, y, 1)
print("Regresijski pravac:", a)                 # Regresijski pravac: [0.36842105 1.05263158]

def fun(x):
    return a[0] * x + a[1]

x_domena = linspace(0, 8, 100)
py.plot(x_domena, fun(x_domena))

print("\n")





# DRUGI ZADATAK
# Mjerenjem je ustanovljeno da električni otpor R bakrene žice ovisi o temperaturi t na sljedeći način:

# |  𝑡°𝐶   |  19.1   |   25   |   30.1  |   36   |   40    |  45.1  |   50   |
# |  𝑅(Ω)  |  76.3   |  77.8  |  79.75  |  80.8  |  82.35  |  83.9  |  85.1  | 

# Uz pretpostavku da se radi o linearnoj ovisnosti, odredite parametre a i b linearne funkcije 𝑅(𝑡) = 𝑎𝑡 + 𝑏.

print("DRUGI ZADATAK")

from numpy import *
import pylab as py

t = [19.1, 25, 30.1, 36, 40, 45.1, 50]
R = [76.3, 77.8, 79.75, 80.8, 82.35, 83.9, 85.1]

py.plot(t, R, 'o')

a = polyfit(t, R, 1)                           # p(t) = a + bt, a = a[1], b = a[0]
print("Parametar a:", a[1])                    # Parametar a: 70.76237423464201
print("Parametar b:", a[0])                    # Parametar b: 0.28806922281902125

def fun(t):
    return a[0] * t + a[1]

t_domena = linspace(19, 51, 1000)
py.plot(t_domena, fun(t_domena))

print("\n")





# TREĆI ZADATAK (4)

# Neka je zadano pet točaka u ravnini:

# |   x   |   1   |   3   |   4   |   6   |   7   |
# |   y   |   1   |   3   |   2   |   4   |   3   |

# Izračunajte i nacrtajte regresijski polinom trećeg stupnja.

print("TREĆI ZADATAK")

from numpy import *
import pylab as py

x = [1, 3, 4, 6, 7]
y = [1, 3, 2, 4, 3]

py.plot(x, y, 'o')

a = polyfit(x, y, 3)                       

def fun(x):
    return a[0] * x**3 + a[1] * x**2 + a[2] * x + a[3]

x_domena = linspace(0, 8, 100)
py.plot(x_domena, fun(x_domena))

print("\n")





# ČETVRTI ZADATAK
# Zadani su podaci o ulaganju u marketing i ostvarenom godišnjem profitu u 15 turističkih agencija. 

# | Ulaganje (tisuća €) |  15  |  22  |  25   |  30   |  40   |  45   |  50   |  60   |  70   |  80   |  95   |  100   |  120   |  130   |  150   |
# | Profit (tisuća €)   |  80  |  95  |  100  |  120  |  110  |  145  |  130  |  180  |  210  |  200  |  280  |  320   |  350   |  375   |  480   |

# Odredite jednadžbu regresijskog pravca, te podatke prikažite grafički.
# Procijenite i godišnji profit tvrtke koja bi u marketing uložila 220 000 €.

print("ČETVRTI ZADATAK")

from numpy import *
import pylab as py

x = [15, 22, 25, 30, 40, 45, 50, 60, 70, 80, 95, 100, 120, 130, 150]
y = [80, 95, 100, 120, 110, 145, 130, 180, 210, 200, 280, 320, 350, 375, 480]
x *= 1000
y *= 1000

py.plot(x, y, 'o')

a = polyfit(x, y, 1)

def fun(x):
    return a[0] * x + a[1]

x_domena = linspace(0, 200, 100)
py.plot(x_domena, fun(x_domena), 'b')

print("Regresijski pravac:", a)                                             # Regresijski pravac: [ 2.83964054 16.29939719]

print("Profit tvrtke koja bi u marketing uložila 220 000 €:", fun(220000))  # Profit tvrtke koja bi u marketing uložila 220 000 €: 624737.2192453692

print("\n")