print("\n")
print("VJEŽBE - 02 \n")

# PRVI ZADATAK - prvi dio
# Ispitajte je li sustav linearnih jednadžbi dobro ili loše uvjetovan. Izračunati rješenje i za b = [2, 2.001].
# x + y = 2
# x + 1.001y = 2

print("PRVI ZADATAK - prvi dio")

from numpy import *
from numpy import linalg

A = array([[1, 1], [1, 1.001]])
b = array([2, 2])

rjesenje = linalg.solve(A, b)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [2, 0.]

b = array([2, 2.001])
rjesenje = linalg.solve(A, b)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [1, 1.]

uvjetovanost = linalg.norm(A, 2) * linalg.norm(linalg.inv(A), 2)
print("Uvjetovanost sustava je:", uvjetovanost.round(4))                # Uvjetovanost sustava je: 4002.0008
print("\n")





# PRVI ZADATAK - drugi dio
# Ispitajte je li sustav linearnih jednadžbi dobro ili loše uvjetovan. Izračunati rješenje i za b = [2, 2.001].
#  x +  y = 2
# -x + 2y = 2

print("PRVI ZADATAK - drugi dio")

from numpy import *
from numpy import linalg

A = array([[1, 1], [-1, 2]])
b = array([2, 2])

rjesenje = linalg.solve(A, b)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [0.66666667 1.33333333]

b = array([2, 2.001])
rjesenje = linalg.solve(A, b)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [0.66633333 1.33366667]

uvjetovanost = linalg.norm(A, 2) * linalg.norm(linalg.inv(A), 2)
print("Uvjetovanost sustava je:", uvjetovanost.round(2))                # Uvjetovanost sustava je: 1.77
print("\n")





# DRUGI ZADATAK
# Izračunajte uvjetovanost matrice u 2 i ∞ normi.
# | 2  0  0 |
# | 0 -3  3 |
# | 0  3  5 |

print("DRUGI ZADATAK")

from numpy import *
from numpy import linalg

A = array([[2, 0, 0], [0, -3, 3], [0, 3, 5]])
b = array([2, 2])

uvjetovanost_2 = linalg.norm(A, 2) * linalg.norm(linalg.inv(A), 2)
print("Uvjetovanost matrice u 2 normi je:", uvjetovanost_2)                # Uvjetovanost matrice u 2 normi je: 3.0

uvjetovanost_inf = linalg.norm(A, inf) * linalg.norm(linalg.inv(A), inf)
print("Uvjetovanost matrice u ∞ normi je:", uvjetovanost_inf)              # Uvjetovanost matrice u ∞ normi je: 4.0
print("\n")





# TREĆI ZADATAK - prvi dio
# Rješenje sustava gdje su matrica sustava A i vektor b dani sa:
#               A = | 0.434 0.26  |       b = | 0.694 |
#                   | 0.79  0.473 |           | 1.263 |
# iznosi        x = | 1 |
#                   | 1 |
# Promijenite vektor b za ∆b = | 0.00006  | i izračunajte cond∞ (A).
#                              | 0.000003 |
# Koliko je puta relativna greška u rješenju sustava uz promjenu vektora b veća od relativne greške u vektoru b?

print("TREĆI ZADATAK - prvi dio")

from numpy import *
from numpy import linalg

A = array([[0.434, 0.26], [0.79, 0.473]])
b = array([0.694, 1.263])

rjesenje = linalg.solve(A, b)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [1. 1.]

uvjetovanost = linalg.norm(A, inf) * linalg.norm(linalg.inv(A), inf)
print("Uvjetovanost matrice u ∞ normi je:", uvjetovanost.round(2))      # Uvjetovanost matrice u ∞ normi je: 13100.95

delta_b = array([0.00006, 0.000003])
b_b = b + delta_b

rjesenje_b = linalg.solve(A, b_b)
print("Rješenje sustava s promjenom u b je:", rjesenje_b)               # Rješenje sustava s promjenom u b je: [0.76610169 1.39066102]

relativna_greska_b = linalg.norm(delta_b, inf) / linalg.norm(b, inf)
relativna_greska_sustava = linalg.norm(rjesenje - rjesenje_b, inf) / linalg.norm(rjesenje, inf)
print("Relativna greška u rješenju sustava je", (relativna_greska_sustava / relativna_greska_b).round(1), "puta veća od relativne greške u vektoru b.")
# Relativna greška u rješenju sustava je 8223.4 puta veća od relativne greške u vektoru b.
print("\n")





