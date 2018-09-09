#!/usr/bin/python
# -*- coding: utf8 -*-
from turtle import *
import math as m
def pira(n,p,lado): #n el numero la base , lado es el largo del lado del poligono
    d=0             #p numero de lados del poligono
    for j in range(n): #este for controla la altura de la piramide
        penup()
        goto(d*lado,d*lado+d)
        pendown()
        for i in range(n): #este for controla la repeticion en cada fila de la piramide
            penup()
            forward(lado*2)
            pendown()
            for k in range(p): #este for da forma a cada figura de la piramide
                forward(lado)
                left(360/p)
            
            print(i)  #imprime el numero de poligonos en cada fila
            
        n=n-1
        d=d+1
        
        print("n= ",n) #imprime para revisar como cambian las variables 
        print("d= ",d)

    



                    
                









