# Taller2-2018-2

## Ejercicio1:
Este ejercicio es bastante sencillo, utiliza un for hasta un rango de 4 donde en cada paso lo que hace es dibujar un cuadro.
Para dibujar cada cuadro utiliza otro for que pinta el cuadro en cada esquina.
Como estoy utilizando windows es necesario para mantener la pantalla de turtle abierta importar  *import msvcrt* y alfinal del programa  *msvcrt.getch()* esto para es para que no se cierre la pantalla 

~~~  from turtle import *
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
