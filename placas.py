# !/usr/bin/python3
# coding: UTF_8

xzero, xplaca, xfinal = 0, 0.5, 1.5
vi = 3e6
mE, qE = 9.11e-31,1.6e-19
tplaca = (xplaca - xzero)/vi
# 8.19
temp = input('Enter the value of E: ')
E = float(temp)

acc = (qE*E)/mE

yplaca = (1/2)*acc*tplaca**2
tlivre = (xfinal-xplaca)/vi
vy = acc *tplaca
yfinal = yplaca+vy*tlivre

print(yfinal)

