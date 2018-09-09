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
## Ejercicio3
Con base en el ejercico anterior,para solicitar el número de lados del poligono de alineación, se introdujó una variable nueva **p**
que controla las coordenadas dentro del **goto()** esto lo que hace es que dependiendo del número que se le introdusca redirecciona las coordenadas y allí dibuja el poligono deseado. 

por ejemplo si se le introduce el número 5 lo que hace es divir la circunferencia en 5 partes iguales y empezando en 90 grados para que este alineado comienza a dibujar en cada lugar el poligono deseado.

~~~
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
~~~
# Ejercicio4
Para resolver el problema de dibujar la siguiente fila de la piramide se implementó un **for** que controla la altura de la piramide, se necesitaba que cada vez que dibujara una fila subiera a la siguiente hasta dibujar la punta. para esto el contador **d** aumenta hasta el valor de **n** que es justamente el número de las poligonos en la base y el número de filas de la piramide, cuando **d=n** el for acaba y se termina el programa.

Como cada que avanza a la siguiente fila el número de polígonos es menor en **uno** el contador **n** va disminuyendo, sin embargo, esto no afecta la altura porque el valor retorna al **for** que controla el número de poligonos por fila.

Para ver como cambia los número **n** y **p** se imprimen despues de terminar cada fila. 
~~~
import msvcrt
import math as m
n= int(input("introdusca el numero de la base de la piramide:  "))#n el numero de la base de la piramide
p= int(input("introdusca el numero de lados de los poligonos en la piramide:  ")) #p numero de lados del poligono
lado=15
d=0            
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
~~~
