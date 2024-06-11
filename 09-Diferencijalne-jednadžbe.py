print("\n")
print("VJEŽBE - 09 \n")

print("Zadatke treba riješiti upotrebom scipy.integrate.odeint ili neke druge preporučene metode.")
print("\n")

# PRVI ZADATAK
# Na intervalu [1, 3] na 100 uniformno raspoređenih točaka pronađite i prikažite slikom približno rješenje
# obične diferencijalne jednadžbe y' + y = x.
# Koristite početni uvjet y(1) = 1. Usporedite numeričko rješenje s analitičkim rješenjem 
# y = (e ** (-x + 1)) + x - 1. 

print("PRVI ZADATAK")

from numpy import *
from scipy import integrate as i
import pylab as py

def fun(y, x):
    return x - y

x = linspace(1, 3, 100)
rjesenje = i.odeint(fun, 1, x)

# Usporedba s analitičkim rješenjem
def analiticko_rjesenje(x):
    return exp(-x + 1) + x - 1

py.plot(x, rjesenje, 'b')
py.plot(x, analiticko_rjesenje(x), 'r')

# Provjera uvjeta
print("Rješenje u čvoru 1: ", rjesenje[0])                      # Rješenje u čvoru 1:  [1.]

print("\n")





# DRUGI ZADATAK
# Na intervalu [0, 3] na 100 uniformno raspoređenih točaka pronađite i prikažite slikom približno rješenje
# obične diferencijalne jednadžbe y' - 2 * y = x.
# Koristite početni uvjet y(0) = 2. Usporedite numeričko rješenje s analitičkim rješenjem 
# y = ((9 / 4) * e ** (2 * x)) - (1 / 2) * x - (1 / 4).   

print("DRUGI ZADATAK")

from numpy import *
from scipy import integrate as i
import pylab as py

def fun(y, x):
    return x + 2 * y

x = linspace(0, 3, 100)
rjesenje = i.odeint(fun, 2, x)

# Usporedba s analitičkim rješenjem
def analiticko_rjesenje(x):
    return ((9 / 4) * exp(2 * x)) - (1 / 2) * x - (1 / 4)

py.plot(x, rjesenje, 'b')
py.plot(x, analiticko_rjesenje(x), 'r')

# Provjera uvjeta
print("Rješenje u čvoru 0: ", rjesenje[0])                      # Rješenje u čvoru 0:  [2.]

print("\n")