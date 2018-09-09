from turtle import *
import msvcrt
lado=40
for i in range(4):
	penup()
	forward(100)
	pendown()
	for j in range(5):
		forward(lado)
		right(90)
msvcrt.getch()

