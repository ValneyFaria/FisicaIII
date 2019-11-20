# !/usr/bin/python3
# coding: UTF-8

from math import sin, sqrt, tan, pi
from pylab import plot, show

k, l, m, g = 9.0e9, 0.5, 0.1e-3, 9.8

theta = []
theta2 = []
q = []

for x in xrange(5,50):
	theta.append(x)
	theta2 = (float(x)*pi)/180
	q.append(sqrt(((4*l**2)*m*g*(sin(theta2))**2)*(tan(theta2))/k))

plot(q, theta)
show()
