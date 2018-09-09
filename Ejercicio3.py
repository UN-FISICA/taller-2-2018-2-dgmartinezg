from turtle import *
import math as m
import msvcrt
lado=30
n=int(input("introdusca el numero de lados del poligono de las puntas"))
p=int(input("introdusca el numero de lados del poligo grande"))
for i in range(p):
	penup()
	goto(100*m.cos((90+(360/p)*i)*(m.pi/180)),100*m.sin((90+(360/p)*i)*(m.pi/180)))
	pendown()
	for j in range(n):
		forward(lado)
		left(360/n)
msvcrt.getch()
