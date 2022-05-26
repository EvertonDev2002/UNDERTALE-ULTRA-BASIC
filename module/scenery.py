from turtle import Turtle, addshape

addshape("assets/skin/heart_white.gif")
addshape("assets/skin/Asgores.gif")

asgores = Turtle()
asgores.up()
asgores.speed(0)
asgores.setpos(60,350)
asgores.shape("assets/skin/Asgores.gif")

def Square():
     '''Criação do quadrado'''
     pencel = Turtle()
     pencel.up()
     pencel.speed(0)
     pencel.shape("blank")
     pencel.setpos(-270, 100)
     pencel.width(5)
     pencel.pd()
     pencel.color("white")
     
     for _ in range(4):
          pencel.fd(500)
          pencel.rt(90)