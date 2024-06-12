print("\n")
print("VJEŽBE - 05 \n")
print("LINEARNI I KUBIČNI SPLINE \n")

# PRVI ZADATAK
# Aproksimirajte linearnim splajnom funkciju x ** 2 * sin(x) na intervalu [-π, π].
# Koristite uniformnu mrežu od 10, 20 i 40 numeričkih čvorova.
# Izračunajte apsolutnu pogrešku aproksimacije u čvoru x = 1 za sva tri slučaja.

print("PRVI ZADATAK")

from numpy import *
from scipy import interpolate as i
import pylab as py

def fun(x):
    return x ** 2 * sin(x)

x_domena = linspace(-pi - 0.3, pi + 0.3, 1000)
py.plot(x_domena, fun(x_domena), 'r')

# 10 numeričkih čvorova
x_10 = linspace(-pi, pi, 10)
linearni_splajn_10 = i.interp1d(x_10, fun(x_10), kind = 'linear')
py.plot(x_10, fun(x_10), 'o')
py.plot(x_10, linearni_splajn_10(x_10))

# 20 numeričkih čvorova
x_20 = linspace(-pi, pi, 20)
linearni_splajn_20 = i.interp1d(x_20, fun(x_20), kind = 'linear')
py.plot(x_20, fun(x_20), 'o')
py.plot(x_20, linearni_splajn_20(x_20))

# 40 numeričkih čvorova
x_40 = linspace(-pi, pi, 40)
linearni_splajn_40 = i.interp1d(x_40, fun(x_40), kind = 'linear')
py.plot(x_40, fun(x_40), 'o')
py.plot(x_40, linearni_splajn_40(x_40))

apsolutna_pogreska_10 = abs(fun(1) - linearni_splajn_10(1)) 
apsolutna_pogreska_20 = abs(fun(1) - linearni_splajn_20(1))
apsolutna_pogreska_40 = abs(fun(1) - linearni_splajn_40(1))

print("Apsolutna pogreška aproksimacije u čvoru x = 1 za 10 čvorova:", apsolutna_pogreska_10)
# Apsolutna pogreška aproksimacije u čvoru x = 1 za 10 čvorova: 0.046844375273971006

print("Apsolutna pogreška aproksimacije u čvoru x = 1 za 20 čvorova:", apsolutna_pogreska_20)
# Apsolutna pogreška aproksimacije u čvoru x = 1 za 20 čvorova: 0.0406973709038545

print("Apsolutna pogreška aproksimacije u čvoru x = 1 za 40 čvorova:", apsolutna_pogreska_40)
# Apsolutna pogreška aproksimacije u čvoru x = 1 za 40 čvorova: 0.008182134279433484

print("\n")





# DRUGI ZADATAK
# Kubičnim splajnom aproksimirajte funkciju 1 / 1 + 5 * x ** 2 na intervalu [-1, 1], 
# upotrebom 5, 10 i 20 čvorova. Izračunajte relativnu pogrešku u čvoru 0.95 za sva tri slučaja.

print("DRUGI ZADATAK")

from numpy import *
from scipy import interpolate as i
import pylab as py

def fun(x):
    return 1 / (1 + 5 * x ** 2)

x_domena = linspace(-1, 1, 1000)
py.plot(x_domena, fun(x_domena), 'r')

# 5 čvorova
x_5 = linspace(-1, 1, 5)
kubicni_splajn_5 = i.interp1d(x_5, fun(x_5), kind = 'cubic')
py.plot(x_5, fun(x_5), 'o')
py.plot(x_5, kubicni_splajn_5(x_5))
relativna_pogreska_5 = abs(fun(0.95) - kubicni_splajn_5(0.95)) / abs(fun(0.95))
print("Relativna pogreška u čvoru 0.95 za 5 čvorova:", relativna_pogreska_5)
# Relativna pogreška u čvoru 0.95 za 5 čvorova: 0.3243359375000002

# 10 čvorova
x_10 = linspace(-1, 1, 10)
kubicni_splajn_10 = i.interp1d(x_10, fun(x_10), kind = 'cubic')
py.plot(x_10, fun(x_10), 'o')
py.plot(x_10, kubicni_splajn_10(x_10))
relativna_pogreska_10 = abs(fun(0.95) - kubicni_splajn_10(0.95)) / abs(fun(0.95))
print("Relativna pogreška u čvoru 0.95 za 10 čvorova:", relativna_pogreska_10)
# Relativna pogreška u čvoru 0.95 za 10 čvorova: 0.0020590954508729552

# 20 čvorova
x_20 = linspace(-1, 1, 20)
kubicni_splajn_20 = i.interp1d(x_20, fun(x_20), kind = 'cubic')
py.plot(x_20, fun(x_20), 'o')
py.plot(x_20, kubicni_splajn_20(x_20))
relativna_pogreska_20 = abs(fun(0.95) - kubicni_splajn_20(0.95)) / abs(fun(0.95))
print("Relativna pogreška u čvoru 0.95 za 20 čvorova:", relativna_pogreska_20)
# Relativna pogreška u čvoru 0.95 za 20 čvorova: 0.00014353356114083852

print("\n")





# TREĆI ZADATAK
# Na intervalu [-π, π] interpolirajte funkciju x * cos(x) linearnim i kubičnim splajnom.
# Koristite uniformnu mrežu od 10 čvorova. Izračunajte apsolutnu pogrešku aproksimacije u čvoru x = 1.

print("TREĆI ZADATAK")

from numpy import *
from scipy import interpolate as i
import pylab as py

def fun(x):
    return x * cos(x)

x_10 = linspace(-pi, pi, 10)

# Linearni splajn
linearni_splajn_10 = i.interp1d(x_10, fun(x_10), kind = 'linear')
py.plot(x_10, fun(x_10), 'o')

# Kubični splajn
kubicni_splajn_10 = i.interp1d(x_10, fun(x_10), kind = 'cubic')
py.plot(x_10, fun(x_10), 'o')

apsolutna_pogreska_linearni_splajn = abs(fun(1) - linearni_splajn_10(1))
apsolutna_pogreska_kubicni_splajn = abs(fun(1) - kubicni_splajn_10(1))

print("Apsolutna pogreška aproksimacije u čvoru x = 1 za linearni splajn:", apsolutna_pogreska_linearni_splajn)
# Apsolutna pogreška aproksimacije u čvoru x = 1 za linearni splajn: 0.02992609837798499

print("Apsolutna pogreška aproksimacije u čvoru x = 1 za kubični splajn:", apsolutna_pogreska_kubicni_splajn)
# Apsolutna pogreška aproksimacije u čvoru x = 1 za kubični splajn: 8.643609851921585e-05

print("\n")