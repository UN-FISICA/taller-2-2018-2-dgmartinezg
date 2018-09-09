#!/usr/bin/python
# -*- coding: utf8 -*-
from turtle import *
import math as m
import msvcrt
r=20
n =int(input("introdusca el numero de la base de la piramide:  ")) 
p =int(input("introdusca el numero de lados del poligono: ")) 
d=0
for j in range(n): 
	penup()
	goto(2*d*r,3*d*r+3*d)
	pendown()
	for i in range(n): 
		penup()
		forward(r*4)
		pendown()
		for k in range(p): 
			forward(2*r*m.sin((180/p)*m.pi/180))
			left(360/(p))      
	p=p-1   
	n=n-1
	d=d+1
msvcrt.getch()
