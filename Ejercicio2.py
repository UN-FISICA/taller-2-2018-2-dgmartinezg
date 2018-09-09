from turtle import *
import msvcrt
import math as m
lado=30
n = int(input("introdusca el numero de lados del poligono en las equinas"))
for i in range(4):
	penup()
	goto(100*m.cos((135+90*i)*(m.pi/180)),100*m.sin((135+90*i)*(m.pi/180)))
	pendown()
	for j in range(n):
		forward(lado)
		left(360/n)
msvcrt.getch()                        

