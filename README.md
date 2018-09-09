# Taller2-2018-2

## Ejercicio1:
Este ejercicio es bastante sencillo, utiliza un for hasta un rango de 4 donde en cada paso lo que hace es dibujar un cuadro.
Para dibujar cada cuadro utiliza otro for que pinta el cuadro en cada esquina.
Como estoy utilizando windows es necesario para mantener la pantalla de turtle abierta importar  *import msvcrt* y alfinal del programa  *msvcrt.getch()* esto para es para que no se cierre la pantalla 

~~~ 
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
  ~~~
  Para compilar en ubunto o otro sistema, solo es quitar  *import msvcrt* y *msvcrt.getch()* y poner al final ´raw_input()'
  # Ejercicio2
Para solucionar el problema de pintar los poligonos con la base horizontal se utilizo la funcion **got(x,y)** para decirle al turtle donde pintar cada poligono. Como es en las puntas de un cuadrado donde se pintan los poligonos, las coordenadas estan dadas en por los cosenos y senos de cada posicion
~~~ 
goto(100*m.cos((135+90*i)*(m.pi/180)),100*m.sin((135+90*i)*(m.pi/180)))
~~~
Asi, el programa por defecto pinta los poligonos con la base orientada horizontalmen.
~~~
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
~~~

Para compilar en ubunto o otro sistema, solo es quitar  *import msvcrt* y *msvcrt.getch()* y poner al final **raw_input()**
