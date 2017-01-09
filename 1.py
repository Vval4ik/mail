#comp
import random
import turtle

def gotoxy(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()

x =random.randint(1,100)

print(x)

turtle.speed(0)

turtle.circle(30)

gotoxy(150,90)

turtle.circle(30)



input('Нажмите любую клавишу')