def PostHeart(obj, x, y=130):
     '''Posicionamento do coração'''
     obj.up()
     obj.speed(0)
     obj.setpos(x, y)
     obj.shape("assets/skin/heart_white.gif")
     
from random import randint

def Teleport(obj):
     '''Teleporte'''
     obj.setpos(randint(0,360), randint(-430,80))

def ObjDefaulft(obj, shape):
     '''Padronização das configurações dos personagens'''
     obj.up()
     obj.speed(0)
     Teleport(obj)
     obj.shape(shape)
     
def TextDefaulft(obj, point):
     '''Padronização dos personagens'''
     obj.up()
     obj.ht()
     obj.speed(0)
     obj.setpos(-190, 120)
     obj.color("white")
     style = ("PressStart2P", 13, "normal")
     obj.write(f"SCORE: {point}", True, "center", style)