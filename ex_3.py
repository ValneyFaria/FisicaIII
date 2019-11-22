"""
    Dois prótons são mantidos fixos separados por 10 cm. Um terceiro próton é projetado desde muito longe com alguma velocidade inicial vi como mostrado na figura.
    
    a) Qual o menor valor de vi que permitirá ao próton atingir o ponto médio da linha unindo os 2 prótons fixos?

    b) Se a velocidade inicial for metade do valor calculdado em (a), qual a distância que o próton chegará de 0 antes de parar?
"""
from math import sqrt, pi

print('------------------------------- Letra A -------------------------------')

"""
    Programa para calcular a distância do ponto médio que o próton para em função da velocidade inicial do próton incidente e da distância entre os prótons fixos.
"""

mP = 1.67e-27
E0 = 8.85e-12
qP = 1.6e-19

vi = input('Enter value of inital velocity: ')

vi = float(vi)

r = qP**2/(pi*E0*vi**2*mP) 

x = 0.05
# hipotenusa para calcular o valor em y
y = sqrt(r**2 - x**2)
print(y)



print('------------------------------- Letra B -------------------------------')


