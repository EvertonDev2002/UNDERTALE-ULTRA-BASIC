from turtle import onkeypress, listen
from random import randint
from math import sqrt, pow

def Movement(player):
     '''Movimentação pelo teclado'''
     def Rt():
          if player.xcor() + 10 < 260.0:
               player.setx(player.xcor() + 10)
     def Lt():
          if player.xcor() - 10 > -260.0:
               player.setx(player.xcor() - 10)
     def Up():
          if player.ycor() + 10 < 80.0:
               player.sety(player.ycor() + 10)
     def Dw():
          if player.ycor() - 10 > -430.0:
               player.sety(player.ycor() - 10)
               
     listen()
     onkeypress(Up, "Up")
     onkeypress(Dw, "Down")
     onkeypress(Lt, "Left")
     onkeypress(Rt, "Right")
     
def Random(obj):
     '''Restrição do movimento'''
     if obj.ycor() > 70.0:
          obj.sety(-400.0)
          obj.seth(randint(0,360))
          
     if obj.ycor() < -400.0:
          obj.sety(70.0)
          obj.seth(randint(0,360))
          
     if obj.xcor() > 230.0:
          obj.setx(230.0)
          obj.seth(randint(0,360))
          
     if obj.xcor() < -230.0:
          obj.setx(-230.0)
          obj.seth(randint(0,360))
          
def Collision(obj1, obj2):
     '''Checagem da colisão'''
     collision = sqrt(pow(obj1.xcor() - obj2.xcor(), 2) + pow(obj1.ycor() - obj2.ycor(), 2))
     if collision <= 20: # Enquanto o resultado da raiz for menor do que 20, há colisão.
          return True