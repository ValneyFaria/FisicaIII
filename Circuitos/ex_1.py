"""
    Aplicação: Escreva um programa em Python para calcular a carga, a corrente e a diferença de potencial entre as placas de um capacitor sendo carregado.
"""

from math import exp

R, C, fem = 1000, 100e-6, 10

temp = input('Insira o valor do tempo em segundos: ')

t = float(temp)

q = C*fem*(1 - exp(-t/(R*C)))

i = (fem/R)*exp(-t/(R*C))

vc = fem * (1 - exp(-t/(R*C)))

print('q = ', q, 'C')
print('i = ', i, 'A')
print('VC = ', vc, 'V')