# TREĆI ZADATAK - drugi dio
# Rješenje sustava gdje su matrica sustava A i vektor b dani sa:
#               A = | 0.434 0.26  |       b = | 0.694 |
#                   | 0.79  0.473 |           | 1.263 |
# iznosi        x = | 1 |
#                   | 1 |
# Promijenite matricu A za ∆A = | -0.001 0 | i izračunajte cond∞ (A).
#                               |  0     0 |
# Koliko je puta relativna greška u rješenju sustava uz promjenu matrice A veća od relativne greške u matrici A?

print("TREĆI ZADATAK - drugi dio")

from numpy import *
from numpy import linalg

A = array([[0.434, 0.26], [0.79, 0.473]])
b = array([0.694, 1.263])

rjesenje = linalg.solve(A, b)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [1. 1.]

uvjetovanost = linalg.norm(A, inf) * linalg.norm(linalg.inv(A), inf)
print("Uvjetovanost matrice u ∞ normi je:", uvjetovanost.round(2))      # Uvjetovanost matrice u ∞ normi je: 13100.95

delta_A = array([[-0.001, 0], [0, 0]])
A_A = A + delta_A

rjesenje_A = linalg.solve(A_A, b)
print("Rješenje sustava s promjenom u A je:", rjesenje_A)               # Rješenje sustava s promjenom u A je: [0.19966159 2.33671743]

relativna_greska_A = linalg.norm(delta_A, inf) / linalg.norm(A, inf)
relativna_greska_sustava = linalg.norm(rjesenje - rjesenje_A, inf) / linalg.norm(rjesenje, inf)
print("Relativna greška u rješenju sustava je", (relativna_greska_sustava / relativna_greska_A).round(1), "puta veća od relativne greške u matrici A.")
# Relativna greška u rješenju sustava je 1688.3 puta veća od relativne greške u matrici A.
print("\n")





# ČETVRTI ZADATAK - prvi dio
# LU dekompozicijom riješi sustav koji je zadan sa:
#                A = | 1  2  3 |         b = | 2 | 
#                    | 0  2  2 |             | 3 |
#                    | 3  2 -1 |             | 1 |

print("ČETVRTI ZADATAK - prvi dio")

from numpy import *
from scipy import linalg
from numpy import linalg as l

A = array([[1, 2, 3], [0, 2, 2], [3, 2, -1]])

P, L, U = linalg.lu(A)

b = array([2, 3, 1])
y = l.solve(L, dot(l.inv(P), b))
rjesenje = l.solve(U, y)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [-0.83333333  1.66666667 -0.16666667]
print("\n")





# ČETVRTI ZADATAK - drugi dio
# LU dekompozicijom riješi sustav koji je zadan sa:
#                A = | 1  2  3 |         b = | -1 | 
#                    | 0  2  2 |             |  5 |
#                    | 3  2 -1 |             |  2 |

print("ČETVRTI ZADATAK - drugi dio")

from numpy import *
from scipy import linalg
from numpy import linalg as l

A = array([[1, 2, 3], [0, 2, 2], [3, 2, -1]])

P, L, U = linalg.lu(A)

b = array([-1, 5, 2])
y = l.solve(L, dot(l.inv(P), b))
rjesenje = l.solve(U, y)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [-3.5  5. -2.5]
print("\n")





# PETI ZADATAK - prvi dio
# LU dekompozicijom riješi sustav koji je zadan sa:
#                A = | 0  7  8 |         b = | 2 | 
#                    | 0  2  1 |             | 3 |
#                    | 3  0 -1 |             | 1 |

print("PETI ZADATAK - prvi dio")

from numpy import *
from scipy import linalg
from numpy import linalg as l

A = array([[0, 7, 8], [0, 2, 1], [3, 0, -1]])

P, L, U = linalg.lu(A)

b = array([2, 3, 1])
y = l.solve(L, dot(l.inv(P), b))
rjesenje = l.solve(U, y)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [-0.2962963   2.44444444 -1.88888889]
print("\n")





# PETI ZADATAK - drugi dio
# LU dekompozicijom riješi sustav koji je zadan sa:
#                A = | 0  7  8 |         b = | -1 | 
#                    | 0  2  1 |             |  5 |
#                    | 3  0 -1 |             |  2 |

print("PETI ZADATAK - drugi dio")

from numpy import *
from scipy import linalg
from numpy import linalg as l

A = array([[0, 7, 8], [0, 2, 1], [3, 0, -1]])

P, L, U = linalg.lu(A)

b = array([-1, 5, 2])
y = l.solve(L, dot(l.inv(P), b))
rjesenje = l.solve(U, y)
print("Rješenje sustava je:", rjesenje)                                 # Rješenje sustava je: [-0.7037037   4.55555556 -4.11111111]
print("\n")