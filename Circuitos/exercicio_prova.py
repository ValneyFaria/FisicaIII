"""
Duas partículas carregadas são mantidas a 1m de distância uma da outra. A partícula 1 possui uma massa mA = 20g e uma carga qA = 6*10^(-6) C. A partícula 2 possui masssa mB = 50g e uma carga qB = -4*10^(-6) C. As partículas são liberadas a partir do repouso simultaneamente.

1) Faça um programa em Python para calcular as velocidades das partículas em função da distância entre elas.

2) Coloque no programa também em qual distância da posição inicial elas irão colidir, em função da distância inicial entre elas.

pedir d inicial
pedir d atual
"""

from math import sqrt

mA = 20
mB = 50

qA = 6e-6
qB = -4e-6

K = 8.99e9

temp = input('Insira a distancia inicial:')

distancia = float(temp)

U = (qA * abs(qB))/distancia

Forca = (qA * abs(qB))/(distancia**2)

aA = Forca/mA

aB = Forca/mB

Ui = (mA + mB)

vA = sqrt((2*U*mB)/(mA*(mA + mB)))
print(f'vA: {vA}')

vB = -(mA * vA) / mB
print(f'vB: {vB}')

vA = sqrt(abs((2*K*qA*qB*mB) / (distancia*(mA + mB)*mA)))
print(f'vA: {vA}')

vB = -(vA*mB)/mB
print(f'vB: {vB}')