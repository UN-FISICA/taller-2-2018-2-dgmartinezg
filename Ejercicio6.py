#!/usr/bin/python
# -*- coding: utf8 -*-
from turtle import *
import math as m
def pira(n,p,r): #n el numero la base
                 #p numero de lados del poligono
                 #r radio de la ircunferencia
    d=0             
    for j in range(n): #este for controla la altura de la piramide
        penup()
        goto(2*d*r,3*d*r+3*d)
        pendown()
        for i in range(n): #este for controla la repeticion en cada fila de la piramide
            penup()
            forward(r*4)
            pendown()
            for k in range(p): #este for da forma a cada figura de la piramide
                forward(2*r*m.sin((180/p)*m.pi/180))
                left(360/(p))
            
            print(i)  #imprime el numero de poligonos en cada fila
        p=p-1   
        n=n-1
        d=d+1
        
        print("n= ",n) #imprime para revisar como cambian las variables 
        print("d= ",d)
