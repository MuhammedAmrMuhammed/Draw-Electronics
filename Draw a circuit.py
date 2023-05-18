import turtle

from turtle import *

r = turtle.Turtle()
r.color('black')
r.pensize(1)
r.shape('arrow')
r.speed(10000)
while 1:
    print("Choose the operation")
    op = input(">:")
    if op == "Vdc g":
        r.circle(50)  # making a supply
        r.left(90)
        r.penup()
        r.forward(20)
        r.pendown()
        r.left(90)
        r.forward(10)
        r.backward(25)
        r.penup()
        r.right(90)
        r.forward(50)
        r.pendown()
        r.left(90)
        r.forward(15)
        r.right(90)
        r.forward(15)
        r.backward(30)
        r.forward(15)
        r.left(90)
        r.forward(15)
        r.penup()
        r.backward(15)
        r.right(90)
        r.forward(30)
        r.pendown()
        gnd = turtle.Turtle()
        gnd.color('black')
        gnd.pensize(1)
        gnd.shape('arrow')
        gnd.speed(0)
        gnd.right(90)
        gnd.forward(40)
        gnd.right(90)
        gnd.forward(20)
        gnd.left(135)
        gnd.forward(30)
        gnd.left(90)
        gnd.forward(30)
        gnd.left(135)
        gnd.forward(30)
    elif op == "gnd":
        r.right(90)
        r.forward(40)
        r.right(90)
        r.forward(20)
        r.left(135)
        r.forward(30)
        r.left(90)
        r.forward(30)
        r.left(135)
        r.forward(30)
    elif op == "und":
        r.undo()
    elif op == "w":
        r.penup()
        r.forward(5)
        r.pendown()
    elif op == "VdcN":
        r.circle(50)
        r.left(90)
        r.penup()
        r.forward(20)
        r.pendown()
        r.left(90)
        r.forward(10)
        r.backward(25)
        r.penup()
        r.right(90)
        r.forward(50)
        r.pendown()
        r.left(90)
        r.forward(15)
        r.right(90)
        r.forward(15)
        r.backward(30)
        r.forward(15)
        r.left(90)
        r.forward(15)
        r.penup()
        r.backward(15)
        r.right(90)
        r.forward(30)
        r.pendown()
    elif op == "VdcP":
        r.circle(50)
        r.left(90)
        r.penup()
        r.forward(20)
        r.pendown()
        r.left(90)
        r.forward(10)
        r.backward(25)
        r.penup()
        r.right(90)
        r.forward(50)
        r.pendown()
        r.left(90)
        r.forward(15)
        r.right(90)
        r.forward(15)
        r.backward(30)
        r.forward(15)
        r.left(90)
        r.forward(15)
        r.penup()
        r.backward(15)
        r.right(90)
        r.forward(30)
        r.pendown()
    elif op == "R":
        r.forward(50)
        r.forward(0)
        r.left(45)
        r.forward(15)
        r.right(90)
        r.forward(15)
        r.left(90)
        r.forward(15)
        r.right(90)
        r.forward(15)
        r.left(90)
        r.forward(15)
        r.right(90)
        r.forward(15)
        r.left(90)
        r.forward(15)
        r.right(90)
        r.forward(15)
        r.left(45)
        r.forward(15)
    elif op == "R g":
        r.forward(100)
        r.forward(20)
        r.left(45)
        r.forward(30)
        r.right(90)
        r.forward(30)
        r.left(90)
        r.forward(30)
        r.right(90)
        r.forward(30)
        r.left(90)
        r.forward(30)
        r.right(90)
        r.forward(30)
        r.left(90)
        r.forward(30)
        r.right(90)
        r.forward(30)
        r.left(45)
        r.forward(30)
        #r.left(90)
        r.forward(40)
        r.right(90)
        r.forward(20)
        r.left(135)
        r.forward(30)
        r.left(90)
        r.forward(30)
        r.left(135)
        r.forward(30)
        #end of making a resistor
    elif (op == "C"):
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.backward(40)
        r.penup()
        r.right(90)
        r.forward(10)
        r.left(90)
        r.pendown()
        r.forward(40)
        r.backward(20)
        r.right(90)
        r.forward(50)
    elif op == "W":
        r.forward(70)
    elif op  =="C g":
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.backward(40)
        r.penup()
        r.right(90)
        r.forward(10)
        r.left(90)
        r.pendown()
        r.forward(40)
        r.backward(20)
        r.right(90)
        r.forward(50)
        r.left(90)  # ground
        r.forward(40)
        r.right(90)
        r.forward(20)
        r.left(135)
        r.forward(30)
        r.left(90)
        r.forward(30)
        r.left(135)
        r.forward(30)
    elif op== "node":
        r.circle(5)
    elif op == "Q":
        break
    elif op == "r90":
        r.right(90)
        
    elif op == "l90":
        r.left(90)

    elif op == "r45":
        r.right(45)

    elif op == "l45":
        r.right(45)
    elif op =="NMOS":
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.backward(40)
        r.penup()
        r.right(90)
        r.forward(10)
        r.left(90)
        r.pendown()
        r.forward(40)
        r.backward(20)
        r.right(90)
        r.forward(20)
        r.backward(20)
        r.right(90)
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.right(90)
        r.forward(10)
        r.left(180)
        r.forward(10)
        r.left(90)
        r.forward(5)
        r.right(45)
        r.forward(8)
        r.left(135)
        r.forward(10)
        r.left(135)
        r.forward(8)
        r.left(135)
        r.forward(15)
        r.right(90)
        r.forward(40)
        r.right(90)
        r.forward(20)
        r.left(90)
        r.forward(20)
    elif op =="PMOS":
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.backward(40)
        r.penup()
        r.right(90)
        r.forward(10)
        r.left(90)
        r.pendown()
        r.forward(40)
        r.backward(20)
        r.right(90)
        r.forward(20)
        r.backward(20)
        r.right(90)
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.right(90)
        r.forward(10)
        r.left(180)
        r.forward(10)
        r.left(90)
        r.forward(5)
        r.forward(15)
        r.right(90)
        r.forward(40)
        r.right(90)
        r.forward(20)
        r.left(90)
        r.forward(20)
        r.penup()
        r.left(180)
        r.forward(20)
        r.right(90)
        r.forward(5)
        r.pendown()
        r.left(90)
        r.forward(8)
        r.right(135)
        r.forward(10)
        r.right(90)
        r.forward(8)
        r.right(135)
        r.forward(10)

    else:
        print("Wrong Option")






















































































