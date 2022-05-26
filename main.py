"""
Disciplina: Fundamentos de Programação
Nome: Éverton da Cunha Sousa
Matrícula: 537858  
"""
# Iniciando turtle
from turtle import Screen, Turtle, bye
from module import audio, scenery, move, defaulft
window = Screen()
window.setup(1000, 1000)
window.bgcolor("black")

# Trilha sonora
audio.Asgores_Theme()
scenery.Square()

# Pontuação e vida
score = 0
text = Turtle()
defaulft.TextDefaulft(text, score)
life = 4
heart_1 = Turtle()
defaulft.PostHeart(heart_1, 200)
heart_2 = Turtle()
defaulft.PostHeart(heart_2, 160)
heart_3 = Turtle()
defaulft.PostHeart(heart_3, 120)

#Adicionando shapes e criando personagens 
window.addshape("assets/skin/heart_red.gif")
window.addshape("assets/skin/heart_purple.gif")
window.addshape("assets/skin/heart_blue.gif")

frisk = Turtle()
frisk.up()
frisk.shape("assets/skin/heart_red.gif")
poison = Turtle()
defaulft.ObjDefaulft(poison, "assets/skin/heart_purple.gif")
setPoint = Turtle()
defaulft.ObjDefaulft(setPoint, "assets/skin/heart_blue.gif")

# Movimentação aleatória do poison e setpoint
def RandomMovement():
    '''Movimentação aleatória'''
    while True:
        poison.fd(10)
        move.Random(poison)
        if move.Collision(frisk, poison):
            global life
            life -=1
            defaulft.Teleport(poison)
            if life == 3:
                heart_1.ht()
            if life == 2:
                heart_2.ht()
            if life == 1:
                bye()
                
        setPoint.bk(5)
        move.Random(setPoint)
        if move.Collision(frisk, setPoint):
            global score
            score += 10
            text.clear()
            defaulft.TextDefaulft(text, score)
            defaulft.Teleport(setPoint)
            
move.Movement(frisk)
RandomMovement()
                              
window.tracer(0)
while True:
    window.update()