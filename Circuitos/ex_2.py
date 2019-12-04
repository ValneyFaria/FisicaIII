from math import exp
import matplotlib.pyplot as plt
from pylab import plot, show

r, c, fem = 1000, 100e-6, 10

listat = []
listaq = []
listavc = []

for index in range (1, 10):
    t = float(index/10)
    listat.append(t)
    listaq.append(c*fem*(1 - exp(-t/(r*c))))
    listavc.append(fem*(1 - exp(-t/(r*c))))

plot(listat, listaq)
show()
plot(listat, listavc)
show()