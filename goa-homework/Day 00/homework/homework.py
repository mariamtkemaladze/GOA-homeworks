from turtle import *
speed(30)

#we want to paint a house

#step 1: draw a square
width(7)
color("purple")


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)

forward(120)     #height of the door
right(90)

forward(60)
right(90)

forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
left(180)
left(30)
forward(190)
left(117)
forward(195)
end_fill()


color("blue")
penup()
goto(70, 120)
pendown()

right(147)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

penup()
goto(130, 120)
pendown()

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)


exitonclick()




























































exitonclick()