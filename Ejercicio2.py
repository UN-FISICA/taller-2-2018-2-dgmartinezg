from turtle import *
import math as m
def poli(lado,n):
    for i in range(4):
            penup()
            goto(100*m.cos((135+90*i)*(m.pi/180)),100*m.sin((135+90*i)*(m.pi/180)))
            pendown()
            for j in range(n):
                forward(lado)
                left(360/n)
                
                 

