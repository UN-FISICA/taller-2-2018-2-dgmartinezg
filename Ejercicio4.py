#!/usr/bin/python
# -*- coding: utf8 -*-
from turtle import *
import msvcrt
import math as m
n= int(input("introdusca el numero de la base de la piramide:  "))#n el numero de la base de la piramide
p= int(input("introdusca el numero de lados de los poligonos en la piramide:  ")) #p numero de lados del poligono
lado=15
d=0             #p numero de lados del poligono
for j in range(n): #este for controla la altura de la piramide
	penup()
	goto(2*d*lado,2*d*lado+2*d)
	pendown()
	for i in range(n): #este for controla la repeticion en cada fila de la piramide
		penup()
		forward(lado*4)
		pendown()
		for k in range(p): #este for da forma a cada figura de la piramide
			forward(lado)
			left(360/p)            
	n=n-1
	d=d+1
	print("n= ",n) #imprime para revisar como cambian las variables 
	print("d= ",d)
msvcrt.getch()
    



                    
                









