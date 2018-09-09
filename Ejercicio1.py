from turtle import *
def cuadrado(lado):
	for i in range(4):
		penup()
		forward(100)
		pendown()
		for j in range(5):
			forward(lado)
			right(90)
			
