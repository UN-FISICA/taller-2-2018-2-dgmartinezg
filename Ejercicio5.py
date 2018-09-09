#!/usr/bin/python
# -*- coding: utf8 -*-
from turtle import *
import math as m
import msvcrt
lado=20
n =int(input("introdusca el numero de la base de la piramide:  ")) 
p =int(input("introdusca el numero de lados del poligono: ")) 
d=0
for j in range(n): #este for controla la altura de la piramide
	penup()
	goto(1.25*d*lado,3*d*lado+3*d)
	pendown()
	for i in range(n): #este for controla la repeticion en cada fila de la piramide
		penup()
		forward(lado*2.5)
		pendown()
		for k in range(p): #este for da forma a cada figura de la piramide
			forward(lado)
			left(360/(p))      
	p=p-1   
	n=n-1
	d=d+1
	if p==0:
		exit()
msvcrt.getch()
