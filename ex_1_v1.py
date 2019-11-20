# !/usr/bin/python3
# coding: UTF-8

from math import sin, sqrt, tan, pi

k, l, m, g = 9.0e9, 0.5, 0.1e-3,9.8

temp = input("Enter the value of theta:")
theta = float(temp)
print(f'The value of theta is {theta}')
theta2 = (theta*pi)/180
q = sqrt(((4.*l**2)*(m*g)*(sin(theta2))**2)*(tan(theta2)/k))

print(f'q = {q}C')