# !/usr/bin/python3
# coding: UTF-8

"""
	Um elétron é projetado com uma velocidade inicial Vi = 3 * 10^6 m/s na direção x na região entre duas placas carregadas com cargas opostas. Quando o elétron deixa a região entre as placas, ele sofreu uma deflexão vertical de 2cm. Suponha que o campo elétrico entre as placas e que o campo elétrico fora da região das placas seja nulo.

	a) Qual a intensidade do campo elétrico entre as placas?
	b) Em qual ponto Yf sobre a tela localizada a 1m de distância das placas o elétron irá colidir?
"""

# F = q*E = m*a
# E = (me/qe)*a

"""
	comp_placa = 0.5
	distancia_tela = 1.0

	vi = 3*10**6
	x0 = 0
	v0x = vi

	x = x0 + v0x*t + 1/2*ax*t**2
	x = vi*t

	t = x/vi = 0.5 / (3*10^6)
	t = 0.166 * 10**(-6) s

	y = y0 + v0y*t + (1/2)*ay*t**2
	y = (1/2)*a*t**2 => a = 2y/t**2 => NÃO TERMNEI AQUI
"""

# Massa elétron
mE = 9.11e-31

# Carga Elétron
qE = 1.6e-19

# Valor de x
comp_placa = 0.5 

x0 = 0
vi = 3*10**6

t = comp_placa / vi
print(f'\nTempo: {t}')

y = 2e-2

a = 2*y/t**2

print(f'\nAceleração: {a}')

E = mE*a/qE

print(f'\nCampo Elétrico: {E} N/C')




